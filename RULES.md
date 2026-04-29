# Workflow Rules — The Grateful Team Website

These rules are mandatory and must never be deviated from.

## Repository

- GitHub repo: https://github.com/jmaitner/the-grateful-team-website

## Required Workflow (Every Single Change)

1. **Pull latest main** — Before touching any file, switch to `main` and pull the most recent copy:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Switch to `luis`** — All work happens on the `luis` branch only:
   ```bash
   git checkout luis
   git merge main   # bring luis up to date with main
   ```

3. **Make changes** — Edit files on the `luis` branch.

4. **Push to `luis`** — Always push to `luis`, never to any other branch:
   ```bash
   git push origin luis
   ```

## Branch Rules

- **Never create new branches.** The only branches to use are `main` (read-only, source of truth) and `luis` (the working branch for all changes).
- **Never push directly to `main`.**
- **Always push to `luis`.**
