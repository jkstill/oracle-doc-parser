---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID
name: DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID

If the underlying GUID is found in the underlying store, this function returns the store-qualified path name.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID (
   store_name          IN      VARCHAR2,
   guid                IN      INTEGER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| guid | INTEGER) | IN | Unique ID representing the desired path item |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.GETPATHBYSTOREID ( store_name IN VARCHAR2, guid IN INTEGER) RETURN VARCHAR2; Parameters Table 53-13 GETPATHBYSTOREID Function Parameters Parameter Description store_name Name of store guid Unique ID representing the desired path item Return Values Store-qualified path name represented by the GUID Usage Notes If the STD_GUID is unknown, a NULL value is returned. Clients are expected to handle this as appropriate.