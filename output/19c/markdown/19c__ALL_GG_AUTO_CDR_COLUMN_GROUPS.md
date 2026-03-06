---
id: 19c__ALL_GG_AUTO_CDR_COLUMN_GROUPS
name: ALL_GG_AUTO_CDR_COLUMN_GROUPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_GG_AUTO_CDR_COLUMN_GROUPS.html
---

# ALL_GG_AUTO_CDR_COLUMN_GROUPS

ALL_GG_AUTO_CDR_COLUMN_GROUPS provides details about Oracle GoldenGate automatic conflict detection and resolution (CDR) column groups owned by the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Table name |
| COLUMN_GROUP_NAME | VARCHAR2(128) | Column group name |
| RESOLUTION_COLUMN | VARCHAR2(128) | Timestamp resolution column |

## Usage Notes

Related View DBA_GG_AUTO_CDR_COLUMN_GROUPS provides details about all of the Oracle GoldenGate automatic CDR column groups in the database. See Also: " DBA_GG_AUTO_CDR_COLUMN_GROUPS " See Also: " DBA_GG_AUTO_CDR_COLUMN_GROUPS "