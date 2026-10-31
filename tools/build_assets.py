"""Draws the profile README artwork (assets/*.svg), light and dark.

GitHub shows README images through its image proxy: SVG with SMIL and CSS
animation plays, scripts and web fonts do not. So everything here is plain
shapes, system fonts, and declarative motion that pauses for people who ask
for reduced motion.

    python tools/build_assets.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

FONT = "'Segoe UI Variable Display','Segoe UI',Inter,-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
MONO = "'Cascadia Code','JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

THEMES = {
    "dark": {
        "sky_top": "#060b18", "sky_bottom": "#0b1730",
        "ink": "#eef4ff", "ink2": "#a9b8d6", "ink3": "#6f7f9f",
        "a1": "#3ee6c1", "a2": "#7c8cff", "a3": "#b48cff", "a4": "#38bdf8",
        "card": "#0d1628", "card_line": "#1f2c47", "pill": "#16233c",
        "blob_op": "0.55", "stars": True,
        "text": {"a1": "#3ee6c1", "a2": "#9aa6ff", "a3": "#c4a8ff", "a4": "#5ccbfa"},
    },
    "light": {
        "sky_top": "#f6f9ff", "sky_bottom": "#eaf2fb",
        "ink": "#0f1a33", "ink2": "#43506b", "ink3": "#7a869e",
        "a1": "#2dd4bf", "a2": "#818cf8", "a3": "#c4b5fd", "a4": "#7dd3fc",
        "card": "#ffffff", "card_line": "#dde6f3", "pill": "#eef3fb",
        "blob_op": "0.42", "stars": False,
        # Readable on white: the pastel accents are for light, these for words.
        "text": {"a1": "#0f8f7e", "a2": "#4f46e5", "a3": "#7c3aed", "a4": "#0369a1"},
    },
}

REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def stars(w, h, n, seed=7):
    # Deterministic sky: same picture every build.
    import random
    r = random.Random(seed)
    out = []
    for i in range(n):
        x, y = r.uniform(0, w), r.uniform(0, h * 0.9)
        rad = r.choice([0.6, 0.8, 1.0, 1.3])
        d = r.uniform(2.5, 6.0)
        delay = r.uniform(0, 6)
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" class="star" '
            f'style="animation-duration:{d:.1f}s;animation-delay:-{delay:.1f}s"/>'
        )
    return "\n    ".join(out)


AVATAR = (Path(__file__).resolve().parent / "src" / "avatar.b64").read_text().strip()


def hero(t, name):
    w, h = 1200, 360
    roles = [
        "I build software that reaches into hardware.",
        "Full-stack apps, shipped and kept running.",
        "Homelab, ESP32 and a lot of Docker.",
    ]
    role_spans = "".join(
        f'<text x="80" y="246" class="role r{i}">{escape(r)}</text>' for i, r in enumerate(roles)
    )
    star_layer = f'<g class="stars">\n    {stars(w, h, 70)}\n  </g>' if t["stars"] else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Redwan Rashid (Ricky): software developer and hardware tinkerer">
  <title>Redwan Rashid (Ricky)</title>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{t['sky_top']}"/>
      <stop offset="1" stop-color="{t['sky_bottom']}"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="48"/></filter>
    <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['ink']}"/>
      <stop offset="0.55" stop-color="{t['ink']}"/>
      <stop offset="1" stop-color="{t['a1']}"/>
    </linearGradient>
    <linearGradient id="ribbon" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['a1']}" stop-opacity="0"/>
      <stop offset="0.3" stop-color="{t['a1']}"/>
      <stop offset="0.65" stop-color="{t['a2']}"/>
      <stop offset="1" stop-color="{t['a3']}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="22"/></clipPath>
    <clipPath id="face"><circle cx="985" cy="180" r="112"/></clipPath>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['a1']}"/><stop offset=".5" stop-color="{t['a2']}"/><stop offset="1" stop-color="{t['a3']}"/>
    </linearGradient>
  </defs>
  <style>
    .name {{ font: 700 64px {FONT}; letter-spacing: -1.6px; fill: url(#nameGrad); }}
    .aka {{ font: 500 22px {FONT}; fill: {t['ink3']}; }}
    .role {{ font: 500 24px {FONT}; fill: {t['ink2']}; opacity: 0; animation: role 12s infinite; }}
    .r1 {{ animation-delay: 4s; }} .r2 {{ animation-delay: 8s; }}
    @keyframes role {{ 0%{{opacity:0;transform:translateY(8px)}} 4%,30%{{opacity:1;transform:none}} 34%,100%{{opacity:0;transform:translateY(-6px)}} }}
    .loc {{ font: 500 15px {MONO}; fill: {t['ink3']}; letter-spacing: .4px; }}
    .star {{ fill: {t['ink']}; animation: tw 4s ease-in-out infinite; }}
    @keyframes tw {{ 0%,100%{{opacity:.15}} 50%{{opacity:.9}} }}
    .curtain {{ animation: sway 16s ease-in-out infinite alternate; transform-origin: 50% 0; }}
    @keyframes sway {{ from{{transform:skewX(-6deg) translateX(-30px)}} to{{transform:skewX(6deg) translateX(30px)}} }}
    .dash {{ stroke-dasharray: 14 10; animation: flow 3s linear infinite; }}
    @keyframes flow {{ to{{stroke-dashoffset:-48}} }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    .ring {{ transform-origin: 985px 180px; animation: spin 18s linear infinite; }}
    @keyframes spin {{ to{{transform:rotate(360deg)}} }}
    .halo {{ transform-origin: 985px 180px; animation: halo 6s ease-in-out infinite; }}
    @keyframes halo {{ 0%,100%{{transform:scale(1);opacity:.55}} 50%{{transform:scale(1.06);opacity:.9}} }}
    @keyframes blink {{ 50%{{opacity:0}} }}
    {REDUCED}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#sky)"/>
    {star_layer}
    <g filter="url(#blur)" opacity="{t['blob_op']}">
      <ellipse cx="820" cy="80" rx="260" ry="90" fill="{t['a1']}">
        <animate attributeName="cx" values="820;930;780;820" dur="22s" repeatCount="indefinite"/>
        <animate attributeName="ry" values="90;130;80;90" dur="17s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="1040" cy="200" rx="220" ry="110" fill="{t['a2']}">
        <animate attributeName="cx" values="1040;960;1100;1040" dur="19s" repeatCount="indefinite"/>
        <animate attributeName="cy" values="200;150;230;200" dur="23s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="640" cy="300" rx="240" ry="80" fill="{t['a3']}">
        <animate attributeName="cx" values="640;720;600;640" dur="26s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="300" cy="-20" rx="300" ry="70" fill="{t['a4']}">
        <animate attributeName="cx" values="300;380;260;300" dur="21s" repeatCount="indefinite"/>
      </ellipse>
    </g>
    <g class="curtain" opacity="0.5">
      <path d="M700 0 C760 90 860 110 900 220 C930 300 1000 330 1200 340" fill="none" stroke="url(#ribbon)" stroke-width="2"/>
      <path d="M760 0 C820 70 940 120 980 200 C1010 260 1080 300 1200 300" fill="none" stroke="url(#ribbon)" stroke-width="1.2" opacity=".7"/>
      <path d="M640 0 C700 120 780 150 830 260 C860 320 930 350 1100 360" fill="none" stroke="url(#ribbon)" stroke-width="1" opacity=".5"/>
    </g>
    <!-- a tiny circuit trace: hardware meets software -->
    <g fill="none" stroke="{t['a1']}" stroke-width="1.6" opacity=".55">
      <path class="dash" d="M80 300 H330 L350 280 H520"/>
      <circle cx="80" cy="300" r="4" fill="{t['a1']}" stroke="none"/>
      <circle cx="520" cy="280" r="4" fill="none"/>
    </g>
    <!-- portrait -->
    <circle cx="985" cy="180" r="132" fill="url(#ring)" opacity=".25" filter="url(#blur)" class="halo"/>
    <circle cx="985" cy="180" r="124" fill="none" stroke="url(#ring)" stroke-width="3" stroke-dasharray="120 40 30 40" class="ring"/>
    <circle cx="985" cy="180" r="116" fill="{t['sky_bottom']}"/>
    <image href="data:image/jpeg;base64,{AVATAR}" x="873" y="68" width="224" height="224" clip-path="url(#face)" preserveAspectRatio="xMidYMid slice"/>
    <circle cx="985" cy="180" r="112" fill="none" stroke="{t['card_line']}" stroke-width="1"/>
    <text x="80" y="120" class="aka">Hi, I&#8217;m</text>
    <text x="80" y="190" class="name">{escape(name)}</text>
    <text x="80" y="246" class="role r0">{escape(roles[0])}</text>
    {role_spans[role_spans.index('</text>') + 7:]}
    <text x="80" y="330" class="loc">Founder, Bohuvuj Softwares <tspan fill="{t['a1']}">/</tspan> BCSE at IUBAT <tspan fill="{t['a1']}">/</tspan> Dhaka<tspan class="cursor" fill="{t['a1']}"> _</tspan></text>
    <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="22" fill="none" stroke="{t['card_line']}"/>
  </g>
</svg>
'''


PROJECTS = [
    {
        "id": "collectra", "title": "Collectra CMS", "status": "Live",
        "lines": ["Collections and hire-purchase accounts for", "retail branches, with Android and iPhone apps."],
        "tags": ["React", "Supabase", "Capacitor"], "accent": "a1", "glyph": "shield",
    },
    {
        "id": "timeforge", "title": "TimeForge", "status": "Building",
        "lines": ["An open-world builder on the real map", "of Earth, running in the browser."],
        "tags": ["three.js", "MapLibre", "Node"], "accent": "a2", "glyph": "globe",
    },
    {
        "id": "systracker", "title": "SysTracker", "status": "Live",
        "lines": ["Self-hosted monitoring for a fleet of", "machines: CPU, memory, disk, network."],
        "tags": ["Docker", "Node", "Agents"], "accent": "a4", "glyph": "pulse",
    },
    {
        "id": "perfumevault", "title": "Perfume Vault", "status": "Live",
        "lines": ["A perfume storefront with its own admin", "and content tools, for a Dhaka retailer."],
        "tags": ["Next.js", "Supabase", "Tailwind"], "accent": "a3", "glyph": "bottle",
    },
    {
        "id": "advance", "title": "Advance Manager", "status": "Live",
        "lines": ["Tracks advance payments across companies,", "vendors and crews, request to settlement."],
        "tags": ["TypeScript", "PostgreSQL", "Docker"], "accent": "a1", "glyph": "ledger",
    },
    {
        "id": "messmanager", "title": "MessManager", "status": "Live",
        "lines": ["Meals, groceries and dues for a shared mess:", "meal rate, ledgers and settlement."],
        "tags": ["Next.js", "Supabase", "PWA"], "accent": "a2", "glyph": "bowl",
    },
]


def glyph(kind, c):
    if kind == "shield":
        return f'<path d="M0 -15 L13 -9 V2 C13 10 6 15 0 17 C-6 15 -13 10 -13 2 V-9 Z" fill="none" stroke="{c}" stroke-width="2"/><path d="M-5 1 L-1 5 L6 -3" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "globe":
        return f'<circle r="15" fill="none" stroke="{c}" stroke-width="2"/><ellipse rx="6.5" ry="15" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M-15 0 H15 M-12 -8 H12 M-12 8 H12" stroke="{c}" stroke-width="1.4"/>'
    if kind == "pulse":
        return f'<path d="M-16 2 H-8 L-4 -10 L2 12 L6 -2 H16" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "bottle":
        return f'<rect x="-9" y="-6" width="18" height="22" rx="5" fill="none" stroke="{c}" stroke-width="2"/><rect x="-4" y="-14" width="8" height="8" rx="1.5" fill="none" stroke="{c}" stroke-width="2"/><path d="M-5 4 H5" stroke="{c}" stroke-width="1.6"/>'
    if kind == "ledger":
        return f'<rect x="-12" y="-15" width="24" height="30" rx="3" fill="none" stroke="{c}" stroke-width="2"/><path d="M-6 -6 H6 M-6 0 H6 M-6 6 H2" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>'
    if kind == "bowl":
        return f'<path d="M-15 -1 H15 C15 10 7 15 0 15 C-7 15 -15 10 -15 -1 Z" fill="none" stroke="{c}" stroke-width="2"/><path d="M-5 -6 C-7 -9 -3 -11 -5 -14 M3 -6 C1 -9 5 -11 3 -14" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
    return f'<rect x="-10" y="-10" width="20" height="20" rx="3" fill="none" stroke="{c}" stroke-width="2"/><path d="M-5 -14 V-10 M0 -14 V-10 M5 -14 V-10 M-5 10 V14 M0 10 V14 M5 10 V14 M-14 -5 H-10 M-14 0 H-10 M-14 5 H-10 M10 -5 H14 M10 0 H14 M10 5 H14" stroke="{c}" stroke-width="1.6"/>'


def card(t, p):
    w, h = 580, 200
    c = t[p["accent"]]
    pills, x = [], 32
    for tag in p["tags"]:
        tw = 16 + len(tag) * 8.2
        pills.append(f'<rect x="{x}" y="150" width="{tw:.0f}" height="28" rx="14" fill="{t["pill"]}"/><text x="{x + tw / 2:.0f}" y="169" class="tag" text-anchor="middle">{escape(tag)}</text>')
        x += tw + 8
    lines = "".join(f'<text x="32" y="{104 + i * 24}" class="body">{escape(l)}</text>' for i, l in enumerate(p["lines"]))
    live = p["status"] in ("Live", "Running")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(p['title'])}: {escape(' '.join(p['lines']))}">
  <title>{escape(p['title'])}</title>
  <defs>
    <radialGradient id="glow" cx="1" cy="0" r="1">
      <stop offset="0" stop-color="{c}" stop-opacity=".28"/>
      <stop offset="1" stop-color="{c}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <style>
    .title {{ font: 700 26px {FONT}; fill: {t['ink']}; letter-spacing: -.4px; }}
    .body {{ font: 400 16px {FONT}; fill: {t['ink2']}; }}
    .tag {{ font: 500 13px {MONO}; fill: {t['ink2']}; }}
    .status {{ font: 600 13px {FONT}; fill: {t['text'][p['accent']]}; }}
    .glow {{ animation: breathe 7s ease-in-out infinite; }}
    @keyframes breathe {{ 0%,100%{{opacity:.7}} 50%{{opacity:1}} }}
    .dot {{ animation: ping 2.4s ease-out infinite; transform-origin: center; transform-box: fill-box; }}
    @keyframes ping {{ 0%{{transform:scale(1);opacity:.7}} 80%,100%{{transform:scale(2.6);opacity:0}} }}
    {REDUCED}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{t['card']}"/>
    <rect width="{w}" height="{h}" fill="url(#glow)" class="glow"/>
    <g transform="translate({w - 56} 52)" opacity=".9">{glyph(p['glyph'], c)}</g>
    <text x="32" y="62" class="title">{escape(p['title'])}</text>
    <text x="{w - 32}" y="169" class="status" text-anchor="end">{escape(p['status'])}</text>
    {f'<circle cx="{w - 46 - len(p["status"]) * 6.6:.0f}" cy="164" r="4.5" fill="{c}" class="dot"/>' if live else ''}
    <circle cx="{w - 46 - len(p["status"]) * 6.6:.0f}" cy="164" r="4.5" fill="{c}"/>
    {lines}
    {''.join(pills)}
    <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="none" stroke="{t['card_line']}"/>
  </g>
</svg>
'''


def footer(t):
    w, h = 1200, 120
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Thanks for visiting">
  <title>Thanks for visiting</title>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['a1']}"/><stop offset=".5" stop-color="{t['a2']}"/><stop offset="1" stop-color="{t['a3']}"/>
    </linearGradient>
  </defs>
  <style>
    .w {{ fill: none; stroke: url(#g); stroke-linecap: round; }}
    .t {{ font: 500 15px {MONO}; fill: {t['ink3']}; letter-spacing: .5px; }}
    {REDUCED}
  </style>
  <path class="w" stroke-width="2" opacity=".8" d="M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 100 1200 70">
    <animate attributeName="d" dur="10s" repeatCount="indefinite" values="M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 100 1200 70;M0 70 C150 100 300 40 450 70 S750 100 900 70 S1100 40 1200 70;M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 100 1200 70"/>
  </path>
  <path class="w" stroke-width="1.2" opacity=".4" d="M0 82 C200 60 350 105 600 82 S1000 60 1200 82">
    <animate attributeName="d" dur="13s" repeatCount="indefinite" values="M0 82 C200 60 350 105 600 82 S1000 60 1200 82;M0 82 C200 105 350 60 600 82 S1000 105 1200 82;M0 82 C200 60 350 105 600 82 S1000 60 1200 82"/>
  </path>
  <text x="600" y="30" class="t" text-anchor="middle">built, broken, fixed, shipped</text>
</svg>
'''


# First commit of each project (git history), not when the repo was made.
MILESTONES = [
    ("Jun 2025", "Purrfect Feeder", "first IoT build"),
    ("Feb 2026", "SysTracker", "fleet monitoring"),
    ("Apr 2026", "Bohuvuj Softwares", "bohuvuj.com goes up"),
    ("Apr 2026", "Perfume Vault", "storefront and admin"),
    ("Jul 2026", "BeeEzee", "ERP and CRM"),
    ("Sep 2026", "Collectra CMS", "live in October"),
    ("Oct 2026", "TimeForge", "the open world"),
]


def timeline(t):
    w, h = 1200, 210
    n = len(MILESTONES)
    x0, x1, y = 90, 1110, 92
    step = (x1 - x0) / (n - 1)
    nodes = []
    for i, (when, what, note) in enumerate(MILESTONES):
        x = x0 + i * step
        last = i == n - 1
        c = t["a1"] if last else t[["a4", "a2", "a3"][i % 3]]
        nodes.append(f'''<g>
      {f'<circle cx="{x:.0f}" cy="{y}" r="9" fill="{c}" class="ping"/>' if last else ''}
      <circle cx="{x:.0f}" cy="{y}" r="{7 if last else 5.5}" fill="{t['card']}" stroke="{c}" stroke-width="2.5"/>
      <text x="{x:.0f}" y="{y - 26}" class="when" text-anchor="middle">{escape(when)}</text>
      <text x="{x:.0f}" y="{y + 40}" class="what" text-anchor="middle">{escape(what)}</text>
      <text x="{x:.0f}" y="{y + 62}" class="note" text-anchor="middle">{escape(note)}</text>
    </g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Milestones: {escape('; '.join(f'{a} {b}' for a, b, _ in MILESTONES))}">
  <title>Milestones</title>
  <defs>
    <linearGradient id="line" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{x1}" y2="0">
      <stop offset="0" stop-color="{t['a4']}" stop-opacity=".2"/><stop offset=".6" stop-color="{t['a2']}"/><stop offset="1" stop-color="{t['a1']}"/>
    </linearGradient>
  </defs>
  <style>
    .when {{ font: 600 14px {MONO}; fill: {t['ink3']}; letter-spacing: .3px; }}
    .what {{ font: 700 17px {FONT}; fill: {t['ink']}; }}
    .note {{ font: 400 14px {FONT}; fill: {t['ink2']}; }}
    .run {{ stroke-dasharray: 6 1000; animation: run 6s linear infinite; }}
    @keyframes run {{ from{{stroke-dashoffset:0}} to{{stroke-dashoffset:-1030}} }}
    .ping {{ transform-box: fill-box; transform-origin: center; animation: ping 2.4s ease-out infinite; }}
    @keyframes ping {{ 0%{{transform:scale(1);opacity:.6}} 80%,100%{{transform:scale(2.4);opacity:0}} }}
    {REDUCED}
  </style>
  <path d="M{x0} {y} H{x1}" stroke="url(#line)" stroke-width="2.5" fill="none"/>
  <path d="M{x0} {y} H{x1}" stroke="{t['ink']}" stroke-width="3" fill="none" stroke-linecap="round" class="run" opacity=".8"/>
  {"".join(nodes)}
</svg>
'''


def main():
    OUT.mkdir(exist_ok=True)
    for mode, t in THEMES.items():
        (OUT / f"hero-{mode}.svg").write_text(hero(t, "Redwan Rashid"), encoding="utf-8")
        (OUT / f"footer-{mode}.svg").write_text(footer(t), encoding="utf-8")
        (OUT / f"milestones-{mode}.svg").write_text(timeline(t), encoding="utf-8")
        for p in PROJECTS:
            (OUT / f"card-{p['id']}-{mode}.svg").write_text(card(t, p), encoding="utf-8")
    print("wrote", len(list(OUT.glob("*.svg"))), "files to", OUT)


if __name__ == "__main__":
    main()
