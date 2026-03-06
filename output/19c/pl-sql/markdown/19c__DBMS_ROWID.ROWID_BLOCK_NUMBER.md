---
id: 19c__DBMS_ROWID.ROWID_BLOCK_NUMBER
name: DBMS_ROWID.ROWID_BLOCK_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_BLOCK_NUMBER

This function returns the database block number for the input ROWID .

## Syntax

```sql
DBMS_ROWID.ROWID_BLOCK_NUMBER (
   row_id      IN   ROWID,
   ts_type_in  IN   VARCHAR2 DEFAULT 'SMALLFILE')
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id | ROWID | IN | ROWID to be interpreted |
| ts_type_in | VARCHAR2 | IN | The type of the tablespace (bigfile/smallfile) to which the row belongs |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_ROWID.ROWID_BLOCK_NUMBER ( row_id IN ROWID, ts_type_in IN VARCHAR2 DEFAULT 'SMALLFILE') RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_block_number,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-6 ROWID_BLOCK_NUMBER Function Parameters Parameter Description row_id ROWID to be interpreted ts_type_in The type of the tablespace (bigfile/smallfile) to which the row belongs Examples The example SQL statement selects the block number from a ROWID and inserts it into another table: INSERT INTO T2 (SELECT dbms_rowid.rowid_block_number(ROWID, 'BIGFILE') FROM some_table WHERE key_value = 42);