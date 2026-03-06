---
id: 19c__ALL_LOG_GROUPS
name: ALL_LOG_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [all]
source_file: ALL_LOG_GROUPS.html
---

# ALL_LOG_GROUPS

ALL_LOG_GROUPS describes the log group definitions on the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the log group definition |
| LOG_GROUP_NAME | VARCHAR2(128) | Name of the log group definition |
| TABLE_NAME | VARCHAR2(128) | Name of the table on which the log group is defined |
| LOG_GROUP_TYPE | VARCHAR2(28) | Type of the log group: PRIMARY KEY LOGGING UNIQUE KEY LOGGING FOREIGN KEY LOGGING ALL COLUMN LOGGING USER LOG GROUP |
| ALWAYS | VARCHAR2(11) | Y indicates the log group is logged any time a row is updated; N indicates the log group is logged any time a member column is updated |
| GENERATED | VARCHAR2(14) | Indicates whether the name of the supplemental log group was system generated ( GENERATED NAME ) or not ( USER NAME ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_LOG_GROUPS describes the log group definitions on all tables in the database. USER_LOG_GROUPS describes the log group definitions on the tables owned by the current user. See Also: " DBA_LOG_GROUPS " " USER_LOG_GROUPS " See Also: " DBA_LOG_GROUPS " " USER_LOG_GROUPS "