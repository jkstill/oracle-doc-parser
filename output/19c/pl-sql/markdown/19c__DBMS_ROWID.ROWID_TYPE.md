---
id: 19c__DBMS_ROWID.ROWID_TYPE
name: DBMS_ROWID.ROWID_TYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_TYPE

This function returns 0 if the ROWID is a restricted ROWID , and 1 if it is extended.

## Syntax

```sql
DBMS_ROWID.ROWID_TYPE (
   rowid_id IN ROWID)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id |  |  | ROWID to be interpreted |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_ROWID.ROWID_TYPE ( rowid_id IN ROWID) RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_type,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-15 ROWID_TYPE Function Parameters Parameter Description row_id ROWID to be interpreted Examples IF DBMS_ROWID.ROWID_TYPE(my_rowid) = 1 THEN my_obj_num := DBMS_ROWID.ROWID_OBJECT(my_rowid);