# MMA Vietnam Claude Handbook

Static documentation site built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Source of truth for how the MMA team uses Claude.

## Run locally

You need Python 3.10 or later.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 in a browser. The site auto-rebuilds when you save a file.

## Add or edit a page

1. Create or edit a file in `docs/` (e.g., `docs/new-topic.md`).
2. If it is a new page, add it to the `nav:` section in `mkdocs.yml`.
3. Preview locally with `mkdocs serve`.
4. Commit and push. GitHub Actions publishes the updated site.

## Brand assets

Drop an MMA logo PNG at `docs/assets/mma-logo.png` and a favicon at `docs/assets/favicon.png`, then uncomment the `logo:` and `favicon:` lines in `mkdocs.yml`.

Brand colours are applied in `docs/stylesheets/extra.css`.

## Publish to GitHub Pages

1. Repo pushed to: https://github.com/YenJLe/mmavn-claude-handbook
2. In the GitHub repo settings: Pages → Source → GitHub Actions (one-time setup).
3. The workflow at `.github/workflows/deploy.yml` publishes on every push to `main`.

The live URL is: https://yenjle.github.io/mmavn-claude-handbook/

## File layout

```
mmavn-claude-handbook/
  mkdocs.yml              # site config
  requirements.txt        # Python dependencies
  .github/workflows/
    deploy.yml            # GitHub Actions deploy
  docs/
    index.md              # Home
    claude-101.md         # What Claude is + comparisons + features
    getting-access.md     # Install and login
    desktop-tour.md       # App walkthrough
    prompting.md          # Prompting basics
    use-cases.md          # Role-specific examples
    assets/               # Logos, favicons, screenshots
    stylesheets/
      extra.css           # MMA brand styling
```
