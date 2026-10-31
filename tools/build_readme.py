"""Writes README.md from the project list below (artwork: build_assets.py).

    python tools/build_readme.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Bump when the artwork changes: GitHub caches images by URL.
V = 6


def pic(name, alt, width="49%"):
    """A light/dark pair of local artwork that follows the GitHub theme."""
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg?v={V}">'
        f'<img alt="{alt}" src="assets/{name}-light.svg?v={V}" width="{width}"></picture>'
    )


def icons(ids, alt):
    # srcset splits on commas, so the icon list's commas are escaped.
    q = "%2C".join(ids)
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i={q}&theme=dark">'
        f'<img alt="{alt}" src="https://skillicons.dev/icons?i={q}&theme=light" height="44"></picture>'
    )


def stats(kind, extra, alt, attr):
    base = f"https://ghstats.dev/api/{kind}?username=Redwan002117"
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}&theme=dark&hide_border=true&{extra}">'
        f'<img alt="{alt}" src="{base}&theme=light&{extra}" {attr}></picture>'
    )


CARDS = [
    ("collectra", "https://singercms.bohuvuj.com/", "Collectra CMS: collections and hire-purchase accounts for retail branches, with Android and iPhone apps. Live."),
    ("timeforge", "https://rico.bd/", "TimeForge: an open-world builder on the real map of Earth, running in the browser. Building."),
    ("systracker", "https://systracker.rico.bd/", "SysTracker: self-hosted monitoring for a fleet of machines. Live."),
    ("perfumevault", "https://perfumevaultbd.com/", "Perfume Vault: a perfume storefront with its own admin and content tools. Live."),
    ("advance", "https://advance.rico.bd/", "Advance Manager: tracks advance payments across companies, vendors and crews. Live."),
    ("messmanager", "https://mess.bohuvuj.com/", "MessManager: meals, groceries and dues for a shared mess. Live."),
]

MORE = [
    ("beeezee", "https://beeezee.bohuvuj.com/", "BeeEzee: ERP and CRM for a growing business"),
    ("bohupay", "https://github.com/Bohuvuj", "BohuPay: drop-in payments for Bangladeshi gateways"),
    ("subash", "https://suubas.com/", "Subash: a fragrance storefront"),
    ("feeder", "https://purrfectfeeder.rico.bd/", "Purrfect Feeder: an ESP32 pet feeder run from a phone"),
    ("homelab", "https://rico.bd/", "Homelab: Docker server and ESP32-C6 Wi-Fi sensing"),
    ("research", "https://github.com/Redwan002117/D_A_GeoFormer", "Research: GeoFormer thesis code and exoplanet notebooks"),
]

STACK = [
    ("Languages", ["ts", "js", "py", "c", "cpp", "go", "java", "php", "powershell"], "TypeScript, JavaScript, Python, C, C++, Go, Java, PHP, PowerShell"),
    ("Frontend and mobile", ["react", "nextjs", "vite", "tailwind", "svelte", "vue", "flutter", "threejs"], "React, Next.js, Vite, Tailwind, Svelte, Vue, Flutter, three.js"),
    ("Backend and data", ["nodejs", "express", "postgres", "supabase", "prisma", "redis", "mysql", "sqlite", "firebase"], "Node.js, Express, PostgreSQL, Supabase, Prisma, Redis, MySQL, SQLite, Firebase"),
    ("Cloud and ops", ["docker", "linux", "nginx", "cloudflare", "vercel", "netlify", "gcp", "githubactions", "git"], "Docker, Linux, nginx, Cloudflare, Vercel, Netlify, Google Cloud, GitHub Actions, Git"),
    ("Hardware and design", ["arduino", "raspberrypi", "figma", "ai", "ae"], "Arduino and ESP32, Raspberry Pi, Figma, Illustrator, After Effects"),
]

SOCIALS = [
    ("Portfolio", "https://rico.bd/", "https://cdn.simpleicons.org/googlechrome/8b9bb4"),
    ("LinkedIn", "https://linkedin.com/in/gamerno002117", "assets/linkedin.svg"),
    ("Behance", "https://behance.net/gamerno002117", "https://cdn.simpleicons.org/behance/8b9bb4"),
    ("X", "https://x.com/redwanrico", "https://cdn.simpleicons.org/x/8b9bb4"),
    ("Instagram", "https://instagram.com/gamerno002117", "https://cdn.simpleicons.org/instagram/8b9bb4"),
    ("Facebook", "https://facebook.com/gamerno002117.99", "https://cdn.simpleicons.org/facebook/8b9bb4"),
    ("YouTube", "https://youtube.com/@gamerno002117", "https://cdn.simpleicons.org/youtube/8b9bb4"),
    ("Twitch", "https://twitch.tv/gamerno002117", "https://cdn.simpleicons.org/twitch/8b9bb4"),
    ("TikTok", "https://tiktok.com/@gamerno002117", "https://cdn.simpleicons.org/tiktok/8b9bb4"),
    ("Reddit", "https://reddit.com/user/gamerno002117", "https://cdn.simpleicons.org/reddit/8b9bb4"),
    ("Pinterest", "https://pinterest.com/gamerno002117", "https://cdn.simpleicons.org/pinterest/8b9bb4"),
    ("Email", "mailto:redwanrashidrico@gmail.com", "https://cdn.simpleicons.org/gmail/8b9bb4"),
]


def main():
    cards = "\n".join(f'  <a href="{url}">{pic("card-" + cid, alt)}</a>' for cid, url, alt in CARDS)
    more = "\n".join(f'  <a href="{url}">{pic("bench-" + mid, alt, "32%")}</a>' for mid, url, alt in MORE)
    stack = "\n".join(f"<tr><td><b>{label}</b></td><td>{icons(ids, alt)}</td></tr>" for label, ids, alt in STACK)
    socials = "&nbsp;&nbsp;\n".join(f'  <a href="{url}"><img alt="{n}" src="{src}" height="22"></a>' for n, url, src in SOCIALS)
    hero_alt = "Redwan Rashid (Ricky), co-founder and Chief Architect of Bohuvuj Softwares: I build software that reaches into hardware."
    milestones_alt = ("Milestones, by first commit: Jun 2025 Purrfect Feeder; Feb 2026 SysTracker; Apr 2026 Bohuvuj Softwares; "
                      "Apr 2026 Perfume Vault; Jul 2026 BeeEzee; Sep 2026 Collectra CMS, live in October; Oct 2026 TimeForge.")
    readme = f"""<a href="https://rico.bd/">
  {pic("hero", hero_alt, "100%")}
