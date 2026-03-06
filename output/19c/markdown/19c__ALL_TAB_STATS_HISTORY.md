---
id: 19c__ALL_TAB_STATS_HISTORY
name: ALL_TAB_STATS_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_TAB_STATS_HISTORY.html
---

# ALL_TAB_STATS_HISTORY

ALL_TAB_STATS_HISTORY provides a history of table statistics modifications for all tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| STATS_UPDATE_TIME | TIMESTAMP(6) WITH TIME ZONE | Time at which the statistics were updated |

## Usage Notes

Related Views DBA_TAB_STATS_HISTORY provides a history of table statistics modifications for all tables in the database. USER_TAB_STATS_HISTORY provides a history of table statistics modifications for all tables owned by the current user. See Also: " DBA_TAB_STATS_HISTORY " " USER_TAB_STATS_HISTORY " See Also: " DBA_TAB_STATS_HISTORY " " USER_TAB_STATS_HISTORY "