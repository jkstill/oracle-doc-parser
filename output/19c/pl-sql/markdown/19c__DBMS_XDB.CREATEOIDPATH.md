---
id: 19c__DBMS_XDB.CREATEOIDPATH
name: DBMS_XDB.CREATEOIDPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CREATEOIDPATH

This deprecated function creates a virtual path to the resource based on object ID.

## Syntax

```sql
DBMS_XDB.CREATEOIDPATH(
   oid    IN   RAW)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oid | RAW) | IN | Object ID of the resource |

**Returns:** `VARCHAR2`

## Usage Notes

Note: This funtion is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATEOIDPATH Function . Note: This funtion is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATEOIDPATH Function . Syntax DBMS_XDB.CREATEOIDPATH( oid IN RAW) RETURN VARCHAR2; Parameters Table 194-9 CREATEOIDPATH Function Parameters Parameter Description oid Object ID of the resource