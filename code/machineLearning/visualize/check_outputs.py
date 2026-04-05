from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, TextBox
import numpy as np
import torch
from torch import nn


def _set_image_pixel_aspect(ax: Any, height: int, width: int) -> None:
    if width > 0 and height > 0:
        ax.set_box_aspect(height / width)


def check_outputs(
    paths: Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]],
    losses: Optional[Union[nn.Module, Dict[str, nn.Module]]] = None,
    show_input: bool = True,
) -> None:
    paths_dict = _normalize_paths(paths)
    losses_dict = _normalize_losses(losses)
    data_list: List[Tuple[str, dict]] = [
        (name, torch.load(p, map_location="cpu", weights_only=False))
        for name, p in paths_dict.items()
    ]

    ref = data_list[0][1]
    has_inputs = "inputs" in ref
    has_outputs = "outputs" in ref
    has_gts = "gts" in ref

    loader_names: List[str] = []
    for sec in ("inputs", "outputs", "gts"):
        if sec in ref:
            loader_names = list(ref[sec].keys())
            break
    if not loader_names:
        raise ValueError("No loader data found in the first .pt file.")

    _Viewer(
        data_list=data_list,
        loader_names=loader_names,
        match_maps=_build_match_maps(data_list, loader_names, has_inputs, has_gts),
        has_inputs=has_inputs,
        has_outputs=has_outputs,
        has_gts=has_gts,
        losses_dict=losses_dict,
        show_input=show_input,
    ).show()


def _normalize_paths(
    paths: Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]],
) -> OrderedDict:
    if isinstance(paths, (str, Path)):
        return OrderedDict({"pt_0": Path(paths).expanduser().resolve()})
    if isinstance(paths, dict):
        return OrderedDict(
            {k: Path(v).expanduser().resolve() for k, v in paths.items()}
        )
    if isinstance(paths, (list, tuple)):
        return OrderedDict(
            {f"pt_{i}": Path(p).expanduser().resolve() for i, p in enumerate(paths)}
        )
    raise TypeError(f"paths must be str, Path, list, or dict; got {type(paths)}")


def _normalize_losses(
    losses: Optional[Union[nn.Module, Dict[str, nn.Module]]],
) -> Dict[str, nn.Module]:
    if losses is None:
        return {}
    if isinstance(losses, nn.Module):
        return {"loss": losses}
    if isinstance(losses, dict):
        return dict(losses)
    raise TypeError(f"losses must be nn.Module, dict, or None; got {type(losses)}")


def _section_sample_count(section: dict) -> int:
    for v in section.values():
        if torch.is_tensor(v):
            return v.shape[0]
        if isinstance(v, (list, tuple)):
            return len(v)
    return 0


def _sample_count(data: dict, loader: str) -> int:
    for sec in ("inputs", "outputs", "gts"):
        section = data.get(sec, {}).get(loader, {})
        if section:
            return _section_sample_count(section)
    return 0


def _build_match_maps(
    data_list: List[Tuple[str, dict]],
    loader_names: List[str],
    has_inputs: bool,
    has_gts: bool,
) -> Dict[str, Dict[str, Dict[int, int]]]:
    if len(data_list) <= 1:
        return {}
    match_sec = "inputs" if has_inputs else ("gts" if has_gts else None)
    ref = data_list[0][1]
    maps: Dict[str, Dict[str, Dict[int, int]]] = {}
    for name, data in data_list[1:]:
        maps[name] = {}
        for loader in loader_names:
            if match_sec is None:
                n = _sample_count(data, loader)
                maps[name][loader] = {i: i for i in range(n)}
                continue
            ref_sec = ref.get(match_sec, {}).get(loader, {})
            oth_sec = data.get(match_sec, {}).get(loader, {})
            if not ref_sec or not oth_sec:
                maps[name][loader] = {}
                continue
            tensor_keys = [
                k for k in ref_sec
                if torch.is_tensor(ref_sec[k])
                and k in oth_sec
                and torch.is_tensor(oth_sec[k])
            ]
            if not tensor_keys:
                n = min(
                    _section_sample_count(ref_sec),
                    _section_sample_count(oth_sec),
                )
                maps[name][loader] = {i: i for i in range(n)}
                continue
            n_ref = ref_sec[tensor_keys[0]].shape[0]
            n_oth = oth_sec[tensor_keys[0]].shape[0]
            mapping: Dict[int, int] = {}
            used: set = set()
            for i in range(n_ref):
                for j in range(n_oth):
                    if j in used:
                        continue
                    if all(
                        torch.equal(ref_sec[k][i], oth_sec[k][j])
                        for k in tensor_keys
                    ):
                        mapping[i] = j
                        used.add(j)
                        break
            maps[name][loader] = mapping
    return maps


