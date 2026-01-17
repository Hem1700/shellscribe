from __future__ import annotations

from typing import Iterable

from .config import ShellScribeConfig
from .event_bus import EventBus
from .policy import PolicyEngine
from .types import Event, TaskSpec


class Orchestrator:
    def __init__(self, config: ShellScribeConfig, bus: EventBus, policy: PolicyEngine) -> None:
        self.config = config
        self.bus = bus
        self.policy = policy

    def submit_task(self, task: TaskSpec) -> None:
        decision = self.policy.check(task)
        event = Event(
            type="TaskProposed",
            timestamp="",
            run_id="",
            payload={"task": task.__dict__, "decision": decision.__dict__},
        )
        self.bus.publish(event)

    def run(self) -> Iterable[Event]:
        # Placeholder run loop
        return []
