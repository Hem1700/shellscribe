from __future__ import annotations

from .base import LLMResult, LLMRuntime


class LlamaCppRuntime(LLMRuntime):
    def generate(self, prompt: str, **params):
        return LLMResult(text="", metadata={"runtime": "llama_cpp"})
