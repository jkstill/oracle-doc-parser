---
id: 19c__DBMS_DBFS_CONTENT.GETFEATURESBYPATH
name: DBMS_DBFS_CONTENT.GETFEATURESBYPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETFEATURESBYPATH

This function returns features of a store by path.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETFEATURESBYPATH (
   path       IN      PATH_T)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | PATH_T) | IN | PATH_T |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETFEATURESBYPATH ( path IN PATH_T) RETURN INTEGER; Parameters Table 52-38 GETFEATURESBYPATH Function Parameters Parameter Description path PATH_T Return Values A bit mask of supported features (see FEATURES_T Table Type )