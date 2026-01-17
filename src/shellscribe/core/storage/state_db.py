from __future__ import annotations

from typing import Iterable

from ..types import Finding


class SQLiteStateDB:
    def __init__(self, path: str) -> None:
        self.path = path

    def add_finding(self, finding: Finding) -> None:
        raise NotImplementedError

    def list_findings(self) -> Iterable[Finding]:
        raise NotImplementedError
