---
id: 19c__DBMS_XDB.GETACLDOCUMENT
name: DBMS_XDB.GETACLDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETACLDOCUMENT

This deprecated function retrieves ACL document that protects resource given its path name.

## Syntax

```sql
DBMS_XDB.GETACLDOCUMENT(
   abspath  IN  VARCHAR2)
  RETURN sys.xmltype;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Path name of the resource whose ACL document is required |

**Returns:** `sys.xmltype`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETACLDOCUMENT Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETACLDOCUMENT Function . Syntax DBMS_XDB.GETACLDOCUMENT( abspath IN VARCHAR2) RETURN sys.xmltype; Parameters Table 194-14 GETACLDOCUMENT Function Parameters Parameter Description abspath Path name of the resource whose ACL document is required Return Values The XMLType for ACL document.