# ShellScribe Architecture (v0.1)

**Intent:** This document describes the system architecture for ShellScribe, an offline‑first, library‑centric framework for **authorized** security testing and research. It complements `DESIGN_DOC.md` by focusing on structure, boundaries, and data flow.

---

## 1) Architectural Principles

- **Offline‑first:** no network egress by default; all inference and analysis is local.
- **Policy‑gated execution:** every action passes through policy checks and approvals.
- **Evidence‑bound outputs:** all findings and reports must reference captured artifacts.
- **Reproducible runs:** deterministic execution where possible; replayable event logs.
- **Modular by design:** modules communicate via events; plugins extend capabilities.

---

## 2) System Context (ANSI)

```text
                                     ┌──────────────────────────────┐
                                     │          ShellScribe          │
                                     │  Offline Offensive Framework  │
                                     └──────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Library API (Python)     CLI (shellscribe)               Local UI (opt)  │
  └──────────────────────────────────────────────────────────────────────────┘
                       │                         │                      │
                       └───────────────┬─────────┴───────────┬──────────┘
                                       │                     │
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                              Core Runtime                                │
  │  ┌────────────┐   ┌────────────┐   ┌─────────────┐   ┌─────────────────┐ │
  │  │Orchestrator│<->│  Event Bus │<->│ Policy/Scope│<->│  State + Store   │ │
  │  └────────────┘   └────────────┘   └─────────────┘   │ JSONL + SQLite   │ │
  │          │                 │               │         └─────────────────┘ │
  │          │                 │               │                   │         │
  └──────────┼─────────────────┼───────────────┼───────────────────┼─────────┘
             │                 │               │                   │
  ┌──────────▼─────────┐  ┌────▼─────┐   ┌──────▼─────┐      ┌─────▼─────────┐
  │  Modules           │  │  LLM     │   │   ML       │      │  Plugin       │
  │  - Recon           │  │ Adapter  │   │ Utilities  │      │  Manager      │
  │  - Fuzzing         │  │  - llama │   │ - triage   │      │ (entrypoints  │
  │  - Scaffold        │  │  - HF    │   │ - ranking  │      │ + manifests)  │
  │  - Emulation       │  │ Pipelines│   │ - cluster  │      └───────────────┘
  │  - Reporting       │  │          │   │            │
  │  - Report Ingest   │  │          │   │            │
  │  - Plan Synth      │  │          │   │            │
  └────────────────────┘  └──────────┘   └────────────┘
             │
             ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                              Artifacts                                    │
  │  Evidence bundles, repro inputs, logs, reports, generated outputs         │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## 3) Core Runtime (Component View)

### 3.1 Orchestrator
**Role:** central run loop, task scheduling, state updates, reporting triggers.  
**Responsibilities:** policy enforcement, module coordination, replay support.

### 3.2 Event Bus
**Role:** async pub/sub channel connecting modules and core services.  
**Responsibilities:** event routing, backpressure handling, schema validation hooks.

### 3.3 Policy/Scope Engine
**Role:** authorization boundary.  
**Responsibilities:** allowlist enforcement, dry‑run handling, approvals, rate limits.

### 3.4 State + Artifact Store
**Role:** durable, replayable record of all runs.  
**Responsibilities:** JSONL event log, SQLite index, artifact storage and checksums.

### 3.5 Plugin Manager
**Role:** discover, load, and validate external capabilities.  
**Responsibilities:** entrypoint discovery, manifest validation, optional sandboxing.

---

## 4) Target Profiles & Capability Routing

ShellScribe supports multiple target types through a **TargetProfile** abstraction.

**Target types**
- Codebase, Package/Library, Website/Web App, API, Mobile App, Network Service

**Routing rules**
- Each module declares supported target types and required inputs.
- The orchestrator selects only compatible modules and logs skips explicitly.

---

## 5) LLM Integration Architecture

### 5.1 Runtime Adapters
- **llama.cpp** for GGUF models
- **HF Transformers** with offline weights
- Adapters are pluggable via the plugin system

### 5.2 Prompt Pipelines (LLM‑assisted)
- **Planner:** propose next high‑level step
- **Translator:** map to structured tasks
- **Verifier:** sanity check and policy alignment
- **Summarizer:** store durable memory

### 5.3 Report‑Driven Planning
LLM consumes prior reports to propose a **high‑level plan** (tasks only):
- Report ingestion → scope + findings
- Gap analysis → missing coverage
- Plan synthesis → task graph (policy‑gated)

LLM never executes actions directly.

---

## 6) ML Utilities (Optional)

Lightweight ML utilities emit events:
- Crash clustering/deduplication
- Finding ranking/prioritization
- Anomaly detection in telemetry

ML output is advisory and always policy‑gated.

---

## 7) Data Model (High‑Level)

**Run**  
`id, timestamps, config, environment metadata`

**TargetProfile**  
`type, inputs, scope, credentials`

**TaskSpec**  
`module, objective, params, policy context`

**Event**  
`type, timestamp, payload, provenance`

**Finding**  
`id, severity, confidence, evidence refs`

**Artifact**  
`path, checksum, provenance`

---

## 8) Data Flow (Execution Loop)

```text
TargetProfile -> Orchestrator -> Policy Check -> Module Execution
         |             |               |                |
         |             v               v                v
         |          Events --------> Event Bus -----> Artifacts
         |             |                               |
         └------> State Store (SQLite + JSONL) <--------┘
