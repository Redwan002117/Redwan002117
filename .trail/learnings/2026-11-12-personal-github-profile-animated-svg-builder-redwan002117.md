---
title: Personal GitHub profile animated SVG builder tools/build_assets.py
author: Redwan002117
date: 2026-11-12
branch: main
id: l-0c7d523e
scope: repo
status: active
src: agent
touches:
  - tools/build_assets.py
  - tools/build_readme.py
---

## Decided
tools/build_assets.py deterministically builds dark/light assets/*.svg (hero, milestones, footer, bohuvuj, linkedin, card-*, bench-*) with Lucide icons, system font stacks, seeded stars(), and reduced-motion rules; build_readme.py compiles README.md.

## Tried and ruled out
Non-deterministic random star positions or external CSS/JS dependencies that break GitHub camo proxying or create noisy SVG diffs.

## Watch out
Keep star RNG seed fixed (seed=7) and test both light and dark GitHub themes after regenerating assets.
