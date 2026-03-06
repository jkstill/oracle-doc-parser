---
id: 19c__V$ADVISOR_PROGRESS
name: V$ADVISOR_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ADVISOR_PROGRESS.html
---

# V$ADVISOR_PROGRESS

V$ADVISOR_PROGRESS displays information about the progress of advisor execution.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| USERNAME | VARCHAR2(128) |  |
| OPNAME | VARCHAR2(64) |  |
| ADVISOR_NAME | VARCHAR2(64) |  |
| TASK_ID | NUMBER |  |
| TARGET_DESC | VARCHAR2(32) |  |
| SOFAR | NUMBER |  |
| TOTALWORK | NUMBER |  |
| UNITS | VARCHAR2(32) |  |
| BENEFIT_SOFAR | NUMBER |  |
| BENEFIT_MAX | NUMBER |  |
| FINDINGS | NUMBER |  |
| RECOMMENDATIONS | NUMBER |  |
| TIME_REMAINING | NUMBER |  |
| START_TIME | DATE |  |
| LAST_UPDATE_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| ADVISOR_METRIC1 | NUMBER |  |
| METRIC1_DESC | VARCHAR2(64) |  |
| EXECUTION_TYPE | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content