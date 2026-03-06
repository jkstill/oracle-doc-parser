---
id: 19c__DBMS_ROWID.ROWID_TO_ABSOLUTE_FNO
name: DBMS_ROWID.ROWID_TO_ABSOLUTE_FNO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_TO_ABSOLUTE_FNO

This function extracts the absolute file number from a ROWID , where the file number is absolute for a row in a given schema and table.

## Syntax

```sql
DBMS_ROWID.ROWID_TO_ABSOLUTE_FNO (
   row_id      IN ROWID,
   schema_name IN VARCHAR2,
   object_name IN VARCHAR2)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id | ROWID | IN | ROWID to be interpreted |
| schema_name | VARCHAR2 | IN | Name of the schema which contains the table |
| object_name | VARCHAR2) | IN | Table name |

**Returns:** `NUMBER`

## Usage Notes

The schema name and the name of the schema object (such as a table name) are provided as IN parameters for this function. Syntax DBMS_ROWID.ROWID_TO_ABSOLUTE_FNO ( row_id IN ROWID, schema_name IN VARCHAR2, object_name IN VARCHAR2) RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_to_absolute_fno,WNDS,WNPS,RNPS); Parameters Table 148-12 ROWID_TO_ABSOLUTE_FNO Function Parameters Parameter Description row_id ROWID to be interpreted schema_name Name of the schema which contains the table object_name Table name Examples DECLARE abs_fno INTEGER; rowid_val CHAR(18); object_name VARCHAR2(20) := 'EMP'; BEGIN SELECT ROWID INTO rowid_val FROM emp WHERE empno = 9999; abs_fno := dbms_rowid.rowid_to_absolute_fno( rowid_val, 'SCOTT', object_name); Note: For partitioned objects, the name must be a table name, not a partition or a sub/partition name.