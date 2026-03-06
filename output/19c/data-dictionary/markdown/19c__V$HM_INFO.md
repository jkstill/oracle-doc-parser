---
id: 19c__V$HM_INFO
name: V$HM_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-HM_INFO.html
---

# V$HM_INFO

V$HM_INFO displays information about Health Monitor runs, findings, and recommendations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| TYPE | VARCHAR2(14) |  |
| NAME | VARCHAR2(32) |  |
| VALUE | VARCHAR2(513) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The information for a run/finding/recommendation is organized as a name, value pair. If the type of information is RUN , then the data represents the input parameters for that run. If the type of information is FINDING or RECOMMENDATION , then the data represents the information about that particular finding/recommendation.