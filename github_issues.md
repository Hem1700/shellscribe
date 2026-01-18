# GitHub Issues Import

This file set was generated from `TODO.md`.

## Files
- `github_issues.csv` — importable CSV for GitHub Issues

## Import options
1) GitHub UI: open your repo → Issues → Import (CSV).
2) GitHub CLI (if installed):
   `gh issue import github_issues.csv --repo <owner>/<repo>`

## Labels
CSV includes a `phase:M#` label per issue. Create these labels first
(or let GitHub create them on import, if supported).

Total issues: 120