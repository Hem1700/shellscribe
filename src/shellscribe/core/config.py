from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ShellScribeConfig:
    offline: bool = True
    dry_run: bool = True
    allowlist: List[str] = field(default_factory=list)
    llm_runtime: str = "llama_cpp"
    storage: Dict[str, Any] = field(default_factory=lambda: {"runs_dir": "runs/"})
