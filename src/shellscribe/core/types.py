from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TargetProfile:
    target_type: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    scope: Dict[str, Any] = field(default_factory=dict)
    credentials: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskSpec:
    module: str
    objective: str
    params: Dict[str, Any] = field(default_factory=dict)
    policy_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Event:
    type: str
    timestamp: str
    run_id: str
    payload: Dict[str, Any]
    provenance: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Finding:
    id: str
    title: str
    severity: str
    confidence: str
    targets: List[str] = field(default_factory=list)
    evidence: List[str] = field(default_factory=list)
    provenance: Dict[str, Any] = field(default_factory=dict)
    timestamps: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Artifact:
    path: str
    checksum: str
    mime: Optional[str] = None
    source: Optional[str] = None
    created_at: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PolicyDecision:
    allowed: bool
    reason: str = ""
    requires_approval: bool = False
