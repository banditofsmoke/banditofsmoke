"""Generate the "feat: hire Wayne Sletcher" pull-request banner, dark and light.

Edit CHECKS below, then run:  python assets/make_banner.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(
        bg="#0d1117", fg="#e6edf3", muted="#9198a1", border="#3d444d",
        pill="#238636", green="#3fb950", yellow="#d29922", link="#4493f8",
        tab="#fd8c73", bubble="#2f3742",
        btn_off="#212830", btn_off_stroke="#3d444d", btn_off_text="#656c76",
        btn_on="#238636", btn_on_stroke="#2ea043", head_bg="#151b23",
    ),
    "light": dict(
        bg="#ffffff", fg="#1f2328", muted="#59636e", border="#d1d9e0",
        pill="#1f883d", green="#1a7f37", yellow="#9a6700", link="#0969da",
        tab="#fd8c73", bubble="#e6eaef",
        btn_off="#eff2f5", btn_off_stroke="#d1d9e0", btn_off_text="#818b98",
        btn_on="#1f883d", btn_on_stroke="#1a7f37", head_bg="#f6f8fa",
    ),
}

CHECKS = [
    ("production / ship", "esl.sletchersystems.com is live and taking payments"),
    ("upstream / unsloth", "5 PRs merged into a 77k★ repo"),
    ("upstream / llama_index", "3 Windows fixes in review at a 52k★ repo"),
    ("tests / ci", "1,200+ tests on the ESL platform, CI on every PR"),
    ("build / courses", "Git From Zero and Kubernetes & OpenShift, both live"),
    ("ops / timezone", "UTC+2, overlapping Europe's whole working day"),
]

W, H = 900, 668
X0, X1 = 28, 872          # merge box edges
FIRST, STEP = 0.9, 0.55   # seconds: first check passes, gap between checks
DONE = FIRST + STEP * len(CHECKS) + 0.2
ROW0, ROW_H = 262, 40


def e(s):
    return escape(s, quote=False)


def spinner(cx, cy, r, color, width=2):
    dash = f"{r * 0.9:.1f} {r * 0.6:.1f}"
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-dasharray="{dash}" stroke-linecap="round">'
        f'<animateTransform attributeName="transform" type="rotate" '
        f'from="0 {cx} {cy}" to="360 {cx} {cy}" dur="1s" repeatCount="indefinite"/></circle>'
    )


def check(cx, cy, color, s=1.0, width=2):
    return (
        f'<path d="M{cx - 5 * s:.1f} {cy:.1f} L{cx - 1.5 * s:.1f} {cy + 3.5 * s:.1f} '
        f'L{cx + 5 * s:.1f} {cy - 3.5 * s:.1f}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def swap(t, before, after):
    """Show `before` until t seconds, then `after`, and hold."""
    return (
        f'<g>{before}<set attributeName="opacity" to="0" begin="{t:.2f}s" fill="freeze"/></g>'
        f'<g opacity="0">{after}<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></g>'
    )


def pr_icon(x, y, color):
    # a pull-request glyph in a 16px box at (x, y)
    return (
        f'<g fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
        f'<circle cx="{x + 4}" cy="{y + 3}" r="1.9"/><path d="M{x + 4} {y + 5} V{y + 11}"/>'
        f'<circle cx="{x + 4}" cy="{y + 13}" r="1.9"/><circle cx="{x + 12}" cy="{y + 13}" r="1.9"/>'
        f'<path d="M{x + 12} {y + 11} V{y + 6.5} Q{x + 12} {y + 3.5} {x + 9} {y + 3.5} H{x + 7}"/>'
        f'<path d="M{x + 8.6} {y + 1.6} L{x + 6.8} {y + 3.5} L{x + 8.6} {y + 5.4}"/></g>'
    )


def build(t):
    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'role="img" aria-labelledby="t d">')
    a('<title id="t">feat: hire Wayne Sletcher</title>')
    a('<desc id="d">A pull request asking to merge one engineer into your team. Six checks pass: '
      'shipped to production, five PRs merged into Unsloth, three fixes in review at LlamaIndex, 1,200+ tests, '
      'two live courses, UTC+2. No conflicts with the base branch. Merge pull request: wsletcher@gmail.com</desc>')
    a(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}"/>')
    a(f'<g font-family="{SANS}">')

    # title + meta line
    a(f'<text x="{X0}" y="58" font-size="28" fill="{t["fg"]}">feat: hire Wayne Sletcher'
      f'<tspan fill="{t["muted"]}" font-weight="300"> #1</tspan></text>')
    a(f'<rect x="{X0}" y="82" width="76" height="28" rx="14" fill="{t["pill"]}"/>')
    a(pr_icon(X0 + 11, 88, "#ffffff"))
    a(f'<text x="{X0 + 33}" y="101" font-size="14" font-weight="600" fill="#ffffff">Open</text>')
    a(f'<text x="{X0 + 88}" y="101" font-size="14" fill="{t["muted"]}">'
      f'<tspan font-weight="600" fill="{t["fg"]}">Sletch</tspan> wants to merge '
      f'<tspan font-weight="600" fill="{t["fg"]}">1 engineer</tspan> into '
      f'<tspan font-family="{MONO}" fill="{t["link"]}">your-team:main</tspan> from '
      f'<tspan font-family="{MONO}" fill="{t["link"]}">sletch:available-now</tspan></text>')

    # tabs
    for label, x in (("Conversation", X0), ("Commits", 150), ("Checks", 250), ("Files changed", 370)):
        sel = label == "Checks"
        weight = ' font-weight="600"' if sel else ""
        a(f'<text x="{x}" y="152" font-size="14" fill="{t["fg"] if sel else t["muted"]}"{weight}>{label}</text>')
    a(f'<rect x="306" y="138" width="22" height="19" rx="9.5" fill="{t["bubble"]}"/>')
    a(f'<text x="317" y="152" font-size="12" font-weight="600" text-anchor="middle" fill="{t["fg"]}">6</text>')
    a(f'<line x1="1" y1="170" x2="{W - 1}" y2="170" stroke="{t["border"]}"/>')
    a(f'<rect x="242" y="167" width="94" height="3" rx="1.5" fill="{t["tab"]}"/>')

    # merge box
    a(f'<rect x="{X0}" y="196" width="{X1 - X0}" height="444" rx="8" fill="{t["bg"]}" stroke="{t["border"]}"/>')
    a(f'<path d="M{X0 + 0.5} 262 V204 Q{X0 + 0.5} 196.5 {X0 + 8} 196.5 H{X1 - 8} '
      f'Q{X1 - 0.5} 196.5 {X1 - 0.5} 204 V262 Z" fill="{t["head_bg"]}"/>')
    a(swap(
        DONE,
        spinner(60, 229, 12, t["yellow"], 2.5)
        + f'<text x="88" y="225" font-size="16" font-weight="600" fill="{t["fg"]}">Some checks haven’t completed yet</text>'
        + f'<text x="88" y="247" font-size="14" fill="{t["muted"]}">Running 6 checks…</text>',
        f'<circle cx="60" cy="229" r="14" fill="{t["pill"]}"/>' + check(60, 229, "#ffffff", 1.1, 2.2)
        + f'<text x="88" y="225" font-size="16" font-weight="600" fill="{t["fg"]}">All checks have passed</text>'
        + f'<text x="88" y="247" font-size="14" fill="{t["muted"]}">6 successful checks</text>',
    ))
    a(f'<line x1="{X0}" y1="262" x2="{X1}" y2="262" stroke="{t["border"]}"/>')

    for i, (name, desc) in enumerate(CHECKS):
        cy = ROW0 + ROW_H // 2 + i * ROW_H
        a(swap(FIRST + i * STEP, spinner(60, cy, 6.5, t["yellow"]), check(60, cy, t["green"])))
        a(f'<text x="84" y="{cy + 5}" font-size="14" fill="{t["muted"]}">'
          f'<tspan font-weight="600" fill="{t["fg"]}">{e(name)}</tspan>  ·  {e(desc)}</text>')
    end = ROW0 + ROW_H * len(CHECKS)
    a(f'<line x1="{X0}" y1="{end}" x2="{X1}" y2="{end}" stroke="{t["border"]}"/>')

    # no conflicts
    a(f'<circle cx="60" cy="{end + 33}" r="14" fill="{t["pill"]}"/>' + check(60, end + 33, "#ffffff", 1.1, 2.2))
    a(f'<text x="88" y="{end + 28}" font-size="16" font-weight="600" fill="{t["fg"]}">'
      f'This branch has no conflicts with the base branch</text>')
    a(f'<text x="88" y="{end + 50}" font-size="14" fill="{t["muted"]}">'
      f'Available now · contract, freelance or full-time · remote from South Africa</text>')
    a(f'<line x1="{X0}" y1="{end + 66}" x2="{X1}" y2="{end + 66}" stroke="{t["border"]}"/>')

    # merge button: disabled until the checks pass, then green and pulsing
    by = end + 84
    bx, bw, bh = 52, 186, 36
    a(f'<rect x="{bx - 3}" y="{by - 3}" width="{bw + 6}" height="{bh + 6}" rx="8" fill="none" '
      f'stroke="{t["green"]}" stroke-width="2" opacity="0">'
      f'<animate attributeName="opacity" values="0;0.75;0" dur="2s" begin="{DONE + 0.2:.2f}s" repeatCount="indefinite"/></rect>')
    a(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6" fill="{t["btn_off"]}" stroke="{t["btn_off_stroke"]}">'
      f'<set attributeName="fill" to="{t["btn_on"]}" begin="{DONE:.2f}s" fill="freeze"/>'
      f'<set attributeName="stroke" to="{t["btn_on_stroke"]}" begin="{DONE:.2f}s" fill="freeze"/></rect>')
    a(f'<line x1="{bx + bw - 32}" y1="{by}" x2="{bx + bw - 32}" y2="{by + bh}" stroke="{t["btn_off_stroke"]}">'
      f'<set attributeName="stroke" to="{t["btn_on_stroke"]}" begin="{DONE:.2f}s" fill="freeze"/></line>')
    for txt, x, extra in (("Merge pull request", bx + (bw - 32) / 2, ' text-anchor="middle"'),
                          ("▾", bx + bw - 16, ' text-anchor="middle"')):
        a(f'<text x="{x}" y="{by + 23}" font-size="14" font-weight="600" fill="{t["btn_off_text"]}"{extra}>{txt}'
          f'<set attributeName="fill" to="#ffffff" begin="{DONE:.2f}s" fill="freeze"/></text>')
    a(f'<text x="{bx + bw + 18}" y="{by + 23}" font-size="14" fill="{t["muted"]}">or just email '
      f'<tspan fill="{t["link"]}" font-weight="600">wsletcher@gmail.com</tspan></text>')

    a('</g></svg>')
    return "\n".join(p)


for name, theme in THEMES.items():
    (OUT / f"hire-me-{name}.svg").write_text(build(theme), encoding="utf-8")
    print("wrote", OUT / f"hire-me-{name}.svg")
