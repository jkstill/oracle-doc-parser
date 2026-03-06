---
id: 19c__V$RSRC_PLAN_HISTORY
name: V$RSRC_PLAN_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_PLAN_HISTORY.html
---

# V$RSRC_PLAN_HISTORY

SEQUENCE#

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEQUENCE# | NUMBER |  |
| ID | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| START_TIME | DATE |  |
| END_TIME | DATE |  |
| ENABLED_BY_SCHEDULER | VARCHAR2(5) |  |
| WINDOW_NAME | VARCHAR2(128) |  |
| ALLOWED_AUTOMATED_SWITCHES | VARCHAR2(5) |  |
| CPU_MANAGED | VARCHAR2(3) |  |
| INSTANCE_CAGING | VARCHAR2(3) |  |
| PARALLEL_EXECUTION_MANAGED | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content