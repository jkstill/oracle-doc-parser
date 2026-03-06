---
id: 19c__DBMS_DBFS_CONTENT.GETFEATURESBYMOUNT
name: DBMS_DBFS_CONTENT.GETFEATURESBYMOUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETFEATURESBYMOUNT

This function returns features of a store by mount point.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETFEATURESBYMOUNT (
   store_mount       IN      VARCHAR2)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_mount | VARCHAR2) | IN | Mount point |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETFEATURESBYMOUNT ( store_mount IN VARCHAR2) RETURN INTEGER; Parameters Table 52-36 GETFEATURESBYMOUNT Function Parameters Parameter Description store_mount Mount point Return Values A bit mask of supported features (see FEATURES_T Table Type )