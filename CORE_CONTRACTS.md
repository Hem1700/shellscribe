# Core Contracts

This document defines the core data contracts shared across the system. These are implemented as JSON Schemas in `schemas/`.

## TaskSpec
Represents a unit of work to be performed by a module.
- Fields: task_id, module, objective, params, policy_context, target_ref, created_at

## Event
Represents a structured runtime signal.
- Fields: event_id, type, timestamp, run_id, payload, provenance

## Finding
Represents a security issue or observation.
- Fields: finding_id, title, severity, confidence, target_refs, evidence_refs, description, remediation, provenance, timestamps

## Artifact
Represents a persisted output.
- Fields: artifact_id, path, checksum, mime, source, created_at, provenance

## TargetProfile
Represents the subject of testing.
- Fields: target_id, type, inputs, scope, credentials, policy_flags, created_at

## Notes
- Each contract includes schema_id and schema_version.
- Schema versions follow SemVer; see `VERSIONING.md`.
