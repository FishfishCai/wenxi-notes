### kitty
#### Catppuccin-Mocha.conf
```
# vim:ft=kitty

## name: Catppuccin-Mocha
## author: Pocco81 (https://github.com/Pocco81)
## license: MIT
## upstream: https://github.com/catppuccin/kitty/blob/main/mocha.conf
## blurb: Soothing pastel theme for the high-spirited!

# The basic colors
foreground #CDD6F4
background #1E1E2E
selection_foreground #1E1E2E
selection_background #F5E0DC

# Cursor colors
cursor #D8DEE9
cursor_text_color #1E1E2E

# URL underline color when hovering with mouse
url_color #74C7EC

# Kitty window border colors
active_border_color #B4BEFE
inactive_border_color #6C7086
bell_border_color #F9E2AF

# OS Window titlebar colors
wayland_titlebar_color system
macos_titlebar_color system

# Tab bar colors
active_tab_foreground #11111B
active_tab_background #CBA6F7
inactive_tab_foreground #CDD6F4
inactive_tab_background #181825
tab_bar_background #11111B

# Colors for marks (marked text in the terminal)
mark1_foreground #1E1E2E
mark1_background #B4BEFE
mark2_foreground #1E1E2E
mark2_background #CBA6F7
mark3_foreground #1E1E2E
mark3_background #74C7EC

# The 16 terminal colors

# black
color0 #45475A
color8 #585B70

# red
color1 #F38BA8
color9 #F38BA8

# green
color2 #A6E3A1
color10 #A6E3A1

# yellow
color3 #F9E2AF
color11 #F9E2AF

# blue
color4 #89B4FA
color12 #89B4FA

# magenta
color5 #F5C2E7
color13 #F5C2E7

# cyan
color6 #94E2D5
color14 #94E2D5

# white
color7 #BAC2DE
color15 #A6ADC8
```
#### kitty.conf
```
# BEGIN_KITTY_THEME
include Catppuccin-Mocha.conf
# END_KITTY_THEME

shell /opt/homebrew/bin/fish --login

window_padding_width 0
confirm_os_window_close 0
cursor_trail 3
remember_window_size no

font_size 13
font_family CodeNewRoman Nerd Font Mono
bold_font CodeNewRoman Nerd Font Mono Bold
italic_font CodeNewRoman Nerd Font Mono Italic

map ctrl+shift+v paste_from_clipboard
```

### fish
#### config.fish
```
# starship
export STARSHIP_CONFIG=$HOME/.config/starship/starship.toml
starship init fish | source

# zoxide
zoxide init fish | source

# greeting message
function fish_greeting
    figlet "Hi, Wenxi" | lolcat
end

# conda
/opt/miniconda3/bin/conda shell.fish hook | source
functions -c conda __conda_orig

function conda
    set -g _CE_CONDA ''
    __conda_orig $argv
end
```
#### conf.d/alias.fish
```
# System command
alias ls="eza --group-directories-first --icons=always --color=always"
alias ll="eza --group-directories-first --icons=always --color=always -alH --git"
alias cls="/usr/bin/clear"
alias cat="bat"
alias rm="rm -i"

# utils
alias untargz="tar -zxvf"
alias untarxz="tar -xJvf"
alias targz="tar -zcvf"
alias tarxz="tar -Jcvf"

# directory
abbr ... --position anywhere '../..'
abbr .... --position anywhere '../../..'
abbr ..... --position anywhere '../../../..'
abbr ...... --position anywhere '../../../../..'

# git
alias gi="git init"
alias gcl="git clone --recursive"
alias ga="git add .gitignore; and git rm -r --cached .; and git add -- ."
alias gc="git commit -m"
alias gcf="git commit --fixup"
alias gp="git push"
alias gpl="git pull --rebase"
alias gplm="git pull --rebase origin main"
alias gl="git log --oneline"
alias gb="git branch"
alias gs="git status"
```
#### conf.d/binds.fish
```
function exit_or_kill_line
    if test -n (commandline)
        commandline ""
        commandline -f repaint
    else
        exit
    end
end

bind -e \cd
bind \cd exit_or_kill_line

bind "" self-insert

bind \cH backward-kill-word
bind \e\[3\;5~ kill-word
```
#### conf.d/color.fish
```
set fish_color_command green
```
#### functions/proxy_toggle.fish
```
function proxy_on
    set server "127.0.0.1"
    set port "7890"

    if test (count $argv) -ge 1
        set server $argv[1]
    end
    if test (count $argv) -ge 2
        set port $argv[2]
    end

    set proxy_url http://$server:$port

    set -gx http_proxy $proxy_url
    set -gx https_proxy $proxy_url
    echo "终端代理已开启。"
end

function proxy_off
    set -e http_proxy
    set -e https_proxy
    echo "终端代理已关闭。"
end

function proxy_toggle
    set server "127.0.0.1"
    set port "7890"

    if test (count $argv) -ge 1
        set server $argv[1]
    end
    if test (count $argv) -ge 2
        set port $argv[2]
    end

    if set -q http_proxy; and set -q https_proxy
        proxy_off
    else
        proxy_on $server $port
    end
end
```