class _Viewer:

    def __init__(
        self,
        data_list: List[Tuple[str, dict]],
        loader_names: List[str],
        match_maps: Dict[str, Dict[str, Dict[int, int]]],
        has_inputs: bool,
        has_outputs: bool,
        has_gts: bool,
        losses_dict: Dict[str, nn.Module],
        show_input: bool,
    ) -> None:
        self.data_list = data_list
        self.loader_names = loader_names
        self.match_maps = match_maps
        self.has_inputs = has_inputs
        self.has_outputs = has_outputs
        self.has_gts = has_gts
        self.losses_dict = losses_dict
        self.show_input = show_input
        self.loader_idx = 0
        self.sample_idx = 0
        self.depth_idx = 0
        self._updating = False
        self._init_columns()
        self._build_figure()
        self._update()

    def _init_columns(self) -> None:
        self.columns: List[Tuple[str, int, str]] = []
        if self.show_input and self.has_inputs:
            self.columns.append(("Input", 0, "inputs"))
        if self.has_gts:
            self.columns.append(("GT", 0, "gts"))
        if self.has_outputs:
            single = len(self.data_list) == 1
            for i, (name, _) in enumerate(self.data_list):
                label = "Output" if single else f"Output ({name})"
                self.columns.append((label, i, "outputs"))
        if not self.columns:
            raise ValueError("No data sections to display.")

    def _sec(self, pt_idx: int, key: str, loader: str) -> dict:
        return self.data_list[pt_idx][1].get(key, {}).get(loader, {})

    def _n_samples(self, loader: str) -> int:
        return _sample_count(self.data_list[0][1], loader)

    def _visual_rows_for(self, section: dict) -> int:
        r = 0
        for v in section.values():
            if torch.is_tensor(v):
                r += v.shape[1] if v.ndim >= 2 else 1
            else:
                r += 1
        return r

    def _max_visual_rows(self) -> int:
        mx = 0
        for loader in self.loader_names:
            for _, pi, sk in self.columns:
                mx = max(mx, self._visual_rows_for(self._sec(pi, sk, loader)))
        return max(mx, 1)

    def _any_3d(self) -> bool:
        for loader in self.loader_names:
            for _, pi, sk in self.columns:
                for v in self._sec(pi, sk, loader).values():
                    if torch.is_tensor(v) and v.ndim == 5:
                        return True
        return False

    def _max_depth(self, loader: str) -> int:
        d = 1
        for _, pi, sk in self.columns:
            for v in self._sec(pi, sk, loader).values():
                if torch.is_tensor(v) and v.ndim == 5:
                    d = max(d, v.shape[2])
        return d

    def _build_figure(self) -> None:
        n_cols = len(self.columns)
        max_rows = self._max_visual_rows()
        self._has_3d_flag = self._any_3d()
        has_loss = bool(self.losses_dict) and self.has_gts and self.has_outputs
        n_ctrl_rows = 2 + int(self._has_3d_flag)

        fig_width = min(max(5.5 * n_cols, 10), 36)
        fig_height = min(
            max(
                (max_rows + 1) * 3.2 + n_ctrl_rows * 0.55 + (0.5 if has_loss else 0),
                8,
            ),
            28,
        )
        self.fig = plt.figure(figsize=(fig_width, fig_height))

        ratios = [(max_rows + 1) * 5]
        if has_loss:
            ratios.append(1)
        ratios.append(n_ctrl_rows)
        outer = self.fig.add_gridspec(
            len(ratios), 1, height_ratios=ratios, hspace=0.07,
        )

        row_ratios = [0.1] + [1] * max_rows
        data_gs = outer[0].subgridspec(
            max_rows + 1, n_cols,
            height_ratios=row_ratios, hspace=0.05, wspace=0.25,
        )
        self._header_axes: List[Any] = []
        self._header_texts: List[Any] = []
        for c in range(n_cols):
            ax = self.fig.add_subplot(data_gs[0, c])
            ax.axis("off")
            self._header_axes.append(ax)
            self._header_texts.append(ax.text(
                0.5, 0.5, self.columns[c][0],
                ha="center", va="center", fontsize=11, fontweight="bold",
                transform=ax.transAxes,
            ))

        self._data_axes: List[List[Any]] = []
        for c in range(n_cols):
            col_axes = []
            for r in range(max_rows):
                ax = self.fig.add_subplot(data_gs[r + 1, c])
                ax.axis("off")
                col_axes.append(ax)
            self._data_axes.append(col_axes)

        self._cell_imgs: List[List[Any]] = []
        self._cell_lines: List[List[Any]] = []
        self._cell_texts: List[List[Any]] = []
        for c in range(n_cols):
            imgs, lines, txts = [], [], []
            for r in range(max_rows):
                ax = self._data_axes[c][r]
                im = ax.imshow(
                    [[0.0]],
                    aspect="equal",
                    interpolation="nearest",
                    cmap="viridis",
                    visible=False,
                )
                _set_image_pixel_aspect(ax, 1, 1)
                imgs.append(im)
                ln, = ax.plot([], [], visible=False)
                lines.append(ln)
                t = ax.text(
                    0.5, 0.5, "", va="center", fontsize=9,
                    transform=ax.transAxes, visible=False,
                )
                txts.append(t)
            self._cell_imgs.append(imgs)
            self._cell_lines.append(lines)
            self._cell_texts.append(txts)

        grid_idx = 1
        if has_loss:
            self._loss_ax = self.fig.add_subplot(outer[grid_idx])
            self._loss_ax.axis("off")
            self._loss_text = self._loss_ax.text(
                0.5, 0.5, "",
                ha="center", va="center", fontsize=10,
                transform=self._loss_ax.transAxes,
            )
            grid_idx += 1
        else:
            self._loss_ax = None
            self._loss_text = None

        ctrl_gs = outer[grid_idx].subgridspec(n_ctrl_rows, 1, hspace=0.35)

        loader_row_gs = ctrl_gs[0].subgridspec(1, 12, wspace=0.05)
        loader_mid = loader_row_gs[0, 3:9].subgridspec(1, 7, wspace=0.32)
        self._btn_lp = Button(self.fig.add_subplot(loader_mid[0, 2]), "Prev")
        self._loader_ax = self.fig.add_subplot(loader_mid[0, 3])
        self._loader_ax.axis("off")
        self._loader_text = self._loader_ax.text(
            0.5, 0.5, "",
            ha="center", va="center", fontsize=11, fontweight="bold",
            transform=self._loader_ax.transAxes,
        )
        self._btn_ln = Button(self.fig.add_subplot(loader_mid[0, 4]), "Next")

        sample_gs = ctrl_gs[1].subgridspec(1, 12, wspace=0.05)
        n_samples = self._n_samples(self.loader_names[0])
        self._btn_sp = Button(self.fig.add_subplot(sample_gs[0, 3]), "Prev")
        self._btn_sn = Button(self.fig.add_subplot(sample_gs[0, 4]), "Next")
        self._tb_s = TextBox(
            ax=self.fig.add_subplot(sample_gs[0, 5]),
            label="",
            initial="",
        )
        self._sld_s = Slider(
            ax=self.fig.add_subplot(sample_gs[0, 6:9]),
            label="",
            valmin=0,
            valmax=max(n_samples - 1, 0),
            valinit=0,
            valstep=1,
            valfmt="%d",
        )

        if self._has_3d_flag:
            depth_gs = ctrl_gs[2].subgridspec(1, 12, wspace=0.05)
            max_d = self._max_depth(self.loader_names[0])
            self._btn_du = Button(self.fig.add_subplot(depth_gs[0, 3]), "Prev")
            self._btn_dd = Button(self.fig.add_subplot(depth_gs[0, 4]), "Next")
            self._tb_d = TextBox(
                ax=self.fig.add_subplot(depth_gs[0, 5]),
                label="",
                initial="",
            )
            self._sld_d = Slider(
                ax=self.fig.add_subplot(depth_gs[0, 6:9]),
                label="",
                valmin=0,
                valmax=max(max_d - 1, 0),
                valinit=0,
                valstep=1,
                valfmt="%d",
            )

        self._btn_lp.on_clicked(lambda _: self._chg_loader(-1))
        self._btn_ln.on_clicked(lambda _: self._chg_loader(1))
        self._btn_sp.on_clicked(lambda _: self._chg_sample(-1))
        self._btn_sn.on_clicked(lambda _: self._chg_sample(1))
        self._sld_s.on_changed(self._on_sld_s)
        self._tb_s.on_submit(self._on_tb_s)
        if self._has_3d_flag:
            self._btn_du.on_clicked(lambda _: self._chg_depth(-1))
            self._btn_dd.on_clicked(lambda _: self._chg_depth(1))
            self._sld_d.on_changed(self._on_sld_d)
            self._tb_d.on_submit(self._on_tb_d)

    def _sync_widgets(self) -> None:
        self._updating = True
        loader = self.loader_names[self.loader_idx]
        n = self._n_samples(loader)
        self._sld_s.valmax = max(n - 1, 0)
        self._sld_s.ax.set_xlim(self._sld_s.valmin, self._sld_s.valmax)
        self._sld_s.set_val(self.sample_idx)
        self._tb_s.set_val(str(self.sample_idx))
        if self._has_3d_flag:
            max_d = self._max_depth(loader)
            self._sld_d.valmax = max(max_d - 1, 0)
            self._sld_d.ax.set_xlim(self._sld_d.valmin, self._sld_d.valmax)
            self._sld_d.set_val(self.depth_idx)
            self._tb_d.set_val(str(self.depth_idx))
        self._updating = False

    def _chg_loader(self, d: int) -> None:
        self.loader_idx = (self.loader_idx + d) % len(self.loader_names)
        self.sample_idx = 0
        self.depth_idx = 0
        self._sync_widgets()
        self._update()

    def _chg_sample(self, d: int) -> None:
        n = self._n_samples(self.loader_names[self.loader_idx])
        self.sample_idx = max(0, min(self.sample_idx + d, n - 1))
        self._sync_widgets()
        self._update()

    def _on_sld_s(self, val: float) -> None:
        if self._updating:
            return
        self.sample_idx = int(val)
        self._updating = True
        self._tb_s.set_val(str(self.sample_idx))
        self._updating = False
        self._update()

    def _on_tb_s(self, text: str) -> None:
        if self._updating:
            return
        try:
            v = int(text)
        except ValueError:
            return
        n = self._n_samples(self.loader_names[self.loader_idx])
        self.sample_idx = max(0, min(v, n - 1))
        self._sync_widgets()
        self._update()

    def _chg_depth(self, d: int) -> None:
        max_d = self._max_depth(self.loader_names[self.loader_idx])
        self.depth_idx = max(0, min(self.depth_idx + d, max_d - 1))
        self._sync_widgets()
        self._update()

    def _on_sld_d(self, val: float) -> None:
        if self._updating:
            return
        self.depth_idx = int(val)
        self._updating = True
        self._tb_d.set_val(str(self.depth_idx))
        self._updating = False
        self._update()

    def _on_tb_d(self, text: str) -> None:
        if self._updating:
            return
        try:
            v = int(text)
        except ValueError:
            return
        max_d = self._max_depth(self.loader_names[self.loader_idx])
        self.depth_idx = max(0, min(v, max_d - 1))
        self._sync_widgets()
        self._update()

    def _show_tensor(
        self, col: int, row: int, ch_data: torch.Tensor,
        spatial_n_dims: int, depth_idx: int, title: str,
    ) -> None:
        ax = self._data_axes[col][row]
        ax.axis("on")
        ax.set_title(title, fontsize=8)
        if spatial_n_dims == 1:
            data = ch_data.numpy()
            ln = self._cell_lines[col][row]
            ln.set_data(np.arange(len(data)), data)
            ln.set_visible(True)
            ax.relim()
            ax.autoscale_view()
        else:
            if spatial_n_dims >= 3:
                d = min(depth_idx, ch_data.shape[0] - 1)
                ch_data = ch_data[d]
                if ch_data.ndim > 2:
                    ch_data = ch_data.reshape(ch_data.shape[0], -1)
            data = ch_data.numpy()
            im = self._cell_imgs[col][row]
            im.set_array(data)
            im.set_clim(data.min(), data.max())
            im.set_extent([0, data.shape[1], data.shape[0], 0])
            im.set_visible(True)
            _set_image_pixel_aspect(ax, data.shape[0], data.shape[1])

    def _show_text(self, col: int, row: int, text: str, mono: bool = False) -> None:
        ax = self._data_axes[col][row]
        ax.axis("on")
        ax.set_xticks([])
        ax.set_yticks([])
        t = self._cell_texts[col][row]
        t.set_text(text)
        t.set_visible(True)
        if mono:
            t.set_ha("left")
            t.set_fontfamily("monospace")
            t.set_position((0.05, 0.5))
        else:
            t.set_ha("center")
            t.set_fontfamily("sans-serif")
            t.set_position((0.5, 0.5))

    def _draw_column(self, col_idx: int, section: dict, sample_idx: int) -> None:
        items = list(section.items())
        non_tensors = [(k, v) for k, v in items if not torch.is_tensor(v)]
        tensors = [(k, v) for k, v in items if torch.is_tensor(v)]
        row = 0

        for key, val in non_tensors:
            if row >= len(self._data_axes[col_idx]):
                break
            sv = val[sample_idx] if sample_idx < len(val) else "N/A"
            self._show_text(col_idx, row, f"{key}: {sv}", mono=True)
            row += 1

        for key, val in tensors:
            if sample_idx >= val.shape[0]:
                continue
            sample = val[sample_idx]

            if sample.ndim == 0:
                if row >= len(self._data_axes[col_idx]):
                    break
                self._show_text(col_idx, row, f"{key}: {sample.item():.6g}")
                row += 1
                continue

            if sample.ndim == 1:
                for ch in range(sample.shape[0]):
                    if row >= len(self._data_axes[col_idx]):
                        break
                    lbl = f"{key}[{ch}]" if sample.shape[0] > 1 else key
                    self._show_text(col_idx, row, f"{lbl}: {sample[ch].item():.6g}")
                    row += 1
                continue

            n_channels = sample.shape[0]
            spatial_n_dims = sample.ndim - 1
            for ch in range(n_channels):
                if row >= len(self._data_axes[col_idx]):
                    break
                title = key if n_channels == 1 else f"{key} ch{ch}"
                self._show_tensor(
                    col_idx, row,
                    sample[ch], spatial_n_dims, self.depth_idx, title,
                )
                row += 1

    def _update(self) -> None:
        loader = self.loader_names[self.loader_idx]

        self._loader_text.set_text(f"Loader: {loader}")

        for c in range(len(self.columns)):
            for r in range(len(self._data_axes[c])):
                self._data_axes[c][r].axis("off")
                self._data_axes[c][r].set_title("")
                self._cell_imgs[c][r].set_visible(False)
                self._cell_lines[c][r].set_visible(False)
                self._cell_texts[c][r].set_visible(False)

        for c, (_, pt_idx, sec_key) in enumerate(self.columns):
            s_idx = self.sample_idx
            if pt_idx > 0:
                pt_name = self.data_list[pt_idx][0]
                mp = self.match_maps.get(pt_name, {}).get(loader, {})
                if s_idx not in mp:
                    self._show_text(c, 0, "No match")
                    continue
                s_idx = mp[s_idx]
            self._draw_column(c, self._sec(pt_idx, sec_key, loader), s_idx)

        if self._loss_text is not None:
            parts: List[str] = []
            gt_sec = self._sec(0, "gts", loader)
            for _, pt_idx, sk in self.columns:
                if sk != "outputs":
                    continue
                pt_name = self.data_list[pt_idx][0]
                si = self.sample_idx
                if pt_idx > 0:
                    mp = self.match_maps.get(pt_name, {}).get(loader, {})
                    if si not in mp:
                        continue
                    si = mp[si]
                out_sec = self._sec(pt_idx, "outputs", loader)
                s_out = {
                    k: v[si : si + 1]
                    for k, v in out_sec.items()
                    if torch.is_tensor(v)
                }
                s_gt = {
                    k: v[self.sample_idx : self.sample_idx + 1]
                    for k, v in gt_sec.items()
                    if torch.is_tensor(v)
                }
                prefix = pt_name if len(self.data_list) > 1 else ""
                for ln, lf in self.losses_dict.items():
                    tag = f"{prefix}/{ln}" if prefix else ln
                    try:
                        with torch.no_grad():
                            lv = lf(**s_out, **s_gt).item()
                        parts.append(f"{tag}={lv:.6g}")
                    except Exception:
                        parts.append(f"{tag}=err")
            self._loss_text.set_text("  |  ".join(parts) if parts else "")

        self.fig.canvas.draw_idle()

    def show(self) -> None:
        plt.show()


outs_path = "baseline/fno/ckpt/eval.pt"
check_outputs(outs_path)
