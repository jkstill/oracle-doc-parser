---
id: 19c__V$DATAGUARD_STATUS
name: V$DATAGUARD_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-DATAGUARD_STATUS.html
---

# V$DATAGUARD_STATUS

V$DATAGUARD_STATUS displays messages recently written to the alert log or server process trace files that concern physical standby databases or redo transport services for all standby database types.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FACILITY | VARCHAR2(24) |  |
| SEVERITY | VARCHAR2(13) |  |
| DEST_ID | NUMBER |  |
| MESSAGE_NUM | NUMBER |  |
| ERROR_CODE | NUMBER |  |
| CALLOUT | VARCHAR2(3) |  |
| TIMESTAMP | DATE |  |
| MESSAGE | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |