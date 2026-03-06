---
id: 19c__V$HM_RUN
name: V$HM_RUN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HM_RUN.html
---

# V$HM_RUN

V$HM_RUN displays information about all Health Monitor checks and their status.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RUN_ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| CHECK_NAME | VARCHAR2(32) |  |
| RUN_MODE | VARCHAR2(8) |  |
| TIMEOUT | NUMBER |  |
| START_TIME | TIMESTAMP(6) |  |
| LAST_RESUME_TIME | TIMESTAMP(6) |  |
| END_TIME | TIMESTAMP(6) |  |
| MODIFIED_TIME | TIMESTAMP(6) |  |
| STATUS | VARCHAR2(11) |  |
| SRC_INCIDENT | NUMBER |  |
| NUM_INCIDENT | NUMBER |  |
| ERROR_NUMBER | NUMBER |  |
| PROBLEM_ID | NUMBER |  |
| CON_ID | NUMBER |  |