# Team Git Guardrails — The Grateful Team Website

These rules are mandatory for all contributors.

## Goal

Prevent accidental pushes and keep `main` stable.

## Required Daily Workflow

1. **Sync `main` first**
   ```bash
   git checkout main
   git pull --ff-only origin main
   ```

2. **Work from your own branch**
   ```bash
   git checkout <your-branch>
   git merge main
   ```
   Use your own branch name (for example: `luis`, `jackson-changes`).

3. **Before commit, verify exactly what is changing**
   ```bash
   git status
   git diff
   ```

4. **Stage only intended files**
   ```bash
   git add <file-a> <file-b>
   ```
   Avoid `git add .` unless you are certain everything shown should be committed.

5. **Commit with a clear message**
   ```bash
   git commit -m "Explain why this change is needed"
   ```

6. **Push only to your branch**
   ```bash
   git push origin <your-branch>
   ```

## Hard Rules

- Never push directly to `main`.
- Never force-push to `main`.
- Never commit editor settings, local configs, or secrets.
- Keep personal notes in `RULES.local.md` (local-only, never committed).

## Local Dev Server Rule (AI and Humans)

Before testing any UI/content/code change locally:

1. Check whether a local dev server is already running.
2. If one is running, stop/kill it first.
3. Start exactly one fresh local server.
4. Confirm which localhost URL/port is active.
5. Validate changes on that active URL only.

Do not leave multiple servers running on different ports, because this can make changes appear "broken" when you are viewing an outdated process.

## Pull Request Checklist

Before opening or merging a PR:

- `git status` shows only intended files changed.
- Diff does not include local-only files.
- Changes are tested quickly in browser for obvious breakages.
- PR targets `main` from your branch.
