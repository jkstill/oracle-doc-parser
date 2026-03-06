---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETFEATURES
name: DBMS_DBFS_CONTENT_SPI.GETFEATURES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETFEATURES

This function returns the features of a store.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETFEATURES (
   store_name          IN      VARCHAR2)
  RETURN  INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.GETFEATURES ( store_name IN VARCHAR2) RETURN INTEGER; Parameters Table 53-11 GETFEATURES Function Parameters Parameter Description store_name Name of store Return Values DBMS_DBFS_CONTENT.FEATURE_* features supported by the Store Provider