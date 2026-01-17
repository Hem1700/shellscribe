from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class LLMResult:
    text: str
    metadata: Dict[str, Any]


class LLMRuntime:
    def generate(self, prompt: str, **params: Any) -> LLMResult:
        raise NotImplementedError
