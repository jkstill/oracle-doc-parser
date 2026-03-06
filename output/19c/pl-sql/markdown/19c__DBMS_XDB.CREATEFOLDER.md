---
id: 19c__DBMS_XDB.CREATEFOLDER
name: DBMS_XDB.CREATEFOLDER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CREATEFOLDER

This deprecated function creates a new folder resource in the hierarchy.

## Syntax

```sql
DBMS_XDB.CREATEFOLDER(
   path   IN  VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2) | IN | Path name for the new folder |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATEFOLDER Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CREATEFOLDER Function . Syntax DBMS_XDB.CREATEFOLDER( path IN VARCHAR2) RETURN BOOLEAN; Parameters Table 194-8 CREATEFOLDER Function Parameters Parameter Description path Path name for the new folder Return Values TRUE if operation successful; FALSE , otherwise.