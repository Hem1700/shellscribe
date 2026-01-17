from __future__ import annotations

from collections import defaultdict
from typing import Callable, Dict, List

from .types import Event


class EventBus:
    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable[[Event], None]) -> None:
        self._subscribers[event_type].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._subscribers.get(event.type, []):
            handler(event)
