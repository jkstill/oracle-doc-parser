---
id: 19c__DBA_COMPARISON_ROW_DIF
name: DBA_COMPARISON_ROW_DIF
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_COMPARISON_ROW_DIF.html
---

# DBA_COMPARISON_ROW_DIF

DBA_COMPARISON_ROW_DIF displays information about the differing rows in all comparison scans in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the comparison |
| COMPARISON_NAME | VARCHAR2(128) | Name of the comparison |
| SCAN_ID | NUMBER | Scan ID for the comparison scan |
| LOCAL_ROWID | ROWID | Local rowid of the differing row |
| REMOTE_ROWID | ROWID | Remote rowid of the differing row |
| INDEX_VALUE | VARCHAR2(4000) | Index column value of the differing row |
| STATUS | VARCHAR2(3) | Status of the differing row: SUC DIF |
| LAST_UPDATE_TIME | TIMESTAMP(6) | Time that this row was last updated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_COMPARISON_ROW_DIF displays information about the differing rows in the comparison scans owned by the current user. This view does not display the OWNER column. See Also: " USER_COMPARISON_ROW_DIF " See Also: " USER_COMPARISON_ROW_DIF "