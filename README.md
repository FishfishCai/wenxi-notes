# Wenxi Notes

Public Obsidian notes written by Wenxi Cai.

An Obsidian vault of mathematics notes on analysis, topology, linear algebra, and optimization, with the textbooks they follow, paper collections for ongoing research, shared training code, and personal tool configurations.

## Repository structure

```
infra/      shared training code: base model, config loader, metric interface, trainer
note/       mathematics notes, one file per subject
research/   papers and reading notes, one folder per research topic
setting/    configurations for Latex Suite, SSH, VPN, and VS Code
textbook/   textbooks the notes follow
.obsidian/  vault settings, Catppuccin theme, and plugins
```

## Requirements

Obsidian ≥ 1.13.0. The code in `infra/` needs Python with `torch` and `accelerate`.

## Usage

Clone the repository and open the folder as a vault in Obsidian. The theme, plugins, and their settings load from `.obsidian/`; turn on community plugins when Obsidian asks.

## Plugins

- [Math Block](https://github.com/FishfishCai/obsidian-math-block): mathematical blocks with `:::` syntax, shared numbering, native block links, and `\ref` completion. Written by the author of this vault.
- Editor Width Slider: adjust the editor line width with a slider.
- File Explorer Note Count: show the number of notes in each folder of the file explorer.
- Lapel: mark heading levels in the editor gutter.
- Latex Suite: snippets and shortcuts for fast LaTeX input; the snippets used here are in `setting/latexSuite.md`.
- Live Background: video wallpaper behind the workspace.
- Style Settings: adjust theme and plugin CSS variables from a settings panel.
