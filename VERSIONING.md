# Versioning

ShellScribe uses Semantic Versioning (SemVer): MAJOR.MINOR.PATCH.

## Pre-1.0 policy
Until 1.0.0, MINOR releases may include breaking changes; all breaks must be called out in release notes.

## Core (app) version
- MAJOR: breaking changes to CLI flags, config formats, module contracts, or storage formats.
- MINOR: new features or optional fields that remain backward compatible.
- PATCH: bug fixes, performance, and refactors with no behavior changes.
- Pre-releases use labels like 1.2.0-alpha.1, 1.2.0-beta.1, 1.2.0-rc.1.

## Schema versioning
Schemas are versioned independently using SemVer. Each serialized object includes:
- schema_id: stable name (event, task, finding, artifact, target_profile, plugin_manifest).
- schema_version: the SemVer version the object conforms to.

Compatibility rules:
- Same MAJOR: readers must accept newer MINOR/PATCH when new fields are optional.
- Different MAJOR: incompatible unless a migration is provided.
- Schema migrations are documented and versioned alongside releases.

## Storage versioning
- JSONL records include schema_id and schema_version.
- SQLite stores db_schema_version and supports forward migrations only.

## Plugin compatibility
Plugins declare core_compat (SemVer range) and schema_compat when relevant.

## Sources of truth
- Python package version: pyproject.toml.
- C++ core version: cpp/CMakeLists.txt.
- CLI reports the unified core version.