```

**Guarantees**
- All actions pass policy check.
- All outputs are logged and reproducible.

---

## 9) Report‑Driven Pentest Flow (High‑Level)

```text
Prior Report -> Report Ingest -> LLM Gap/Plan -> Policy Gate -> Modules
       |                                |                     |
       v                                v                     v
  Structured Scope                Task Graph            Evidence Artifacts
       \______________________________|__________________________/
                                      v
                             Evidence‑Bound Report
```

---

## 10) Storage Layout (Run‑Scoped)

```
runs/<run_id>/
  events.jsonl         # full event timeline
  state.db             # SQLite state snapshot
  artifacts/           # evidence, repro inputs, logs
  reports/             # markdown + JSON exports
```

---

## 11) Safety & Controls

- **Default dry‑run** and explicit approvals.
- **Allowlist required** for all targets.
- **Offline execution enforced**.
- **Evidence‑bound reporting**; no unsupported claims.

---

## 12) Extensibility

Plugins can contribute:
- New modules
- Tool wrappers
- Prompt packs
- Model runtimes
- Technique packs

Each plugin includes a manifest with metadata, policy tags, and compatibility info.

### Capability tiers & trust levels

**Capability tiers**
- **Tier 0 — Passive/Read‑only**
- **Tier 1 — Active/Safe**
- **Tier 2 — High‑risk/External (explicit enablement required)**

**Trust levels**
- **Core (first‑party):** Tier 0/1 only
- **Verified (partner):** audited + signed manifest
- **Third‑party:** explicit enablement + strict policy gates

**Policy gates (example)**
- Tier 0: allowlist + offline required
- Tier 1: allowlist + approvals + rate limits
- Tier 2: explicit enablement + approvals + lab mode + audit logging

---

## 13) Performance & Scaling (Future)

- High‑throughput event bus with backpressure support.
- C++ core for performance‑critical modules.
- Distributed offline execution (agent pool + shared artifacts).

---

## 14) Decisions & Open Questions

### Decisions (current)
- **Report formats (phase 1):** Markdown + JSON.
- **Lab mode defaults:** approvals optional; dry‑run OFF; allowlist + offline still enforced; any online intel sync must be explicit and logged.
- **Findings schema:** baseline required fields (id/title/severity/confidence/targets/evidence refs/provenance/timestamps) plus extensible metadata.
- **C++ core:** required (not optional at build time).

### Open Questions
- Which tools are allowed as first‑party plugins?
