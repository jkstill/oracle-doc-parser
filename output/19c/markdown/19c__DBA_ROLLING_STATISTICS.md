---
id: 19c__DBA_ROLLING_STATISTICS
name: DBA_ROLLING_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_ROLLING_STATISTICS.html
---

# DBA_ROLLING_STATISTICS

DBA_ROLLING_STATISTICS provides a list of rolling operation statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(256) | Name of the statistic. Possible values: DBMS_ROLLING execution time logical to primary switchover finish time primary services offline for primary to logical switchover start time rolling upgrade finish time rolling upgrade start time time for former primary to fully recover upgrade redo time for former primary to start upgrade redo recovery total time former primary in physical role transient logical creation finish time transient logical creation start time transient logical protection finish time transient logical protection start time user upgrade time |
| VALUE | VARCHAR2(256) | Value of the statistic |
| UPDATE_TIME | TIMESTAMP(6) | Time of last update |

## Usage Notes

See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations. See Also: Oracle Data Guard Concepts and Administration for more information about rolling operations.