---
id: 19c__DBA_AUTO_SEGADV_SUMMARY
name: DBA_AUTO_SEGADV_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTO_SEGADV_SUMMARY.html
---

# DBA_AUTO_SEGADV_SUMMARY

DBA_AUTO_SEGADV_SUMMARY provides a summary of the auto advisor task runs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AUTO_TASKID | NUMBER | Unique auto task ID |
| SNAPID | NUMBER | Maximum AWR snapid used to process the segments |
| SEGMENTS_SELECTED | NUMBER | Number of segments chosen for analysis |
| SEGMENTS_PROCESSED | NUMBER | Number of segments actually processed |
| TABLESPACE_SELECTED | NUMBER | Number of tablespaces chosen for analysis |
| TABLESPACE_PROCESSED | NUMBER | Number of tablespaces actually processed |
| RECOMMENDATIONS_COUNT | NUMBER | Number of recommendations generated |
| START_TIME | TIMESTAMP(6) | Time at which the auto task was started |
| END_TIME | TIMESTAMP(6) | Time at which the auto task ended |