---
id: 19c__DBMS_DBFS_CONTENT.PROPERTIESH2T
name: DBMS_DBFS_CONTENT.PROPERTIESH2T
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PROPERTIESH2T

This function converts a PROPERTY_T hash to a DBMS_DBFS_CONTENT_PROPERTIES_T table.

## Syntax

```sql
DBMS_DBFS_CONTENT.PROPERTIEST2H (
   pprops      IN      PROPERTIES_T)
RETURN DBMS_DBFS_CONTENT_PROPERTIES_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sprops |  |  | A PROPERTIES_T hash |

**Returns:** `DBMS_DBFS_CONTENT_PROPERTIES_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PROPERTIEST2H ( pprops IN PROPERTIES_T) RETURN DBMS_DBFS_CONTENT_PROPERTIES_T; Parameters Table 52-53 PROPERTIEST2H Function Parameters Parameter Description sprops A PROPERTIES_T hash Return Values DBMS_DBFS_CONTENT_PROPERTIES_T Table Type