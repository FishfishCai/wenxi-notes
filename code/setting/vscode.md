---
id: d9v4q08wj8qy2zjf
title: vscode setting
tags: []
refs: []
backrefs: []
---
# Setting
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
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.showContextMenu": true,
    "latex-workshop.intellisense.package.enabled": true,
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk-xe",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-xelatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk-pdf",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk-lua",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-lualatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk (XeLaTeX)",
            "tools": ["latexmk-xe"]
        },
        {
            "name": "latexmk (pdfLaTeX)",
            "tools": ["latexmk-pdf"]
        },
        {
            "name": "latexmk (LuaLaTeX)",
            "tools": ["latexmk-lua"]
        }
    ],
    "latex-workshop.latex.recipe.default": "latexmk (XeLaTeX)",
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
        "*.log",
        "*.synctex(busy)",
        "*.nav",
        "*.snm",
        "*.vrb",
        "*.bcf",
        "*.run.xml",
        "*.xdv"
    ],
    "latex-workshop.latex.autoClean.run": "onBuilt",
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

# key-binding
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
```---
id: d9v4q08wj8qy2zjf
nota: true
title: vscode setting
tag: [setting]
coconote: true
---
# Setting
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
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.showContextMenu": true,
    "latex-workshop.intellisense.package.enabled": true,
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk-xe",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-xelatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk-pdf",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk-lua",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-lualatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk (XeLaTeX)",
            "tools": ["latexmk-xe"]
        },
        {
            "name": "latexmk (pdfLaTeX)",
            "tools": ["latexmk-pdf"]
        },
        {
            "name": "latexmk (LuaLaTeX)",
            "tools": ["latexmk-lua"]
        }
    ],
    "latex-workshop.latex.recipe.default": "latexmk (XeLaTeX)",
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
        "*.log",
        "*.synctex(busy)",
        "*.nav",
        "*.snm",
        "*.vrb",
        "*.bcf",
        "*.run.xml",
        "*.xdv"
    ],
    "latex-workshop.latex.autoClean.run": "onBuilt",
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
