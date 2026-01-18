# Config Format

ShellScribe uses YAML as the canonical configuration format. JSON is fully supported as an input format and is treated as an equivalent representation of the same schema.

## Canonical rules
- YAML is the primary authoring format for human-edited configs.
- JSON is accepted anywhere YAML is accepted.
- Internally, configs are normalized to a canonical JSON form for validation and storage.

## Precedence (highest to lowest)
1. CLI flags
2. Environment variables
3. Config file (YAML or JSON)
4. Built-in defaults

## Config file discovery
- If `--config` is provided, it is used.
- Otherwise, search in order: `./shellscribe.yaml`, `./shellscribe.yml`, `./shellscribe.json`.

## Validation
- Config files are validated against JSON Schema.
- Unknown fields are rejected in strict mode and warned in permissive mode.

## Serialization
- All persisted runtime configs are stored as JSON with a schema version.
