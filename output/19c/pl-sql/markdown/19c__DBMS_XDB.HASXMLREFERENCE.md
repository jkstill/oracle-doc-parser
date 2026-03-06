---
id: 19c__DBMS_XDB.HASXMLREFERENCE
name: DBMS_XDB.HASXMLREFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.HASXMLREFERENCE

This deprecated function returns TRUE if the resource has a REF to XML content.

## Syntax

```sql
DBMS_XDB.HASXMLREFERENCE 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the HASXMLREFERENCE Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the HASXMLREFERENCE Function . Syntax DBMS_XDB.HASXMLREFERENCE abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 194-27 HASXMLREFERENCE Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values TRUE resource has a REF to XML content.