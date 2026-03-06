---
id: 19c__DBMS_DBFS_CONTENT.GETFEATURESBYNAME
name: DBMS_DBFS_CONTENT.GETFEATURESBYNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETFEATURESBYNAME

This function returns features of a store by store name.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETFEATURESBYNAME (
   store_name       IN      VARCHAR2)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETFEATURESBYNAME ( store_name IN VARCHAR2) RETURN INTEGER; Parameters Table 52-37 GETFEATURESBYNAME Function Parameters Parameter Description store_name Name of store Return Values A bit mask of supported features (see FEATURES_T Table Type )