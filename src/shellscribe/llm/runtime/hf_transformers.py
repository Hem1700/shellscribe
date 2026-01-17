from __future__ import annotations

from .base import LLMResult, LLMRuntime


class HFTransformersRuntime(LLMRuntime):
    def generate(self, prompt: str, **params):
        return LLMResult(text="", metadata={"runtime": "hf_transformers"})
