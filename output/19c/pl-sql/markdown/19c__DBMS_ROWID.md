---
id: 19c__DBMS_ROWID
name: DBMS_ROWID
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID

This example returns the ROWID for a row in the EMP table, extracts the data object number from the ROWID , using the ROWID_OBJECT function in the DBMS_ROWID package, then displays the object number:

## Syntax

```sql
DECLARE
  object_no   INTEGER;
  row_id      ROWID;
  ...
BEGIN
  SELECT ROWID INTO row_id FROM emp
    WHERE empno = 7499;
  object_no := DBMS_ROWID.ROWID_OBJECT(row_id);
  DBMS_OUTPUT.PUT_LINE('The obj. # is '|| object_no);
  ...
```

## Usage Notes

DECLARE object_no INTEGER; row_id ROWID; ... BEGIN SELECT ROWID INTO row_id FROM emp WHERE empno = 7499; object_no := DBMS_ROWID.ROWID_OBJECT(row_id); DBMS_OUTPUT.PUT_LINE('The obj. # is '|| object_no); ...