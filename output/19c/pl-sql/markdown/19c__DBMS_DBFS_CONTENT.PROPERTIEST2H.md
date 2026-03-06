---
id: 19c__DBMS_DBFS_CONTENT.PROPERTIEST2H
name: DBMS_DBFS_CONTENT.PROPERTIEST2H
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PROPERTIEST2H

This function converts a DBMS_DBFS_CONTENT_PROPERTIES_T table to a PROPERTY_T hash.

## Syntax

```sql
DBMS_DBFS_CONTENT.PROPERTIEST2H (
   sprops      IN      DBMS_DBFS_CONTENT_PROPERTIES_T)
RETURN properties_t;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sprops | DBMS_DBFS_CONTENT_PROPERTIES_T) | IN | A DBMS_DBFS_CONTENT_PROPERTIES_T table |

**Returns:** `properties_t`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PROPERTIEST2H ( sprops IN DBMS_DBFS_CONTENT_PROPERTIES_T) RETURN properties_t; Parameters Table 52-54 PROPERTIEST2H Function Parameters Parameter Description sprops A DBMS_DBFS_CONTENT_PROPERTIES_T table Return Values PROPERTIES_T Table Type