### starfish
#### starfish.toml
```
"$schema" = "https://starship.rs/config-schema.json"

format = """
[╭─](#7e726d)\
$sudo\
$os\
$username\
$localip\
$directory\
$git_branch\
$git_status\
$git_state\
$c\
$cmake\
$dotnet\
$golang\
$gradle\
$java\
$lua\
$nodejs\
$python\
$rust\
$package\
$fill\
$cmd_duration\
$conda\
$container\
$docker_context\
$time
[╰─](#7e726d)\
$character
"""

[c]
symbol = " "
format = "[$symbol($version(-$name))]($style) "
detect_extensions = ["c", "h", "cpp", "hpp", "cu"]
detect_files = ["Makefile", "CMakeLists.txt"]

[cmake]
format = "[cmake($symbol$version)]($style) "

[character]
# success_symbol = "[➜](bold green)"
# error_symbol = "[✖](bold red)"
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"

[cmd_duration]
format = "[◄ took](dimmed) [$duration](bold yellow) "

[conda]
symbol = "◯ "
format = "[$symbol$environment]($style) "
ignore_base = false

[container]
format = "[$symbol $name]($style) "

[directory]
use_os_path_sep = true
style = "#74c7ec"
repo_root_style = "bold #89dceb"
repo_root_format = "[$before_root_path](dimmed $style)[$repo_root]($repo_root_style)[$path]($repo_root_style)[$read_only]($read_only_style) "
read_only = " 󰌾"
format = "[$path]($style)[$read_only]($read_only_style) "
truncation_length = 3
truncate_to_repo = false
fish_style_pwd_dir_length = 1

[docker_context]
symbol = ""
style = "#06969A"
format = "[$symbol $context]($style) "

[dotnet]
symbol = "•NET "
format = "[$symbol$version( $tfm)]($style) "

[fill]
symbol = "─"
style = "#7e726d"

[git_branch]
symbol = ""
style = "#96f169"
format = "[$symbol $branch(:$remote_branch)]($style) "

[git_status]
ahead = "⇡${count} "
behind = "⇣${count} "
conflicted = "[=]${count} "
deleted = "✕${count} "
diverged = "⇕⇡${ahead_count} ⇣${behind_count} "
modified = "!${count} "
staged = "+${count} "
stashed = "\\$${count} "
renamed = "»${count} "
untracked = "?${count} "
format = """
[$ahead_behind](#96f169)\
[$conflicted](italic red)\
[$stashed](#8fbcbb)\
[$deleted](#f07178)\
[$renamed](#f2a272)\
[$modified](#fab387)\
[$staged](#a9b665)\
[$untracked](#89b4fa)\
"""

[golang]
symbol = " go "
format = "[$symbol($version)]($style) "

[java]
symbol = " java"
style = "red"
format = "[$symbol ($version)]($style) "

[localip]
ssh_only = true
format = "@[$localipv4](#81c8be) "
disabled = false

[lua]
symbol = " "
format = "[$symbol($version)]($style) "

[nodejs]
symbol = " "
format = "[$symbol($version)]($style) "

[os]
disabled = false
format = "$symbol "

[os.symbols]
Alpaquita = "[](#FF0080)"
Alpine = "[](#0D2149)"
AlmaLinux = "[[](#264F78)"
Amazon = "[](#FF9900)"
Android = "[](#A4C639)"
Arch = "[](#1793D1)"
Artix = "[](#1A5A9C)"
CentOS = "[](#EE2727)"
Debian = "[](#A80030)"
DragonFly = "[](#6F2DA8)"
Emscripten = "[](#5A4F4F)"
EndeavourOS = "[](#8C1A1A)"
Fedora = "[](#294172)"
FreeBSD = "[](#A92D31)"
Garuda = "[󰛓](#00B4D8)"
Gentoo = "[](#54487A)"
HardenedBSD = "[󰞌](#000000)"
Illumos = "[󰈸](#EA0000)"
Kali = "[](#557C94)"
Linux = "[](#FCC624)"
Mabox = "[](#FFCC00)"
# Macos = "[](#C0CAF5)"
Macos = ""
Manjaro = "[](#35BF5C)"
Mariner = "[](#0076DE)"
MidnightBSD = "[](#FFA500)"
Mint = "[](#87CF3E)"
NetBSD = "[](#C13A3A)"
NixOS = "[](#5277C3)"
OpenBSD = "[󰈺](#2F3030)"
openSUSE = "[](#73BA25)"
OracleLinux = "[󰌷](#F80000)"
Pop = "[](#6F2DA8)"
Raspbian = "[](#A22846)"
Redhat = "[](#EE2727)"
RedHatEnterprise = "[](#EE2727)"
RockyLinux = "[](#8C1A1A)"
Redox = "[󰀘](#000000)"
Solus = "[󰠳](#5294E2)"
SUSE = "[](#73BA25)"
Ubuntu = "[](#E95420)"
Unknown = "[](#4183C4)"
Void = "[](#00A0FF)"
Windows = "[󰍲](#C065DB)"

[package]
symbol = "󰏗 "
format = "is [$symbol$version](style) "

[python]
symbol = " "
format = "[$symbol($version)]($style) "

[rust]
symbol = "󱘗 "
format = "[$symbol$version]($style) "

[sudo]
format = "[$symbol]($style)"
style = "bold italic bright-purple"
symbol = "⋈┈"
disabled = false

[time]
style = "#96e3a1 dimmed"
format = "[at](dimmed) [ $time]($style) "
disabled = false

[username]
style_root = "red"
style_user = "yellow"
format = "[$user]($style)"
disabled = false
```