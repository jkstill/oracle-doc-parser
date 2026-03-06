---
id: 19c__DBA_AUTOTASK_WINDOW_HISTORY
name: DBA_AUTOTASK_WINDOW_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_WINDOW_HISTORY.html
---

# DBA_AUTOTASK_WINDOW_HISTORY

DBA_AUTOTASK_WINDOW_HISTORY displays historical information for automated maintenance task windows.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WINDOW_NAME | VARCHAR2(261) | Name of the maintenance window |
| WINDOW_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Window start time |
| WINDOW_END_TIME | TIMESTAMP(6) WITH TIME ZONE | Window end time |