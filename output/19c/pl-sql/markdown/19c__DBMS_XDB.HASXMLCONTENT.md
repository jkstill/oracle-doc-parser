---
id: 19c__DBMS_XDB.HASXMLCONTENT
name: DBMS_XDB.HASXMLCONTENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.HASXMLCONTENT

This deprecated function returns TRUE if the resource has XML content.

## Syntax

```sql
DBMS_XDB.HASXMLCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the HASXMLCONTENT Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the HASXMLCONTENT Function . Syntax DBMS_XDB.HASXMLCONTENT abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 194-26 HASXMLCONTENT Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values TRUE if the resource has XML content.