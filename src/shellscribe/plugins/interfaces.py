from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class PluginManifest:
    name: str
    version: str
    tier: str
    targets: List[str] = field(default_factory=list)
    policies: Dict[str, Any] = field(default_factory=dict)
