---
id: 19c__DBMS_ROWID.ROWID_ROW_NUMBER
name: DBMS_ROWID.ROWID_ROW_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_ROW_NUMBER

This function extracts the row number from the ROWID IN parameter.

## Syntax

```sql
DBMS_ROWID.ROWID_ROW_NUMBER (
   row_id IN ROWID)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id | ROWID) | IN | ROWID to be interpreted. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_ROWID.ROWID_ROW_NUMBER ( row_id IN ROWID) RETURN NUMBER; Pragmas PRAGMA RESTRICT_REFERENCES(rowid_row_number,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-11 ROWID_ROW_NUMBER Function Parameters Parameter Description row_id ROWID to be interpreted. Examples Select a row number: SELECT dbms_rowid.rowid_row_number(ROWID) FROM emp WHERE ename = 'ALLEN';