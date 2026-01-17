from __future__ import annotations

from typing import Iterable

from ..core.types import Event, TaskSpec


class Module:
    name = "base"

    def initialize(self, ctx) -> None:
        pass

    def on_event(self, event: Event) -> None:
        pass

    def handle_task(self, task: TaskSpec) -> Iterable[Event]:
        return []
