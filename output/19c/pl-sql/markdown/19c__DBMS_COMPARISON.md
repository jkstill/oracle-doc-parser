---
id: 19c__DBMS_COMPARISON
name: DBMS_COMPARISON
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPARISON
tags: [dbms_comparison]
source_file: DBMS_COMPARISON.html
---

# DBMS_COMPARISON

The DBMS_COMPARISON package defines a RECORD type.

## Syntax

```sql
TYPE COMPARISON_TYPE IS RECORD(
  scan_id            NUMBER,
  loc_rows_merged    NUMBER,
  rmt_rows_merged    NUMBER,
  loc_rows_deleted   NUMBER,
  rmt_rows_deleted   NUMBER);
```

## Usage Notes

Contains information returned by the COMPARE function or CONVERGE procedure in the DBMS_COMPARISON package. Note: The COMPARE function only returns a value for the scan_id field. Note: The COMPARE function only returns a value for the scan_id field. Note: The COMPARE function only returns a value for the scan_id field. Note: The COMPARE function only returns a value for the scan_id field. Syntax TYPE COMPARISON_TYPE IS RECORD( scan_id NUMBER, loc_rows_merged NUMBER, rmt_rows_merged NUMBER, loc_rows_deleted NUMBER, rmt_rows_deleted NUMBER);