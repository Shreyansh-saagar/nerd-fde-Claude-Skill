# nerd-fde website

This directory contains the standalone promotional website for **nerd-fde**, an independent Forward Deployed Engineer toolkit for Claude Code.

- `index.html`: self-contained, accessible, responsive static website.
- `assets/mascot.png`: Git blob copy of the approved PNG mascot from `/assets/logo.png`.
- `.nojekyll`: disables Jekyll processing when served by GitHub Pages.

## Separation from the Claude plugins

The actual Claude Code plugins are sourced exclusively from `./core`, `./dev`, `./qa`, `./pm`, and `./general` in `.claude-plugin/marketplace.json`. Nothing under `site/` is referenced by those plugin manifests. It is not part of any installed plugin's content.

**Note:** Adding a GitHub marketplace can still clone/cache the source repository, depending on Claude Code's source mechanism; isolating the directory ensures the site does not become a plugin skill/runtime dependency, not that repository transport necessarily excludes its bytes.

## Local preview

Open `site/index.html` in a browser or, from the repository root:

```bash
python3 -m http.server 8000 --directory site
```

Then visit http://localhost:8000.

## GitHub Pages

The workflow `.github/workflows/pages.yml` uploads *only* the `site/` directory, not plugin code.

After reviewing and merging the website PR:

1. In GitHub, go to **Settings → Pages → Build and deployment**, and set **Source: GitHub Actions**.
2. From **Actions**, run **Deploy nerd-fde website** if a push to `main` hasn't already triggered it.
3. When the deployment succeeds, the intended URL is:
   https://shreyansh-saagar.github.io/nerd-fde-Claude-Skill/

The feature branch itself does not automatically become the public Pages site. Do not claim deployment succeeded until GitHub Actions confirms it.
