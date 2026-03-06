---
id: 19c__DBA_FEATURE_USAGE_STATISTICS
name: DBA_FEATURE_USAGE_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_FEATURE_USAGE_STATISTICS.html
---

# DBA_FEATURE_USAGE_STATISTICS

DBA_FEATURE_USAGE_STATISTICS displays information about database feature usage statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database identifier of the database being tracked |
| NAME | VARCHAR2(64) | Name of the feature |
| VERSION | VARCHAR2(17) | Database version in which the feature was tracked |
| DETECTED_USAGES | NUMBER | Number of times the system has detected usage for the feature |
| TOTAL_SAMPLES | NUMBER | Number of times the system has woken up and checked for feature usage |
| CURRENTLY_USED | VARCHAR2(5) | Indicates whether usage was detected the last time the system checked ( TRUE ) or not ( FALSE ) |
| FIRST_USAGE_DATE | DATE | First sample time the system detected usage of the feature |
| LAST_USAGE_DATE | DATE | Last sample time the system detected usage of the feature |
| AUX_COUNT | NUMBER | This column stores feature-specific usage data in number format. |
| FEATURE_INFO | CLOB | This column stores feature-specific usage data in character format. |
| LAST_SAMPLE_DATE | DATE | The last time the system checked for usage |
| LAST_SAMPLE_PERIOD | NUMBER | Amount of time (in seconds) between the last two usage sample times |
| SAMPLE_INTERVAL | NUMBER | Sample interval |
| DESCRIPTION | VARCHAR2(128) | Description of the feature and usage detection logic |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: Use the following SQL query to list the database features and their descriptions in alphabetical order: SELECT name, description FROM dba_feature_usage_statistics ORDER BY name; Note: Use the following SQL query to list the database features and their descriptions in alphabetical order: SELECT name, description FROM dba_feature_usage_statistics ORDER BY name;