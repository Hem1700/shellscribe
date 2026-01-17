from __future__ import annotations

from typing import Iterable, Optional

from .types import Event, Finding


class StateStore:
    def add_event(self, event: Event) -> None:
        raise NotImplementedError

    def add_finding(self, finding: Finding) -> None:
        raise NotImplementedError

    def get_findings(self) -> Iterable[Finding]:
        raise NotImplementedError
