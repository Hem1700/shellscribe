# ShellScribe TODO List (Detailed)

This is a comprehensive, phase‑based build plan for ShellScribe.

---

## Phase M0 — Foundation & Governance
- M0‑01: Create repo skeleton with `src/`, `cli/`, `docs/`, `tests/`, `examples/`, `cpp/`, `schemas/`.
- M0‑02: Add MIT license, CODE_OF_CONDUCT, SECURITY.md, CONTRIBUTING.md.
- M0‑03: Define versioning strategy (SemVer + schema versioning).
- M0‑04: Define threat model document (offline constraints, policy bypass risks).
- M0‑05: Add project glossary (target types, module, task, event, artifact).
- M0‑06: Define compatibility policy for plugins (min core version, deprecation policy).
- M0‑07: Decide canonical config format (YAML + JSON).
- M0‑08: Create “core contracts” doc (TaskSpec, Event, Finding, TargetProfile, Artifact).

## Phase M1 — Schemas & Contracts
- M1‑01: Define Event schema (type, timestamp, run_id, payload, provenance).
- M1‑02: Define TaskSpec schema (module, objective, params, policy_context).
- M1‑03: Define Finding schema baseline (id, title, severity, confidence, target refs, evidence refs, provenance, timestamps).
- M1‑04: Define Artifact schema (path, checksum, mime, source, created_at).
- M1‑05: Define TargetProfile schema (type, inputs, scope, credentials, policy flags).
- M1‑06: Implement JSON schema validation for all core entities.
- M1‑07: Add schema version bump rules + migration strategy.

## Phase M2 — Core Runtime Spine
- M2‑01: Build Event Bus interface (publish/subscribe, filters, backpressure).
- M2‑02: Implement Orchestrator run loop (task queue, state transitions).
- M2‑03: Implement Policy Engine skeleton (allowlist, dry‑run, approvals).
- M2‑04: Build State Store interface (CRUD for targets, tasks, findings).
- M2‑05: Build Artifact Store interface (write/read, checksums, retention).
- M2‑06: Implement run lifecycle (init → run → finalize → report).
- M2‑07: Implement replay mechanism from `events.jsonl`.
- M2‑08: Add audit log entry for every policy decision.

## Phase M3 — Storage & Persistence
- M3‑01: Implement JSONL event log writer/reader.
- M3‑02: Implement SQLite state schema + migrations.
- M3‑03: Link events to state updates (projection logic).
- M3‑04: Build “run export” bundle (events + state + artifacts).
- M3‑05: Add artifact integrity validation (checksums + manifest).
- M3‑06: Add query helpers (findings by severity, targets by type).

## Phase M4 — C++ Core Required
- M4‑01: Create `cpp/` with CMake build setup.
- M4‑02: Define C++ core API boundaries (event emitter, task executor hooks).
- M4‑03: Add pybind11 bindings to expose C++ core to Python.
- M4‑04: Add build matrix for Linux + macOS.
- M4‑05: Add CI build validation for C++ core.
- M4‑06: Implement at least one performance‑critical path in C++ (e.g., event buffer).

## Phase M5 — Plugin System
- M5‑01: Define plugin manifest schema (name, version, tier, targets, policies).
- M5‑02: Implement Python entrypoint discovery.
- M5‑03: Implement manifest validation and compatibility checks.
- M5‑04: Implement trust levels (Core/Verified/Third‑party).
- M5‑05: Implement capability tier gating (Tier 0/1/2).
- M5‑06: Add sandboxing hooks (process isolation, resource limits).
- M5‑07: Add plugin registry index (local file‑based).

## Phase M6 — CLI (Reference Client)
- M6‑01: `shellscribe project init` (scaffold config and folders).
- M6‑02: `shellscribe config set/get` (YAML/JSON config support).
- M6‑03: `shellscribe policy allowlist add/remove/list`.
- M6‑04: `shellscribe run scenario <name>` (policy‑gated).
- M6‑05: `shellscribe replay <run_id>`.
- M6‑06: `shellscribe report <run_id> --format md|json`.
- M6‑07: `shellscribe plugins list|enable|disable`.
- M6‑08: Add interactive approval prompts (lab mode toggle).

## Phase M7 — LLM Integration
- M7‑01: Implement llama.cpp runtime adapter (offline GGUF).
- M7‑02: Implement HF Transformers adapter (offline weights).
- M7‑03: Build prompt pipeline engine (planner → translator → verifier → summarizer).
- M7‑04: Build context/memory store (short‑term + long‑term summaries).
- M7‑05: Add safety verifier to enforce policy alignment.
- M7‑06: Add prompt pack system (versioned templates).
- M7‑07: Add offline model registry + config validation.

