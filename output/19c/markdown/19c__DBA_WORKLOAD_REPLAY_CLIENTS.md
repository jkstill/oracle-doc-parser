---
id: 19c__DBA_WORKLOAD_REPLAY_CLIENTS
name: DBA_WORKLOAD_REPLAY_CLIENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_REPLAY_CLIENTS.html
---

# DBA_WORKLOAD_REPLAY_CLIENTS

DBA_WORKLOAD_REPLAY_CLIENTS displays all workload replay clients and their assigned instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WRC_ID | NUMBER(38) | The identifier of a workload replay client |
| SCHEDULE_CAP_ID | NUMBER(38) | A unique identifier for a workload capture added to a replay schedule. 0 for a non-consolidated replay |
| INSTANCE_NUMBER | NUMBER(38) | The instance that the replay client connects to |