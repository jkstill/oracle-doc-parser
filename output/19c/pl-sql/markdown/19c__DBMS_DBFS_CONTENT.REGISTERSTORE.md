---
id: 19c__DBMS_DBFS_CONTENT.REGISTERSTORE
name: DBMS_DBFS_CONTENT.REGISTERSTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.REGISTERSTORE

This procedure registers a new store backed by a provider that uses a store provider (conforming to the DBMS_DBFS_CONTENT_SPI package signature).

## Syntax

```sql
DBMS_DBFS_CONTENT.REGISTERSTORE (
   store_name          IN      VARCHAR2,
   provider_name       IN      VARCHAR2,
   provider_package    IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store, must be unique |
| provider_name | VARCHAR2 | IN | Name of provider |
| provider_package | VARCHAR2) | IN | Store provider |

## Usage Notes

This method is to be used primarily by store providers after they have created a new store. Syntax DBMS_DBFS_CONTENT.REGISTERSTORE ( store_name IN VARCHAR2, provider_name IN VARCHAR2, provider_package IN VARCHAR2); Parameters Table 52-62 REGISTERSTORE Procedure Parameters Parameter Description store_name Name of store, must be unique provider_name Name of provider provider_package Store provider