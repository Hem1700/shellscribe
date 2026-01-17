from __future__ import annotations

from typing import List


class MemoryStore:
    def __init__(self) -> None:
        self._items: List[str] = []

    def add(self, item: str) -> None:
        self._items.append(item)

    def recent(self, n: int = 5) -> List[str]:
        return self._items[-n:]
