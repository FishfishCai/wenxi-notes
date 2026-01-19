# Plugins
- AttachFlow: better PDF and image notes reference.
- Better Link Clicker: change click-to-open into Ctrl+click-to-open.
- BRAT: support install plugins from GitHub and beta versions.
- Editor Width Slider: adjust editor line width interactively with a slider.
- File Explorer Note Count: show note counts in the file explorer.
- Git: support Git.
- Lapel: show extra info at the line number area.
- Latex Suite: support LaTeX input and shortcuts.
- LaTeX-like Theorem & Equation Referencer: provide theorem-style callouts.
- Live Background: dynamic wallpaper.
- MathLinks: dependency of LaTeX-like Theorem & Equation Referencer.
- PDF++: enhance PDF reading and annotation.
- Quick Preview: dependency of LaTeX-like Theorem & Equation Referencer.
- Quiet Outline: show a clean, low-noise outline panel.
- Style Settings: expose theme and CSS options in a settings panel for controlled UI customization.
- TikZJax: support TikZ diagrams.

# Latex Suite
```
[
    // blocks
	{trigger: "beg", replacement: "\\begin{$0}\n$1\n\\end{$0}", options: "mA"},
	{trigger: "align", replacement: "\\begin{align}\n$0\n\\end{align}", options: "mA"},
	{trigger: "cases", replacement: "\\begin{cases}\n$0\n\\end{cases}", options: "mA"},
	{trigger: "array", replacement: "\\begin{array}\n$0\n\\end{array}", options: "mA"},
	{trigger: "matrix", replacement: "\\begin{matrix}\n$0\n\\end{matrix}", options: "MA"},
	{trigger: "pmat", replacement: "\\begin{pmatrix}\n$0\n\\end{pmatrix}", options: "MA"},
	{trigger: "bmat", replacement: "\\begin{bmatrix}\n$0\n\\end{bmatrix}", options: "MA"},
	{trigger: "Bmat", replacement: "\\begin{Bmatrix}\n$0\n\\end{Bmatrix}", options: "MA"},
	{trigger: "vmat", replacement: "\\begin{vmatrix}\n$0\n\\end{vmatrix}", options: "MA"},
	{trigger: "Vmat", replacement: "\\begin{Vmatrix}\n$0\n\\end{Vmatrix}", options: "MA"},
	{trigger: "dm", replacement: "$$\n$0\n$$", options: "tA"},
	{trigger: "mk", replacement: "$$0$$1", options: "tA"},
	{trigger: "proof", replacement: "`\\begin{proof}`\n$0\n`\\end{proof}`\n$1", options: "t"},

    // callout
	{trigger: "def", replacement: "> [!definition|] $0\n$1", options: "t"},
	{trigger: "thm", replacement: "> [!theorem|]$0\n$1", options: "t"},
	{trigger: "lemma", replacement: "> [!lemma|] $0\n$1", options: "t"},
	{trigger: "prop", replacement: "> [!proposition|]$0\n$1", options: "t"},
	{trigger: "rmk", replacement: "> [!remark|]$0\n$1", options: "t"},
	{trigger: "example", replacement: "> [!example|]$0\n$1", options: "t"},

    // tikz
    	{trigger: "tikz", replacement: "```tikz\n\\usepackage{tikz-cd}\n\\begin{document}\n\\begin{tikzcd}\n$0\n\\end{tikzcd}\n\\end{document}\n``` ", options: "t"},

    // text
	{trigger: "text", replacement: "\\text{$0}$1", options: "mA"},

    // style
 	{trigger: "bf", replacement: "\\mathbf{$0}", options: "mA"},
	{trigger: "rm", replacement: "\\mathrm{$0}", options: "mA"},
    	{trigger: "bb", replacement: "\\mathbb{$0}", options: "mA"},

    // accents
	{trigger: "hat", replacement: "\\hat{$0}", options: "m"},
    	{trigger: "bar", replacement: "\\bar{$0}", options: "m"},
	{trigger: "dot", replacement: "\\dot{$0}", options: "m"},
	{trigger: "ddot", replacement: "\\ddot{$0}", options: "m"},
	{trigger: "tilde", replacement: "\\tilde{$0}", options: "m"},
	{trigger: "und", replacement: "\\underline{$0}", options: "m"},
	{trigger: "vec", replacement: "\\vec{$0}", options: "m"},

    // braces
	{trigger: "U", replacement: "\\underbrace{${VISUAL}}_{$0}", options: "mA"},
	{trigger: "O", replacement: "\\overbrace{${VISUAL}}^{$0}", options: "mA"},
	{trigger: "u", replacement: "\\underset{$0}{ ${VISUAL}}", options: "mA"},
	{trigger: "o", replacement: "\\overset{$0}{ ${VISUAL}}", options: "mA"},

    // script
	{trigger: "_", replacement: "_{$0}", options: "mA"},
    	{trigger: "^", replacement: "^{$0}", options: "mA"},

    // brackets
	{trigger: "mod", replacement: "|$0|$1", options: "m"},
	{trigger: "norm", replacement: "\|$0\|", options: "m"},
	{trigger: "ceil", replacement: "\\lceil$0\\rceil", options: "m"},
	{trigger: "floor", replacement: "\\lfloor$0\\rfloor", options: "m"},
	{trigger: "(", replacement: "(${VISUAL})", options: "mA"},
	{trigger: "[", replacement: "[${VISUAL}]", options: "mA"},
	{trigger: "{", replacement: "{${VISUAL}}", options: "mA"},
	{trigger: "(", replacement: "($0)", options: "mA"},
	{trigger: "{", replacement: "{$0}", options: "mA"},
	{trigger: "[", replacement: "[$0]", options: "mA"},
	{trigger: "lr(", replacement: "\\left($0\\right)", options: "mA"},
	{trigger: "lr{", replacement: "\\left\\{$0\\right\\}", options: "mA"},
	{trigger: "lr[", replacement: "\\left[$0\\right]", options: "mA"},

    // arith
	{trigger: "sq", replacement: "\\sqrt{$0}", options: "mA"},
    	{trigger: "cdot", replacement: "\\cdot", options: "mA"},
	{trigger: "xx", replacement: "\\times", options: "mA"},
	{trigger: "sum", replacement: "\\sum", options: "mA"},
	{trigger: "prod", replacement: "\\prod", options: "mA"},
    	{trigger: "+-", replacement: "\\pm", options: "mA"},
	{trigger: "-+", replacement: "\\mp", options: "mA"},

    // relation
	{trigger: "===", replacement: "\\equiv", options: "mA"},
    	{trigger: "!=", replacement: "\\neq", options: "mA"},
	{trigger: ">=", replacement: "\\geq", options: "mA"},
	{trigger: "<=", replacement: "\\leqslant", options: "mA"},
	{trigger: ">>", replacement: "\\gg", options: "mA"},
	{trigger: "<<", replacement: "\\ll", options: "mA"},
	{trigger: "sim", replacement: "\\sim", options: "mA"},
    	{trigger: "prop", replacement: "\\propto", options: "mA"},
	{trigger: "perp", replacement: "\\perp", options: "mA"},
    	{trigger: "para", replacement: "\\parallel", options: "mA"},

    // sets
	{trigger: "eset", replacement: "\\emptyset", options: "mA"},
    	{trigger: "in", replacement: "\\in", options: "mA"},
	{trigger: "and", replacement: "\\cap", options: "mA"},
	{trigger: "or", replacement: "\\cup", options: "mA"},
    	{trigger: "subset", replacement: "\\subset", options: "mA"},
    	{trigger: "supset", replacement: "\\supset", options: "mA"},
    	{trigger: "sub=", replacement: "\\subseteq", options: "mA"},
    	{trigger: "sup=", replacement: "\\supseteq", options: "mA"},

    // logic
	{trigger: "exists", replacement: "\\exists", options: "mA"},
	{trigger: "forall", replacement: "\\forall", options: "mA"},

    // arrows
    	{trigger: "<->", replacement: "\\leftrightarrow ", options: "mA"},
	{trigger: "->", replacement: "\\to", options: "mA"},
	{trigger: "<-", replacement: "\\leftarrow", options: "mA"},
    	{trigger: "=>", replacement: "\\implies", options: "mA"},
	{trigger: "=<", replacement: "\\impliedby", options: "mA"},

    // analysis
    	{trigger: "...", replacement: "\\cdots ", options: "mA"},
    	{trigger: "infty", replacement: "\\infty", options: "mA"},
    	{trigger: "lim", replacement: "\\lim", options: "mA"},

    // calculus
	{trigger: "nabla", replacement: "\\nabla", options: "mA"},
	{trigger: "partial", replacement: "\\partial", options: "mA"},
    	{trigger: "par", replacement: "\\frac{ \\partial $0 }{ \\partial $1 } $2", options: "m"},
    	{trigger: "der", replacement: "\\frac{d $0}{d $1} $2", options: "m"},
	{trigger: "int", replacement: "\\int_{$0}^{$1} $2", options: "m"},

    // linear
	{trigger: "ip", replacement: "\\langle $0 \\rangle", options: "m"},
	{trigger: "invs", replacement: "^{-1}", options: "m"},
    	{trigger: "tran", replacement: "^{\\top}", options: "m"},
    	{trigger: "tr", replacement: "\\mathrm{Tr}", options: "m"},
	{trigger: "ker", replacement: "\\ker", options: "mA"},
    	{trigger: "coker", replacement: "\\mathop{\\mathrm{coker}}", options: "mA"},

    // complex
    	{trigger: "conj", replacement: "^{*}", options: "m"},
    	{trigger: "re", replacement: "\\mathrm{Re}", options: "mA"},
	{trigger: "im", replacement: "\\mathrm{Im}", options: "mA"},

    // number
	{trigger: "CC", replacement: "\\mathbb{C}", options: "mA"},
	{trigger: "RR", replacement: "\\mathbb{R}", options: "mA"},
	{trigger: "ZZ", replacement: "\\mathbb{Z}", options: "mA"},
	{trigger: "NN", replacement: "\\mathbb{N}", options: "mA"},

    // trig
    	{trigger: /([^\\])(arcsin|sin|arccos|cos|arctan|tan|csc|sec|cot)/, replacement: "[[0]]\\[[1]]", options: "rmA"},
    	{trigger: /\\(arcsin|sin|arccos|cos|arctan|tan|csc|sec|cot)([A-Za-gi-z])/, replacement: "\\[[0]] [[1]]", options: "rmA"},
    	{trigger: /\\(sinh|cosh|tanh|coth)([A-Za-z])/, replacement: "\\[[0]] [[1]]", options: "rmA"},

    // greek
	{trigger: "(^|[^\\\\])(${GREEK})", replacement: "[[0]]\\[[1]]", options: "rmA", description: "Add backslash before Greek letters"},
	{trigger: "\\\\(${GREEK})([A-Za-z])", replacement: "\\[[0]] [[1]]", options: "rmA"},
]
```
```
{
	"${GREEK}": "alpha|beta|gamma|Gamma|delta|Delta|epsilon|varepsilon|zeta|eta|theta|vartheta|Theta|iota|kappa|lambda|Lambda|mu|nu|xi|Xi|pi|Pi|rho|varrho|sigma|Sigma|tau|upsilon|Upsilon|phi|varphi|Phi|chi|psi|Psi|omega|Omega"
}
```