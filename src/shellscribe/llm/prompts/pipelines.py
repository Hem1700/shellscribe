from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List

from ..runtime.base import LLMRuntime, LLMResult


@dataclass
class PromptStage:
    name: str
    handler: Callable[[str], str]


class PromptPipeline:
    def __init__(self, runtime: LLMRuntime, stages: List[PromptStage]) -> None:
        self.runtime = runtime
        self.stages = stages

    def run(self, prompt: str) -> LLMResult:
        current = prompt
        for stage in self.stages:
            current = stage.handler(current)
        return self.runtime.generate(current)
