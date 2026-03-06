---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETVERSION
name: DBMS_DBFS_CONTENT_SPI.GETVERSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETVERSION

This function returns the version associated with a store.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETVERSION (
   store_name          IN      VARCHAR2)
  RETURN  VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.GETVERSION ( store_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 53-16 GETVERSION Function Parameters Parameter Description store_name Name of store Return Values A "version" (either specific to a provider package, or to an individual store) based on a standard a.b.c naming convention (for major , minor , and patch components)