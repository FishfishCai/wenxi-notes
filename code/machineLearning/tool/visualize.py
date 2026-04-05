from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, TextBox
import torch
from torch import nn


def check_outputs(
    paths: Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]],
    losses: Optional[Union[nn.Module, Dict[str, nn.Module]]] = None,
    show_input: bool = True,
) -> None:
    """Load ``.pt`` evaluation files and launch an interactive matplotlib viewer.

    Parameters
    ----------
    paths : Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]]
        One or more paths to ``.pt`` files saved by ``Trainer.evaluate``.
        A dict maps display names to paths; a list auto-names them
        ``pt_0``, ``pt_1``, etc.  A single path is also accepted.
    losses : Optional[Union[nn.Module, Dict[str, nn.Module]]]
        Optional loss functions ``loss(**outputs, **gts)`` computed per sample.
        A single module is wrapped as ``{"loss": module}``.  Default is ``None``.
    show_input : bool
        Whether to display the input column.  Default is ``True``.

    Returns
    -------
    None
    """
    paths_dict = _normalize_paths(paths)
    losses_dict = _normalize_losses(losses)

    data_list: List[Tuple[str, dict]] = []
    for name, p in paths_dict.items():
        data_list.append(
            (name, torch.load(p, map_location="cpu", weights_only=False))
        )

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

    match_maps = _build_match_maps(
        data_list=data_list,
        loader_names=loader_names,
        has_inputs=has_inputs,
        has_gts=has_gts,
    )

    _Viewer(
        data_list=data_list,
        loader_names=loader_names,
        match_maps=match_maps,
        has_inputs=has_inputs,
        has_outputs=has_outputs,
        has_gts=has_gts,
        losses_dict=losses_dict,
        show_input=show_input,
    ).show()


def _normalize_paths(
    paths: Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]],
) -> OrderedDict:
    """Normalize heterogeneous path input into an ordered name-to-path mapping.

    Parameters
    ----------
    paths : Union[str, Path, List[Union[str, Path]], Dict[str, Union[str, Path]]]
        Single path, list of paths, or ``{name: path}`` dict.

    Returns
    -------
    paths_dict : OrderedDict[str, Path]
        Ordered mapping from display name to resolved ``Path``.
    """
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
    """Normalize loss input into a name-to-module dict.

    Parameters
    ----------
    losses : Optional[Union[nn.Module, Dict[str, nn.Module]]]
        Single loss module, ``{name: module}`` dict, or ``None``.

    Returns
    -------
    losses_dict : Dict[str, nn.Module]
        Named loss modules; empty dict when *losses* is ``None``.
    """
    if losses is None:
        return {}
    if isinstance(losses, nn.Module):
        return {"loss": losses}
    if isinstance(losses, dict):
        return dict(losses)
    raise TypeError(f"losses must be nn.Module, dict, or None; got {type(losses)}")

def _section_sample_count(
    section: dict,
) -> int:
    """Return the number of samples in a single section dict.

    Parameters
    ----------
    section : dict
        Mapping from key names to tensors or lists.

    Returns
    -------
    n_samples : int
        Batch size of the first tensor or length of the first list; 0 if empty.
    """
    for v in section.values():
        if torch.is_tensor(v):
            return v.shape[0]
        if isinstance(v, (list, tuple)):
            return len(v)
    return 0

