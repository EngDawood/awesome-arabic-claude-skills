#!/usr/bin/env bash
# Commit catalog changes to a branch and open (or update) a pull request.
# Usage: open_catalog_pr.sh <branch> <title> <body>
set -euo pipefail

branch="$1"
title="$2"
body="$3"

git config user.email "github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"

git checkout -B "$branch"
git add -A -- skills commands sources.json skills.json README.md README.en.md

if git diff --cached --quiet; then
  echo "No catalog changes."
  exit 0
fi

git commit -m "$title"
git push --force -u origin "$branch"

if gh pr view "$branch" >/dev/null 2>&1; then
  gh pr edit "$branch" --title "$title" --body "$body"
else
  gh pr create --base main --head "$branch" --title "$title" --body "$body"
fi
