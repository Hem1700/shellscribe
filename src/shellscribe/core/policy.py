from __future__ import annotations

from .types import PolicyDecision, TaskSpec


class PolicyEngine:
    def __init__(self, allowlist: list[str] | None = None, dry_run: bool = True) -> None:
        self.allowlist = allowlist or []
        self.dry_run = dry_run

    def check(self, task: TaskSpec) -> PolicyDecision:
        # Placeholder policy: allow by default, require approval if not dry-run.
        return PolicyDecision(allowed=True, requires_approval=not self.dry_run)
