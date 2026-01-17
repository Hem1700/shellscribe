from __future__ import annotations

from typing import Iterable

from ..types import Event


class JsonlEventLog:
    def __init__(self, path: str) -> None:
        self.path = path

    def append(self, event: Event) -> None:
        raise NotImplementedError

    def read_all(self) -> Iterable[Event]:
        raise NotImplementedError
