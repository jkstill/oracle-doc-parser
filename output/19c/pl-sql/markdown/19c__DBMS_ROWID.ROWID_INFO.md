---
id: 19c__DBMS_ROWID.ROWID_INFO
name: DBMS_ROWID.ROWID_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_INFO

This procedure returns information about a ROWID , including its type (restricted or extended), and the components of the ROWID .

## Syntax

```sql
DBMS_ROWID.ROWID_INFO (
   rowid_in         IN   ROWID,
   rowid_type       OUT  NUMBER,
   object_number    OUT  NUMBER,
   relative_fno     OUT  NUMBER,
   block_number     OUT  NUMBER,
   row_number       OUT  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rowid_in | ROWID | IN | ROWID to be interpreted. This determines if the ROWID is a restricted (0) or extended (1) ROWID . |
| rowid_type | NUMBER | OUT | Returns type (restricted/extended) |
| object_number | NUMBER | OUT | Returns data object number ( rowid_object_undefined for restricted) |
| relative_fno | NUMBER | OUT | Returns relative file number |
| block_number | NUMBER | OUT | Returns block number in this file |
| row_number | NUMBER) | OUT | Returns row number in this block |

## Usage Notes

This is a procedure, and it cannot be used in a SQL statement. Syntax DBMS_ROWID.ROWID_INFO ( rowid_in IN ROWID, rowid_type OUT NUMBER, object_number OUT NUMBER, relative_fno OUT NUMBER, block_number OUT NUMBER, row_number OUT NUMBER); Pragmas pragma RESTRICT_REFERENCES(rowid_info,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-8 ROWID_INFO Procedure Parameters Parameter Description rowid_in ROWID to be interpreted. This determines if the ROWID is a restricted (0) or extended (1) ROWID . rowid_type Returns type (restricted/extended) object_number Returns data object number ( rowid_object_undefined for restricted) relative_fno Returns relative file number block_number Returns block number in this file row_number Returns row number in this block See Also: " ROWID_TYPE Function " See Also: " ROWID_TYPE Function "