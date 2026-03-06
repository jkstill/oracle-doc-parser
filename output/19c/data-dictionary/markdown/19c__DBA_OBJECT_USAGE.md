---
id: 19c__DBA_OBJECT_USAGE
name: DBA_OBJECT_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_OBJECT_USAGE.html
---

# DBA_OBJECT_USAGE

DBA_OBJECT_USAGE displays statistics about index usage gathered from the database for all the indexes in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Index owner |
| INDEX_NAME | VARCHAR2(128) | Index name in sys.obj$.name |
| TABLE_NAME | VARCHAR2(128) | Table name in sys.obj$.name |
| MONITORING | VARCHAR2(3) | Indicates whether the monitoring feature is turned on. Possible values: YES NO |
| USED | VARCHAR2(3) | Indicates whether the index has been accessed. Possible values: YES NO |
| START_MONITORING | VARCHAR2(19) | Start monitoring time in sys.object_stats.start_monitoring |
| END_MONITORING | VARCHAR2(19) | End monitoring time in sys.object_stats.end_monitoring |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content You can use this view to monitor index usage. All indexes that have been used at least once can be monitored and displayed in this view. Related View USER_OBJECT_USAGE displays statistics about index usage gathered from the database for the indexes owned by the current user. See Also: " USER_OBJECT_USAGE "