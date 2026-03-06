---
id: 19c__DBMS_ROWID.ROWID_OBJECT
name: DBMS_ROWID.ROWID_OBJECT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROWID
tags: [dbms_rowid]
source_file: DBMS_ROWID.html
---

# DBMS_ROWID.ROWID_OBJECT

This function returns the data object number for an extended ROWID .

## Syntax

```sql
DBMS_ROWID.ROWID_OBJECT (
   rowid_id IN ROWID)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| row_id |  |  | ROWID to be interpreted |

**Returns:** `NUMBER`

## Usage Notes

The function returns zero if the input ROWID is a restricted ROWID . Syntax DBMS_ROWID.ROWID_OBJECT ( rowid_id IN ROWID) RETURN NUMBER; Pragmas pragma RESTRICT_REFERENCES(rowid_object,WNDS,RNDS,WNPS,RNPS); Parameters Table 148-9 ROWID_OBJECT Function Parameters Parameter Description row_id ROWID to be interpreted Note: The ROWID_OBJECT_UNDEFINED constant is returned for restricted ROWIDs . Note: The ROWID_OBJECT_UNDEFINED constant is returned for restricted ROWIDs .