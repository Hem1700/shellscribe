# Glossary

- Artifact: A persisted output produced during a run (e.g., logs, evidence bundles, generated files). Stored with metadata like path, checksum, mime, and provenance.
- Event: A structured runtime signal emitted by the core (e.g., task started, tool invoked, finding created). Used for auditing and orchestration.
- Finding: A structured security issue with severity, confidence, evidence references, and provenance.
- Module: A functional unit that performs a class of tasks (e.g., recon, static analysis, dependency analysis, report generation).
- Policy: Rules that govern what actions are allowed (e.g., execution, network access, file access) and under what conditions.
- Provenance: Metadata that records the origin of data (source, time, tool, model, operator) to support auditability.
- Task / TaskSpec: A declarative description of work to be done by a module, including objective, parameters, and policy context.
- Target: The subject of testing (repo, package, service, web app, mobile app, binary, container, etc.).
- TargetProfile: The structured description of a target (type, inputs, scope, credentials, policy flags).
- Plugin: An external module that extends core capabilities, packaged with a manifest and compatibility metadata.
- Run: A single orchestrated execution session with a unique run_id and scoped configuration.
- Store: The persistence layer for events, findings, artifacts, and run metadata (JSONL and/or SQLite).