</a>

<br>

I like the place where software meets the physical world. Most days that means full-stack apps that real people depend on; other days it is a microcontroller on the desk, a server humming in the corner, or a logo that will not sit right yet.

I co-founded **[Bohuvuj Softwares](https://github.com/Bohuvuj)** and lead its architecture as Chief Architect. Bohuvuj is a small studio in Dhaka that builds web platforms, custom software and mobile apps for teams who mean to still be running them in five years. Most of what is below shipped under Bohuvuj. I also study Computer Science and Engineering at IUBAT, and keep a portfolio at **[rico.bd](https://rico.bd/)**.

<a href="https://github.com/Bohuvuj">
  {pic("bohuvuj", "Bohuvuj Softwares: built to ship, built to last. Web platforms, software, mobile apps and the cloud systems behind them.", "100%")}
</a>

### Now building

<p>
{cards}
</p>

### Milestones

{pic("milestones", milestones_alt, "100%")}

### More from the workbench

<p>
{more}
</p>

### Stack

<table>
{stack}
</table>

### In numbers

<p align="center">
  {stats("card", "border_radius=16&size=compact", "GitHub stats", 'height="176"')}
  {stats("langs", "border_radius=16&layout=compact", "Most used languages", 'height="176"')}
</p>
<p align="center">
  {stats("sparkline", "days=90&width=880&height=140", "Contributions over the last 90 days", 'width="100%"')}
</p>

### Find me

<p>
{socials}
</p>

{pic("footer", "", "100%")}

<p align="center"><img alt="Profile views" src="https://komarev.com/ghpvc/?username=redwan002117&label=visits&color=7c8cff&style=flat-square"></p>

<!-- Generated by tools/build_readme.py; artwork by tools/build_assets.py. -->
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    print("README.md:", len(readme), "chars")


if __name__ == "__main__":
    main()
