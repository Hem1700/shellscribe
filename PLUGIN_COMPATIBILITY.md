# Plugin Compatibility Policy

## Required plugin metadata
Every plugin must declare the following fields in its manifest:
- plugin_id: globally unique identifier (reverse-DNS or org/name).
- plugin_version: SemVer for the plugin itself.
- core_compat: SemVer range for compatible ShellScribe core versions (e.g., ">=0.2,<1.0").
- schema_compat: minimum schema versions required for any schemas it reads/writes.
- entrypoints: executable entrypoints and their interfaces.

## Compatibility rules
- Core verifies core_compat before loading a plugin.
- Core verifies schema_compat before allowing read/write operations.
- New optional manifest fields may be added in MINOR core releases.
- Breaking changes to manifest schema require MAJOR core bump.

## Deprecation policy
- Core will support a deprecated plugin API for at least 2 MINOR releases.
- Deprecated APIs emit warnings during plugin load.
- Removed APIs require a MAJOR core bump and migration notes.

## Trust and signing (future)
- Optional plugin signing to establish publisher trust.
- Trust policy can allowlist plugin IDs and publisher keys.

## Failure behavior
- Incompatible plugins are rejected with a clear error.
- The core must continue operating without the plugin.
