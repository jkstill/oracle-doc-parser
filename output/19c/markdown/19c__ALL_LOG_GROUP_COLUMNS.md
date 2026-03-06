---
id: 19c__ALL_LOG_GROUP_COLUMNS
name: ALL_LOG_GROUP_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_LOG_GROUP_COLUMNS.html
---

# ALL_LOG_GROUP_COLUMNS

ALL_LOG_GROUP_COLUMNS describes columns that are accessible to the current user and that are specified in log groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the log group definition |
| LOG_GROUP_NAME | VARCHAR2(128) | Name of the log group definition |
| TABLE_NAME | VARCHAR2(128) | Name of the table in which the log group is defined |
| COLUMN_NAME | VARCHAR2(4000) | Name of the column or attribute of the object type column specified in the log group definition |
| POSITION | NUMBER | Original position of the column or attribute in the definition of the object |
| LOGGING_PROPERTY | VARCHAR2(6) | Indicates whether the column or attribute would be supplementally logged ( LOG ) or not ( NO LOG ) |

## Usage Notes

Related Views DBA_LOG_GROUP_COLUMNS describes all columns in the database that are specified in log groups. USER_LOG_GROUP_COLUMNS describes columns that are owned by the current user and that are specified in log groups. See Also: " DBA_LOG_GROUP_COLUMNS " " USER_LOG_GROUP_COLUMNS " See Also: " DBA_LOG_GROUP_COLUMNS " " USER_LOG_GROUP_COLUMNS "