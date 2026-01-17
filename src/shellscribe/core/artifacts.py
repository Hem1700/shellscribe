from __future__ import annotations

from typing import Optional

from .types import Artifact


class ArtifactStore:
    def add(self, artifact: Artifact) -> None:
        raise NotImplementedError

    def get(self, path: str) -> Optional[Artifact]:
        raise NotImplementedError