## Phase M8 — Report‑Driven Pentest Mode
- M8‑01: Report Ingestion module (Markdown + JSON first).
- M8‑02: Report normalization into structured scope + findings.
- M8‑03: LLM gap analysis (coverage gaps, unclear evidence).
- M8‑04: LLM plan synthesis (tasks only).
- M8‑05: Evidence consistency checker (no unsupported claims).
- M8‑06: Report composer (evidence‑bound, templated).
- M8‑07: Add “delta report” mode vs prior report.

## Phase M9 — Core Modules (Baseline)
- M9‑01: Recon module skeleton (asset/service normalization).
- M9‑02: Fuzzing module skeleton (lab‑safe, controlled).
- M9‑03: Exploit scaffold module (research notes only, non‑operational).
- M9‑04: Emulation/scenario engine (technique graphs + checkpoints).
- M9‑05: Reporting module (MD + JSON output, evidence bundling).
- M9‑06: Add module capability declarations (target types + inputs).
- M9‑07: Add module‑level resource limits (CPU/mem/time).

## Phase M10 — Pentest‑Focused Module Pack
- M10‑01: Asset Inventory module (normalize all targets into graph).
- M10‑02: Service Fingerprint module (passive metadata).
- M10‑03: Web/App Mapper module (routes/params inventory).
- M10‑04: API Surface Mapper module (OpenAPI ingestion).
- M10‑05: Config Posture module (TLS/headers/safe defaults).
- M10‑06: Auth Flow Analyzer module (session/token lifecycle modeling).
- M10‑07: Role/Permission Graph module (policy mapping).
- M10‑08: Input Robustness module (boundary/type checks, non‑destructive).
- M10‑09: Evidence Bundler module (consistent artifact packaging).
- M10‑10: Redaction module (sanitize sensitive artifacts).
- M10‑11: Finding Correlator module (dedupe + merge related signals).

## Phase M11 — ML Utilities
- M11‑01: Crash clustering pipeline (signature + similarity).
- M11‑02: Finding ranking (risk + confidence + relevance).
- M11‑03: Anomaly detector for telemetry (lab‑only).
- M11‑04: ML output events + state updates.
- M11‑05: ML evaluation harness (precision/recall on sample data).

## Phase M12 — Safety & Policy Hardening
- M12‑01: Offline enforcement (deny network unless explicitly enabled).
- M12‑02: Policy profiles (lab, strict, audit‑only).
- M12‑03: Approval policies (auto‑approve in lab, manual elsewhere).
- M12‑04: Audit trail for every action.
- M12‑05: Evidence provenance enforcement (all findings must reference artifacts).

## Phase M13 — UI (Optional, Local)
- M13‑01: Timeline view (events + approvals).
- M13‑02: Task graph view (scenario steps).
- M13‑03: Findings + evidence viewer.
- M13‑04: Policy status panel (offline, allowlist, approvals).
- M13‑05: UI uses same APIs; no bypass paths.

## Phase M14 — Distributed Offline Execution (Future)
- M14‑01: Agent pool manager (local cluster).
- M14‑02: Work queue + scheduling policy.
- M14‑03: Shared artifact storage interface.
- M14‑04: Deterministic replay across nodes.
- M14‑05: Cross‑node policy enforcement.

## Phase M15 — Testing & CI
- M15‑01: Unit tests for policy + schemas.
- M15‑02: Unit tests for prompt pipelines + adapters.
- M15‑03: Integration tests for end‑to‑end run.
- M15‑04: Replay determinism tests.
- M15‑05: Offline enforcement tests (no outbound calls).
- M15‑06: Plugin compatibility tests.
- M15‑07: C++ core build tests (Linux + macOS).
- M15‑08: Golden run fixtures with expected outputs.

## Phase M16 — Docs & Examples
- M16‑01: Quickstart guide (offline setup).
- M16‑02: Target Profile guide (codebase, web, API, mobile).
- M16‑03: Plugin authoring guide (manifest + capability tiers).
- M16‑04: Policy configuration guide.
- M16‑05: Report templates + schema docs.
- M16‑06: Example scenarios and sample reports.

## Phase M17 — Release Engineering
- M17‑01: Packaging strategy (PyPI + native wheels).
- M17‑02: Versioned migration scripts for SQLite schema.
- M17‑03: Release checklist (tests, docs, compatibility).
- M17‑04: Artifact signing policy (optional).
