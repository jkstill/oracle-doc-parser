---
id: 19c__DBMS_ROWID.ROWID_RELATIVE_FNO
name: DBMS_ROWID.ROWID_RELATIVE_FNO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_RELATIVE_FNO

This function returns the relative file number of the ROWID specified as the IN parameter. (The file number is relative to the tablespace.)

## Syntax

```sql
DBMS_ROWID.ROWID_RELATIVE_FNO (
   rowid_id      IN   ROWID,
   ts_type_in    IN   VARCHAR2 DEFAULT 'SMALLFILE')
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id |  |  | ROWID to be interpreted |
| ts_type_in | VARCHAR2 | IN | Type of the tablespace (bigfile/smallfile) to which the row belongs |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_ROWID.ROWID_RELATIVE_FNO ( rowid_id IN ROWID, ts_type_in IN VARCHAR2 DEFAULT 'SMALLFILE') RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_relative_fno,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-10 ROWID_RELATIVE_FNO Function Parameters Parameter Description row_id ROWID to be interpreted ts_type_in Type of the tablespace (bigfile/smallfile) to which the row belongs Examples The example PL/SQL code fragment returns the relative file number: DECLARE file_number INTEGER; rowid_val ROWID; BEGIN SELECT ROWID INTO rowid_val FROM dept WHERE loc = 'Boston'; file_number := dbms_rowid.rowid_relative_fno(rowid_val, 'SMALLFILE'); ...