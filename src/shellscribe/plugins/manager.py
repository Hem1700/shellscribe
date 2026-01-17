from __future__ import annotations

from typing import List

from .interfaces import PluginManifest


class PluginManager:
    def __init__(self) -> None:
        self._plugins: List[PluginManifest] = []

    def register(self, manifest: PluginManifest) -> None:
        self._plugins.append(manifest)

    def list(self) -> List[PluginManifest]:
        return list(self._plugins)