def _sample_count(
    data: dict,
    loader: str,
) -> int:
    """Return the number of samples for a loader across all sections.

    Parameters
    ----------
    data : dict
        Top-level loaded ``.pt`` dict with optional ``inputs``, ``outputs``, ``gts``.
    loader : str
        Loader name to look up.

    Returns
    -------
    n_samples : int
        Sample count from the first non-empty section; 0 if none found.
    """
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
    """Build per-pt, per-loader index mappings from the reference pt to each subsequent pt.

    Matching compares all shared tensor keys with ``torch.equal``.
    Falls back to positional indexing when no tensor keys are available.

    Parameters
    ----------
    data_list : List[Tuple[str, dict]]
        ``(name, loaded_dict)`` pairs; the first entry is the reference.
    loader_names : List[str]
        Loader names to build mappings for.
    has_inputs : bool
        Whether the reference pt contains ``"inputs"``.
    has_gts : bool
        Whether the reference pt contains ``"gts"``.

    Returns
    -------
    maps : Dict[str, Dict[str, Dict[int, int]]]
        ``maps[pt_name][loader_name]`` maps reference sample index to the
        matched index in the other pt.  Empty dict when only one pt is given.
    """
    if len(data_list) <= 1:
        return {}

    match_sec = "inputs" if has_inputs else ("gts" if has_gts else None)
    ref = data_list[0][1]
    maps: Dict[str, Dict[str, Dict[int, int]]] = {}

    for name, data in data_list[1:]:
        maps[name] = {}
        for loader in loader_names:
            # No matchable section -- fall back to positional
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
            # No tensor keys to compare -- fall back to positional
            if not tensor_keys:
                n = min(
                    _section_sample_count(ref_sec),
                    _section_sample_count(oth_sec),
                )
                maps[name][loader] = {i: i for i in range(n)}
                continue

            # Exact matching via torch.equal on all tensor keys
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
    """Interactive matplotlib figure for browsing evaluation data."""

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
        """Initialize viewer state, build the figure, and draw the first frame.

        Parameters
        ----------
        data_list : List[Tuple[str, dict]]
            ``(name, loaded_dict)`` pairs.
        loader_names : List[str]
            Available loader names from the reference pt.
        match_maps : Dict[str, Dict[str, Dict[int, int]]]
            Sample index mappings produced by :func:`_build_match_maps`.
        has_inputs : bool
            Whether the reference pt contains ``"inputs"``.
        has_outputs : bool
            Whether the reference pt contains ``"outputs"``.
        has_gts : bool
            Whether the reference pt contains ``"gts"``.
        losses_dict : Dict[str, nn.Module]
            Named loss functions for per-sample evaluation.
        show_input : bool
            Whether to display the input column.

        Returns
        -------
        None
        """
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

        ## Determine active display columns
        self._init_columns()
        ## Create figure, axes, and widgets
        self._build_figure()
        ## Initial render
        self._update()

    # -- column helpers -----------------------------------------------------

    def _init_columns(
        self,
    ) -> None:
        """Populate ``self.columns`` with ``(label, pt_idx, section_key)`` tuples.

        Returns
        -------
        None
        """
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

    def _sec(
        self,
        pt_idx: int,
        key: str,
        loader: str,
    ) -> dict:
        """Retrieve the section dict for a given pt, section key, and loader.

        Parameters
        ----------
        pt_idx : int
            Index into ``self.data_list``.
        key : str
            Section key: ``"inputs"``, ``"outputs"``, or ``"gts"``.
        loader : str
            Loader name.

        Returns
        -------
        section : dict
            Key-to-value mapping; empty dict if the path does not exist.
        """
        return self.data_list[pt_idx][1].get(key, {}).get(loader, {})

    def _n_samples(
        self,
        loader: str,
    ) -> int:
        """Return the number of samples in the reference pt for *loader*.

        Parameters
        ----------
        loader : str
            Loader name.

        Returns
        -------
        n_samples : int
            Sample count.
        """
        return _sample_count(self.data_list[0][1], loader)

    # -- layout metrics -----------------------------------------------------

    def _visual_rows_for(
        self,
        section: dict,
    ) -> int:
        """Count the number of visual subplot rows required by *section*.

        Each non-tensor key uses one row; each tensor key uses one row per channel.

        Parameters
        ----------
        section : dict
            Key-to-value mapping for a single section and loader.

        Returns
        -------
        n_rows : int
            Total visual rows.
        """
        r = 0
        for v in section.values():
            if torch.is_tensor(v):
                r += v.shape[1] if v.ndim >= 2 else 1
            else:
                r += 1
        return r

    def _max_visual_rows(
        self,
    ) -> int:
        """Return the maximum visual-row count across all loaders and columns.

        Returns
        -------
        n_rows : int
            At least 1.
        """
        mx = 0
        for loader in self.loader_names:
            for _, pi, sk in self.columns:
                mx = max(mx, self._visual_rows_for(self._sec(pi, sk, loader)))
        return max(mx, 1)

    def _any_3d(
        self,
    ) -> bool:
        """Check whether any tensor across all loaders has 3-D spatial data (ndim == 5).

        Returns
        -------
        flag : bool
            ``True`` if depth controls are needed.
        """
        for loader in self.loader_names:
            for _, pi, sk in self.columns:
                for v in self._sec(pi, sk, loader).values():
                    if torch.is_tensor(v) and v.ndim == 5:
                        return True
        return False

    def _max_depth(
        self,
        loader: str,
    ) -> int:
        """Return the maximum depth dimension across all 3-D tensors for *loader*.

        Parameters
        ----------
        loader : str
            Loader name.

        Returns
        -------
        max_depth : int
            At least 1.
        """
        d = 1
        for _, pi, sk in self.columns:
            for v in self._sec(pi, sk, loader).values():
                if torch.is_tensor(v) and v.ndim == 5:
                    d = max(d, v.shape[2])
        return d

    # -- figure construction ------------------------------------------------

    def _build_figure(
        self,
    ) -> None:
        """Create the matplotlib figure, axes grid, loss area, and control widgets.

        Returns
        -------
        None
        """
        n_cols = len(self.columns)
        max_rows = self._max_visual_rows()
        self._has_3d_flag = self._any_3d()
        has_loss = bool(self.losses_dict) and self.has_gts and self.has_outputs
        n_ctrl_rows = 2 + int(self._has_3d_flag)

        fig_width = min(max(3.5 * n_cols, 8), 28)
        fig_height = min(
            max(
                (max_rows + 1) * 1.8 + n_ctrl_rows * 0.7 + (0.6 if has_loss else 0),
                6,
            ),
            18,
        )
        self.fig = plt.figure(figsize=(fig_width, fig_height))

        ratios = [(max_rows + 1) * 3]
        if has_loss:
            ratios.append(1)
        ratios.append(n_ctrl_rows)
        outer = self.fig.add_gridspec(
            len(ratios), 1, height_ratios=ratios, hspace=0.35,
        )

        ## Data grid (row 0 = header, rows 1.. = data)
        data_gs = outer[0].subgridspec(
            max_rows + 1, n_cols, hspace=0.55, wspace=0.35,
        )
        self._header_axes: List[Any] = []
        for c in range(n_cols):
            ax = self.fig.add_subplot(data_gs[0, c])
            ax.axis("off")
            self._header_axes.append(ax)

        self._data_axes: List[List[Any]] = []
        for c in range(n_cols):
            col_axes = []
            for r in range(max_rows):
                ax = self.fig.add_subplot(data_gs[r + 1, c])
                ax.axis("off")
                col_axes.append(ax)
            self._data_axes.append(col_axes)

        ## Loss area
        grid_idx = 1
        if has_loss:
            self._loss_ax = self.fig.add_subplot(outer[grid_idx])
            self._loss_ax.axis("off")
            grid_idx += 1
        else:
            self._loss_ax = None

        ## Control panel
        ctrl_gs = outer[grid_idx].subgridspec(n_ctrl_rows, 1, hspace=0.7)

        ## Loader row
        loader_gs = ctrl_gs[0].subgridspec(1, 5, wspace=0.05)
        self._btn_lp = Button(self.fig.add_subplot(loader_gs[0, 0]), "\u25C0")
        self._loader_ax = self.fig.add_subplot(loader_gs[0, 1:4])
        self._loader_ax.axis("off")
        self._btn_ln = Button(self.fig.add_subplot(loader_gs[0, 4]), "\u25B6")

        ## Sample row
        sample_gs = ctrl_gs[1].subgridspec(1, 10, wspace=0.05)
        n_samples = self._n_samples(self.loader_names[0])
        self._btn_sp = Button(self.fig.add_subplot(sample_gs[0, 0]), "\u25C0")
        self._sld_s = Slider(
            ax=self.fig.add_subplot(sample_gs[0, 1:8]),
            label="Sample",
            valmin=0,
            valmax=max(n_samples - 1, 0),
            valinit=0,
            valstep=1,
            valfmt="%d",
        )
        self._btn_sn = Button(self.fig.add_subplot(sample_gs[0, 8]), "\u25B6")
        self._tb_s = TextBox(
            ax=self.fig.add_subplot(sample_gs[0, 9]),
            label="",
            initial="0",
        )

        ## Depth row (only when 3-D spatial data exists)
        if self._has_3d_flag:
            depth_gs = ctrl_gs[2].subgridspec(1, 10, wspace=0.05)
            max_d = self._max_depth(self.loader_names[0])
            self._btn_du = Button(self.fig.add_subplot(depth_gs[0, 0]), "\u25B2")
            self._sld_d = Slider(
                ax=self.fig.add_subplot(depth_gs[0, 1:8]),
                label="Depth",
                valmin=0,
                valmax=max(max_d - 1, 0),
                valinit=0,
                valstep=1,
                valfmt="%d",
            )
            self._btn_dd = Button(self.fig.add_subplot(depth_gs[0, 8]), "\u25BC")
            self._tb_d = TextBox(
                ax=self.fig.add_subplot(depth_gs[0, 9]),
                label="",
                initial="0",
            )

        ## Wire callbacks
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

    # -- widget callbacks ---------------------------------------------------

    def _sync_widgets(
        self,
    ) -> None:
        """Synchronize slider and text-box values to the current state indices.

        Returns
        -------
        None
        """
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

    def _chg_loader(
        self,
        d: int,
    ) -> None:
        """Advance the loader index by *d*, reset sample and depth, then redraw.

        Parameters
        ----------
        d : int
            Step direction (+1 forward, -1 backward).

        Returns
        -------
        None
        """
        self.loader_idx = (self.loader_idx + d) % len(self.loader_names)
        self.sample_idx = 0
        self.depth_idx = 0
        self._sync_widgets()
        self._update()

    def _chg_sample(
        self,
        d: int,
    ) -> None:
        """Advance the sample index by *d*, clamped to valid range, then redraw.

        Parameters
        ----------
        d : int
            Step direction.

        Returns
        -------
        None
        """
        n = self._n_samples(self.loader_names[self.loader_idx])
        self.sample_idx = max(0, min(self.sample_idx + d, n - 1))
        self._sync_widgets()
        self._update()

    def _on_sld_s(
        self,
        val: float,
    ) -> None:
        """Callback for the sample slider ``on_changed`` event.

        Parameters
        ----------
        val : float
            New slider value.

        Returns
        -------
        None
        """
        if self._updating:
            return
        self.sample_idx = int(val)
        self._updating = True
        self._tb_s.set_val(str(self.sample_idx))
        self._updating = False
        self._update()

    def _on_tb_s(
        self,
        text: str,
    ) -> None:
        """Callback for the sample text-box ``on_submit`` event.

        Parameters
        ----------
        text : str
            Submitted text.

        Returns
        -------
        None
        """
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

    def _chg_depth(
        self,
        d: int,
    ) -> None:
        """Advance the depth index by *d*, clamped to valid range, then redraw.

        Parameters
        ----------
        d : int
            Step direction.

        Returns
        -------
        None
        """
        max_d = self._max_depth(self.loader_names[self.loader_idx])
        self.depth_idx = max(0, min(self.depth_idx + d, max_d - 1))
        self._sync_widgets()
        self._update()

    def _on_sld_d(
        self,
        val: float,
    ) -> None:
        """Callback for the depth slider ``on_changed`` event.

        Parameters
        ----------
        val : float
            New slider value.

        Returns
        -------
        None
        """
        if self._updating:
            return
        self.depth_idx = int(val)
        self._updating = True
        self._tb_d.set_val(str(self.depth_idx))
        self._updating = False
        self._update()

    def _on_tb_d(
        self,
        text: str,
    ) -> None:
        """Callback for the depth text-box ``on_submit`` event.

        Parameters
        ----------
        text : str
            Submitted text.

        Returns
        -------
        None
        """
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

    # -- rendering ----------------------------------------------------------

    @staticmethod
    def _render_tensor_cell(
        ax: Any,
        ch_data: torch.Tensor,
        spatial_n_dims: int,
        depth_idx: int,
        title: str,
    ) -> None:
        """Render a single-channel tensor slice into an axis.

        Dispatches to line plot (1-D), image (2-D), or depth-sliced image (>=3-D).

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Target axis.
        ch_data : torch.Tensor
            Single-channel spatial data with shape ``(*spatial)``.
        spatial_n_dims : int
            Number of spatial dimensions (0, 1, 2, or >=3).
        depth_idx : int
            Depth slice index used when ``spatial_n_dims >= 3``.
        title : str
            Axis title or text label.

        Returns
        -------
        None
        """
        ax.axis("on")
        if spatial_n_dims == 0:
            ax.set_xticks([])
            ax.set_yticks([])
            ax.text(
                0.5, 0.5, f"{title}: {ch_data.item():.6g}",
                ha="center", va="center", fontsize=9,
                transform=ax.transAxes,
            )
        elif spatial_n_dims == 1:
            ax.plot(ch_data.numpy())
            ax.set_title(title, fontsize=8)
        elif spatial_n_dims == 2:
            ax.imshow(ch_data.numpy(), aspect="auto", cmap="viridis")
            ax.set_title(title, fontsize=8)
        else:
            d = min(depth_idx, ch_data.shape[0] - 1)
            img = ch_data[d]
            if img.ndim > 2:
                img = img.reshape(img.shape[0], -1)
            ax.imshow(img.numpy(), aspect="auto", cmap="viridis")
            ax.set_title(f"{title} d={d}", fontsize=8)

    def _draw_column(
        self,
        col_idx: int,
        section: dict,
        sample_idx: int,
    ) -> None:
        """Fill a display column with non-tensor text and tensor plots for one sample.

        Non-tensor keys are rendered as text above tensor keys.  Tensor keys
        are rendered with one subplot row per channel.

        Parameters
        ----------
        col_idx : int
            Column index in ``self._data_axes``.
        section : dict
            Key-to-value mapping for the target section and loader.
        sample_idx : int
            Sample index into each value.

        Returns
        -------
        None
        """
        items = list(section.items())
        non_tensors = [(k, v) for k, v in items if not torch.is_tensor(v)]
        tensors = [(k, v) for k, v in items if torch.is_tensor(v)]

        row = 0

        # Non-tensor keys as text
        for key, val in non_tensors:
            if row >= len(self._data_axes[col_idx]):
                break
            ax = self._data_axes[col_idx][row]
            ax.axis("on")
            ax.set_xticks([])
            ax.set_yticks([])
            sv = val[sample_idx] if sample_idx < len(val) else "N/A"
            ax.text(
                0.05, 0.5, f"{key}: {sv}",
                ha="left", va="center", fontsize=9, family="monospace",
                transform=ax.transAxes,
            )
            row += 1

        # Tensor keys as plots
        for key, val in tensors:
            if sample_idx >= val.shape[0]:
                continue
            sample = val[sample_idx]

            # Scalar tensor
            if sample.ndim == 0:
                if row >= len(self._data_axes[col_idx]):
                    break
                ax = self._data_axes[col_idx][row]
                ax.axis("on")
                ax.set_xticks([])
                ax.set_yticks([])
                ax.text(
                    0.5, 0.5, f"{key}: {sample.item():.6g}",
                    ha="center", va="center", fontsize=9,
                    transform=ax.transAxes,
                )
                row += 1
                continue

            # 1-D tensor: (C,) -- scalar per channel
            if sample.ndim == 1:
                for ch in range(sample.shape[0]):
                    if row >= len(self._data_axes[col_idx]):
                        break
                    ax = self._data_axes[col_idx][row]
                    ax.axis("on")
                    ax.set_xticks([])
                    ax.set_yticks([])
                    lbl = f"{key}[{ch}]" if sample.shape[0] > 1 else key
                    ax.text(
                        0.5, 0.5, f"{lbl}: {sample[ch].item():.6g}",
                        ha="center", va="center", fontsize=9,
                        transform=ax.transAxes,
                    )
                    row += 1
                continue

            # ndim >= 2: (C, *spatial)
            n_channels = sample.shape[0]
            spatial_n_dims = sample.ndim - 1
            for ch in range(n_channels):
                if row >= len(self._data_axes[col_idx]):
                    break
                title = key if n_channels == 1 else f"{key} ch{ch}"
                self._render_tensor_cell(
                    self._data_axes[col_idx][row],
                    sample[ch], spatial_n_dims, self.depth_idx, title,
                )
                row += 1

    def _update(
        self,
    ) -> None:
        """Clear and redraw all data axes, loss text, and the loader label.

        Returns
        -------
        None
        """
        loader = self.loader_names[self.loader_idx]
        n = self._n_samples(loader)

        # Loader label
        self._loader_ax.clear()
        self._loader_ax.axis("off")
        self._loader_ax.text(
            0.5, 0.5,
            f"Loader: {loader}  ({self.sample_idx}/{max(n - 1, 0)})",
            ha="center", va="center", fontsize=11, fontweight="bold",
            transform=self._loader_ax.transAxes,
        )

        # Column headers
        for c, (label, _, _) in enumerate(self.columns):
            ax = self._header_axes[c]
            ax.clear()
            ax.axis("off")
            ax.text(
                0.5, 0.5, label,
                ha="center", va="center", fontsize=11, fontweight="bold",
                transform=ax.transAxes,
            )

        # Clear data axes
        for col in self._data_axes:
            for ax in col:
                ax.clear()
                ax.axis("off")

        # Draw each column
        for c, (_, pt_idx, sec_key) in enumerate(self.columns):
            s_idx = self.sample_idx

            # Apply sample matching for non-reference pts
            if pt_idx > 0:
                pt_name = self.data_list[pt_idx][0]
                mp = self.match_maps.get(pt_name, {}).get(loader, {})
                if s_idx not in mp:
                    ax = self._data_axes[c][0]
                    ax.axis("on")
                    ax.set_xticks([])
                    ax.set_yticks([])
                    ax.text(
                        0.5, 0.5, "No match",
                        ha="center", va="center", fontsize=10, color="gray",
                        transform=ax.transAxes,
                    )
                    continue
                s_idx = mp[s_idx]

            section = self._sec(pt_idx, sec_key, loader)
            self._draw_column(c, section, s_idx)

        # Losses
        if self._loss_ax is not None:
            self._loss_ax.clear()
            self._loss_ax.axis("off")
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

            if parts:
                self._loss_ax.text(
                    0.5, 0.5, "  |  ".join(parts),
                    ha="center", va="center", fontsize=10,
                    transform=self._loss_ax.transAxes,
                )

        self.fig.canvas.draw_idle()

    # -- public -------------------------------------------------------------

    def show(
        self,
    ) -> None:
        """Display the interactive figure via ``plt.show()``.

        Returns
        -------
        None
        """
        plt.show()
