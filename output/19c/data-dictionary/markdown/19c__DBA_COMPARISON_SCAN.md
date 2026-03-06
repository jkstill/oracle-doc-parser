---
id: 19c__DBA_COMPARISON_SCAN
name: DBA_COMPARISON_SCAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_COMPARISON_SCAN.html
---

# DBA_COMPARISON_SCAN

DBA_COMPARISON_SCAN displays information about all comparison scans in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the comparison scan |
| COMPARISON_NAME | VARCHAR2(128) | Name of the comparison scan |
| SCAN_ID | NUMBER | Scan ID |
| PARENT_SCAN_ID | NUMBER | Scan ID of the immediate parent scan |
| ROOT_SCAN_ID | NUMBER | Scan ID of the root (top-most) parent |
| STATUS | VARCHAR2(16) | Status of the scan: SUC BUCKET DIF FINAL BUCKET DIF ROW DIF |
| CURRENT_DIF_COUNT | NUMBER | Current cumulative (including children) diff count of the scan |
| INITIAL_DIF_COUNT | NUMBER | Initial cumulative (including children) diff count of the scan |
| COUNT_ROWS | NUMBER | Number of rows in the scan |
| SCAN_NULLS | VARCHAR2(1) | Indicates whether NULLs are part of this scan ( Y ) or not ( N ) |
| LAST_UPDATE_TIME | TIMESTAMP(6) | Time that this row was last updated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_COMPARISON_SCAN displays information about the comparison scans owned by the current user. This view does not display the OWNER column. See Also: " USER_COMPARISON_SCAN " See Also: " USER_COMPARISON_SCAN "