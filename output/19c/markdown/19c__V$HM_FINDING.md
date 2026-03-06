---
id: 19c__V$HM_FINDING
name: V$HM_FINDING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HM_FINDING.html
---

# V$HM_FINDING

V$HM_FINDING displays information about all the findings of various Health Monitor runs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FINDING_ID | NUMBER |  |
| RUN_ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| PARENT_ID | NUMBER |  |
| CHILD_COUNT | NUMBER |  |
| CLASS_NAME | VARCHAR2(32) |  |
| TIME_DETECTED | TIMESTAMP(6) |  |
| MODIFIED | TIMESTAMP(6) |  |
| PRIORITY | VARCHAR2(8) |  |
| STATUS | VARCHAR2(12) |  |
| TYPE | VARCHAR2(13) |  |
| DESCRIPTION | VARCHAR2(1024) |  |
| DAMAGE_DESCRIPTION | VARCHAR2(1024) |  |
| CON_ID | NUMBER |  |