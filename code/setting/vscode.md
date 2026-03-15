#### Setting
```json
{
    // terminal
    "terminal.integrated.defaultProfile.osx": "fish",
    "terminal.integrated.inheritEnv": false,
    "terminal.integrated.scrollback": 1000000,
    "terminal.integrated.profiles.osx": {
        "zsh": {
            "path": "/bin/zsh",
            "args": ["-l"]
        },
        "fish": {
            "path": "/opt/homebrew/bin/fish",
            "args": ["-l"]
        }
    },
    
    // latex
    "latex-workshop.latex.autoBuild.run": "onFileChange",
    "latex-workshop.showContextMenu": true,
    "latex-workshop.intellisense.package.enabled": true,
    "latex-workshop.message.error.show": false,
    "latex-workshop.message.warning.show": false,
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        },
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-interaction=nonstopmode",
                "-file-line-error",
                "outdir=%OUTDIR%",
                "-pdf",
                "%DOCFILE%"
            ]
        },
        {
            "name": "biber",
            "command": "biber",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "XeLaTeX",
            "tools": [
                "xelatex"
            ]
        },
        {
            "name": "PDFLaTeX",
            "tools": [
                "pdflatex"
            ]
        },
        {
            "name": "BibTeX",
            "tools": [
                "bibtex"
            ]
        },
        {
            "name": "LaTeXmk",
            "tools": [
                "latexmk"
            ]
        },
        {
            "name": "xelatex -> bibtex -> xelatex*2",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "pdflatex -> biber -> pdflatex*2",
            "tools": [
                "pdflatex",
                "biber",
                "pdflatex",
                "pdflatex"
            ]
        }
    ],
    "latex-workshop.latex.clean.fileTypes": [
        "*.fdb_latexmk",
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log"
    ],
    "latex-workshop.latex.autoClean.run": "onBuilt",
    "latex-workshop.latex.recipe.default": "xelatex",
    "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
    "latex-workshop.intellisense.argumentHint.enabled": false,

    // vscode
    "files.autoSaveDelay": 10000,
    "editor.fontSize": 15,
    "editor.minimap.enabled": false,
    "workbench.sideBar.location": "right",
    "workbench.statusBar.visible": false,
    "workbench.startupEditor": "none",
    "extensions.ignoreRecommendations": true,
    "security.workspace.trust.untrustedFiles": "open",
    "window.restoreWindows": "none",
    "explorer.confirmPasteNative": false,
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "update.showReleaseNotes": false,

    // jupyter
    "jupyter.askForKernelRestart": false,
    
    // copilot
    "github.copilot.nextEditSuggestions.enabled": true,

    // ssh
    "remote.SSH.lockfilesInTmp": true,
    
    // git
    "git.autofetch": true,
}
```
