---
id: 19c__DBA_COMPARISON_SCAN_VALUES
name: DBA_COMPARISON_SCAN_VALUES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_COMPARISON_SCAN_VALUES.html
---

# DBA_COMPARISON_SCAN_VALUES

DBA_COMPARISON_SCAN_VALUES displays information about the values for all comparison scans in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the comparison scan |
| COMPARISON_SCAN | VARCHAR2(128) | Name of the comparison scan |
| SCAN_ID | NUMBER | Scan ID |
| COLUMN_POSITION | NUMBER | Column position, as in DBA_COMPARISON_COLUMNS |
| MIN_VALUE | VARCHAR2(4000) | Minimum value of the scan |
| MAX_VALUE | VARCHAR2(4000) | Maximum value of the scan |
| LAST_UPDATE_TIME | TIMESTAMP(6) | Time that this row was last updated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_COMPARISON_SCAN_VALUES displays information about the values for the comparison scans owned by the current user. This view does not display the OWNER column. See Also: " USER_COMPARISON_SCAN_VALUES " See Also: " USER_COMPARISON_SCAN_VALUES "