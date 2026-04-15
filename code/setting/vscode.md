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

    // vscode
    "files.autoSaveDelay": 10000,
    "editor.fontSize": 15,
    "editor.minimap.enabled": false,
    "workbench.sideBar.location": "right",
    "workbench.statusBar.visible": false,
    "workbench.startupEditor": "none",
    "workbench.browser.showInTitleBar": false,
    "workbench.navigationControl.enabled": false,
    "workbench.layoutControl.enabled": false,
    "workbench.activityBar.location": "hidden",
    "workbench.secondarySideBar.defaultVisibility": "hidden",
    "window.commandCenter": false,
    "window.restoreWindows": "none",
    "extensions.ignoreRecommendations": true,
    "security.workspace.trust.untrustedFiles": "open",
    "explorer.confirmPasteNative": false,
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "update.showReleaseNotes": false,
    "chat.tips.enabled": false,
    "chat.viewSessions.orientation": "stacked",
    
    // git
    "git.autofetch": true,

    // ssh
    "remote.SSH.lockfilesInTmp": true,
    "remote.SSH.remotePlatform": {
        "server1": "linux"
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
                "-outdir=%OUTDIR%",
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
    "latex-workshop.latex.recipe.default": "LaTeXmk",
    "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
    "latex-workshop.intellisense.argumentHint.enabled": false,
    "workbench.editorAssociations": {
        "*.pdf": "latex-workshop-pdf-hook"
    },

    // jupyter
    "jupyter.askForKernelRestart": false,
    
    // java
    "redhat.telemetry.enabled": false,
    
    // claude code
    "claudeCode.preferredLocation": "sidebar"
}
```

#### key-binding
```json
[
    {
        "key": "cmd+m",
        "command": "opensshremotes.openEmptyWindow"
    },
    {
        "key": "cmd+j",
        "command": "workbench.action.toggleSidebarVisibility"
    },
    {
        "key": "cmd+j",
        "command": "-workbench.action.togglePanel"
    },
    {
        "key": "cmd+n",
        "command": "workbench.action.togglePanel"
    },
    {
        "key": "cmd+b",
        "command": "-workbench.action.toggleSidebarVisibility"
    },
    {
        "key": "cmd+b",
        "command": "workbench.action.terminal.new",
        "when": "terminalProcessSupported || terminalWebExtensionContributedProfile"
    },
    {
        "key": "cmd+h",
        "command": "workbench.action.toggleAuxiliaryBar"
    },
    {
        "key": "alt+cmd+b",
        "command": "-workbench.action.toggleAuxiliaryBar"
    }
]
```