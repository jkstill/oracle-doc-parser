---
id: 19c__DBMS_ROWID.ROWID_CREATE
name: DBMS_ROWID.ROWID_CREATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_CREATE

This function lets you create a ROWID , given the component parts as parameters.

## Syntax

```sql
DBMS_ROWID.ROWID_CREATE (
   rowid_type    IN NUMBER, 
   object_number IN NUMBER,
   relative_fno  IN NUMBER,
   block_number  IN NUMBER,
   row_number    IN NUMBER) 
  RETURN ROWID;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rowid_type | NUMBER | IN | Type (restricted or extended) Set the rowid_type parameter to 0 for a restricted ROWID . Set it to 1 to create an extended ROWID . If you specify rowid_type as 0, then the required object_number parameter is ignored, and ROWID_CREATE returns a restricted ROWID . |
| object_number | NUMBER | IN | Data object number ( rowid_object_undefined for restricted) |
| relative_fno | NUMBER | IN | Relative file number |
| block_number | NUMBER | IN | Block number in this file |
| row_number | NUMBER) | IN | Returns row number in this block |

**Returns:** `ROWID`

## Usage Notes

This is useful for testing ROWID operations, because only the Oracle Server can create a valid ROWID that points to data in a database. Syntax DBMS_ROWID.ROWID_CREATE ( rowid_type IN NUMBER, object_number IN NUMBER, relative_fno IN NUMBER, block_number IN NUMBER, row_number IN NUMBER) RETURN ROWID; Pragmas pragma RESTRICT_REFERENCES(rowid_create,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-7 ROWID_CREATE Function Parameters Parameter Description rowid_type Type (restricted or extended) Set the rowid_type parameter to 0 for a restricted ROWID . Set it to 1 to create an extended ROWID . If you specify rowid_type as 0, then the required object_number parameter is ignored, and ROWID_CREATE returns a restricted ROWID . object_number Data object number ( rowid_object_undefined for restricted) relative_fno Relative file number block_number Block number in this file row_number Returns row number in this block Examples Create a dummy extended ROWID : my_rowid := DBMS_ROWID.ROWID_CREATE(1, 9999, 12, 1000, 13); Find out what the rowid_object function returns: obj_number := DBMS_ROWID.ROWID_OBJECT(my_rowid); The variable obj_number now contains 9999.