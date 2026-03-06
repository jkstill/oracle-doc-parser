---
id: 19c__DBA_WORKLOAD_ACTIVE_USER_MAP
name: DBA_WORKLOAD_ACTIVE_USER_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_WORKLOAD_ACTIVE_USER_MAP.html
---

# DBA_WORKLOAD_ACTIVE_USER_MAP

DBA_WORKLOAD_ACTIVE_USER_MAP contains the mappings that are going to be valid for the next replay or are valid for the current replay.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEDULE_CAP_ID | NUMBER | The ID of a capture in the schedule |
| CAPTURE_USER | VARCHAR2(4000) | The user name during the time of the workload capture |
| REPLAY_USER | VARCHAR2(4000) | The user name to which captured user should be remapped during replay |