---
id: 19c__V$HM_RECOMMENDATION
name: V$HM_RECOMMENDATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HM_RECOMMENDATION.html
---

# V$HM_RECOMMENDATION

V$HM_RECOMMENDATION displays information about all the recommendations made to various Health Monitor findings.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECOMMENDATION_ID | NUMBER |  |
| FDG_ID | NUMBER |  |
| RUN_ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| TYPE | VARCHAR2(7) |  |
| RANK | NUMBER |  |
| TIME_DETECTED | TIMESTAMP(6) |  |
| EXECUTED | TIMESTAMP(6) |  |
| STATUS | VARCHAR2(7) |  |
| DESCRIPTION | VARCHAR2(1024) |  |
| REPAIR_SCRIPT | VARCHAR2(512) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content