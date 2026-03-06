---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETSTOREID
name: DBMS_DBFS_CONTENT_SPI.GETSTOREID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETSTOREID

This function returns the ID of a store.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETSTOREID (
   store_name          IN      VARCHAR2)
  RETURN  NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.GETSTOREID ( store_name IN VARCHAR2) RETURN NUMBER; Parameters Table 53-15 GETSTOREID Function Parameters Parameter Description store_name Name of store Return Values ID of the Store Usage Notes A store ID identifies a provider-specific store, across registrations and mounts, but independent of changes to the store contents. For this reason, changes to the store table or tables should be reflected in the store ID, but re-initialization of the same store table or tables should preserve the store ID.