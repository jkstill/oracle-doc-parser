---
id: 19c__DBMS_XDB.GETCONTENTXMLREF
name: DBMS_XDB.GETCONTENTXMLREF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETCONTENTXMLREF

This deprecated function retrieves the contents of a resource returned as a a REF to an XMLTYPE .

## Syntax

```sql
DBMS_XDB.GETCONTENTXMLREF(
     abspath    IN     VARCHAR2,
  RETURN SYS.XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `SYS.XMLTYPE`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTXMLREF Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTXMLREF Function . Syntax DBMS_XDB.GETCONTENTXMLREF( abspath IN VARCHAR2, RETURN SYS.XMLTYPE; Parameters Table 194-18 GETCONTENTXMLREF Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as a REF to an XMLTYPE .