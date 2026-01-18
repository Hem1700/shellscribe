# Threat Model

## Goals
- Protect the host system, target data, and user secrets.
- Prevent unauthorized execution and policy bypass.
- Preserve integrity of artifacts and reports.

## Assumptions
- Users have explicit authorization for all testing.
- Runtime is offline by default (no outbound network).
- Plugins, models, and inputs may be untrusted.

## Assets
- Host system (files, processes, environment).
- Target data and credentials.
- Findings, reports, and evidence artifacts.
- Configuration and policy settings.

## Trust boundaries
- CLI <-> Core runtime
- Core <-> Plugins (entrypoints/manifest)
- Core <-> Model runtime (llama.cpp / HF)
- Core <-> OS tools and process execution
- Core <-> Storage (JSONL / SQLite)
- Imported inputs (reports, artifacts, prompts)

## Threats (STRIDE-style)
- Spoofing: plugin impersonates core or forges provenance.
- Tampering: modify artifacts, logs, or schema payloads.
- Repudiation: insufficient audit trail or missing provenance.
- Information disclosure: secrets in logs, prompts, or reports.
- Denial of service: large inputs, resource exhaustion.
- Elevation of privilege: execution outside policy or sandbox escape.

## Policy bypass risks
- Direct process execution that skips policy checks.
- Plugin calling OS tools without capability tokens.
- Prompt injection attempts to elevate permissions.
- User enabling aggressive mode without explicit acknowledgement.
- Deserialization or schema parsing vulnerabilities.

## Mitigations
- Capability tokens for execution paths.
- Mandatory policy checks before spawning processes.
- Strict schema validation and provenance tracking.
- Artifact hashing and append-only logs.
- Resource limits (timeouts, memory caps, file size limits).
- Explicit consent prompts for destructive actions.
- Clear separation of lab mode vs normal mode.

## Offline constraints
- No live intel; vulnerability data is bundled and verified.
- Updates are manual imports with checksum verification.
- Runtime blocks outbound network by default.

## Residual risks
- Malicious plugins or models with local access.
- User misconfiguration of policy or scope.
- Third-party tool vulnerabilities.

## Open questions
- Required sandboxing tech per platform.
- Plugin signing and trust policy.
- Update cadence and validation for vulnerability data.
