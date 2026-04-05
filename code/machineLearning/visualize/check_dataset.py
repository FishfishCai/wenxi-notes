from pathlib import Path
from typing import Any, List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, TextBox
import torch


def _set_image_pixel_aspect(ax: Any, height: int, width: int) -> None:
    if width > 0 and height > 0:
        ax.set_box_aspect(height / width)


def check_dataset(data_path: str | Path) -> None:
    p = Path(data_path).expanduser().resolve()
    suffix = p.suffix.lower()
    if suffix == ".npy":
        arr = np.load(p.as_posix(), mmap_mode="r")
    elif suffix == ".pt":
        obj = torch.load(p, map_location="cpu", weights_only=False)
        arr = obj.numpy() if isinstance(obj, torch.Tensor) else np.asarray(obj)
    else:
        raise ValueError(f"Unsupported file format '{suffix}', expected .npy or .pt")
    if arr.ndim < 3:
        raise ValueError(f"Expected at least 3D array (N, C, *spatial), got shape {arr.shape}")
    _Viewer(arr, p.name).show()


class _Viewer:
    def __init__(self, arr: np.ndarray, name: str) -> None:
        self.arr = arr
        self.name = name
        self.n_samples = arr.shape[0]
        self.n_channels = arr.shape[1]
        self.spatial_shape = arr.shape[2:]
        self.spatial_ndim = len(self.spatial_shape)
        self.sample_idx = 0
        self.depth_idx = 0
        self._updating = False
        self._has_depth = self.spatial_ndim >= 3
        self._build_figure()
        self._update()

    def _build_figure(self) -> None:
        n_cols = self.n_channels
        n_ctrl_rows = 1 + int(self._has_depth)

        fig_width = min(max(5.5 * n_cols, 10), 36)
        fig_height = min(max(5.2 + n_ctrl_rows * 0.55, 7.5), 28)
        self.fig = plt.figure(figsize=(fig_width, fig_height))

        outer = self.fig.add_gridspec(
            2, 1, height_ratios=[12, n_ctrl_rows], hspace=0.1,
        )

        row_ratios = [0.08, 1]
        data_gs = outer[0].subgridspec(
            2, n_cols, height_ratios=row_ratios, hspace=0.04, wspace=0.25,
        )
        self._header_axes: List[Any] = []
        for c in range(n_cols):
            ax = self.fig.add_subplot(data_gs[0, c])
            ax.axis("off")
            self._header_axes.append(ax)

        self._data_axes: List[Any] = []
        for c in range(n_cols):
            ax = self.fig.add_subplot(data_gs[1, c])
            ax.axis("off")
            self._data_axes.append(ax)

        self._title_texts: List[Any] = []
        self._artists: List[Any] = []
        for ch in range(self.n_channels):
            hdr = self._header_axes[ch]
            title = f"ch{ch}" if self.n_channels > 1 else self.name
            self._title_texts.append(hdr.text(
                0.5, 0.5, title,
                ha="center", va="center", fontsize=11, fontweight="bold",
                transform=hdr.transAxes,
            ))
            ax = self._data_axes[ch]
            ax.axis("on")
            if self.spatial_ndim == 1:
                line, = ax.plot([], [])
                self._artists.append(line)
            else:
                if self.spatial_ndim == 2:
                    h, w = int(self.spatial_shape[0]), int(self.spatial_shape[1])
                else:
                    h, w = int(self.spatial_shape[1]), int(self.spatial_shape[2])
                im = ax.imshow(
                    np.zeros((h, w)),
                    aspect="equal",
                    interpolation="nearest",
                    cmap="viridis",
                )
                _set_image_pixel_aspect(ax, h, w)
                self._artists.append(im)

        ctrl_gs = outer[1].subgridspec(n_ctrl_rows, 1, hspace=0.35)

        sample_gs = ctrl_gs[0].subgridspec(1, 12, wspace=0.05)
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
            valmax=max(self.n_samples - 1, 0),
            valinit=0,
            valstep=1,
            valfmt="%d",
        )

        if self._has_depth:
            depth_gs = ctrl_gs[1].subgridspec(1, 12, wspace=0.05)
            max_d = self.spatial_shape[0]
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

        self._btn_sp.on_clicked(lambda _: self._chg_sample(-1))
        self._btn_sn.on_clicked(lambda _: self._chg_sample(1))
        self._sld_s.on_changed(self._on_sld_s)
        self._tb_s.on_submit(self._on_tb_s)
        if self._has_depth:
            self._btn_du.on_clicked(lambda _: self._chg_depth(-1))
            self._btn_dd.on_clicked(lambda _: self._chg_depth(1))
            self._sld_d.on_changed(self._on_sld_d)
            self._tb_d.on_submit(self._on_tb_d)

    def _sync_widgets(self) -> None:
        self._updating = True
        self._sld_s.valmax = max(self.n_samples - 1, 0)
        self._sld_s.ax.set_xlim(self._sld_s.valmin, self._sld_s.valmax)
        self._sld_s.set_val(self.sample_idx)
        self._tb_s.set_val(str(self.sample_idx))
        if self._has_depth:
            max_d = self.spatial_shape[0]
            self._sld_d.valmax = max(max_d - 1, 0)
            self._sld_d.ax.set_xlim(self._sld_d.valmin, self._sld_d.valmax)
            self._sld_d.set_val(self.depth_idx)
            self._tb_d.set_val(str(self.depth_idx))
        self._updating = False

    def _chg_sample(self, d: int) -> None:
        self.sample_idx = max(0, min(self.sample_idx + d, self.n_samples - 1))
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
        self.sample_idx = max(0, min(v, self.n_samples - 1))
        self._sync_widgets()
        self._update()

    def _chg_depth(self, d: int) -> None:
        max_d = self.spatial_shape[0]
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
        max_d = self.spatial_shape[0]
        self.depth_idx = max(0, min(v, max_d - 1))
        self._sync_widgets()
        self._update()

    def _update(self) -> None:
        sample = np.asarray(self.arr[self.sample_idx])
        for ch in range(self.n_channels):
            ch_data = sample[ch]
            if self.spatial_ndim == 1:
                self._artists[ch].set_data(np.arange(len(ch_data)), ch_data)
                self._data_axes[ch].relim()
                self._data_axes[ch].autoscale_view()
            elif self.spatial_ndim == 2:
                self._artists[ch].set_array(ch_data)
                self._artists[ch].set_clim(ch_data.min(), ch_data.max())
                self._artists[ch].set_extent(
                    [0, ch_data.shape[1], ch_data.shape[0], 0]
                )
                _set_image_pixel_aspect(
                    self._data_axes[ch], ch_data.shape[0], ch_data.shape[1],
                )
            else:
                d = min(self.depth_idx, ch_data.shape[0] - 1)
                img = ch_data[d]
                if img.ndim > 2:
                    img = img.reshape(img.shape[0], -1)
                self._artists[ch].set_array(img)
                self._artists[ch].set_clim(img.min(), img.max())
                self._artists[ch].set_extent(
                    [0, img.shape[1], img.shape[0], 0]
                )
                _set_image_pixel_aspect(
                    self._data_axes[ch], img.shape[0], img.shape[1],
                )
        self.fig.canvas.draw_idle()

    def show(self) -> None:
        plt.show()


data_path = Path("./data/test_kolmogorov2d.npy")
check_dataset(data_path)
