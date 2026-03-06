---
id: 19c__DBMS_DBFS_CONTENT_SPI.CHECKACCESS
name: DBMS_DBFS_CONTENT_SPI.CHECKACCESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.CHECKACCESS

This function reports if the user ( principal ) can perform the specified operation on the given path. This enables verifying the validity of an operation without attempting to perform the operation. If CHECKACCESS returns 0, then the subprogram invoked to implement that operation should fail with an error.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.CHECKACCESS (
   store_name     IN     VARCHAR2  DEFAULT NULL,
   path           IN     VARCHAR2,
   pathtype       IN     INTEGER,
   operation      IN     VARCHAR2,
   principal      IN     VARCHAR2)
  RETURN  INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to check for access |
| pathtype | INTEGER | IN | Type of object path represents (see Table 52-4 ) |
| operation | VARCHAR2 | IN | Operation to be checked (see Table 52-8 ) |
| principal | VARCHAR2) | IN | File system user for whom the access check is made |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.CHECKACCESS ( store_name IN VARCHAR2 DEFAULT NULL, path IN VARCHAR2, pathtype IN INTEGER, operation IN VARCHAR2, principal IN VARCHAR2) RETURN INTEGER; Parameters Table 53-3 CHECKACCESS Procedure Parameters Parameter Description store_name Name of store path Name of path to check for access pathtype Type of object path represents (see Table 52-4 ) operation Operation to be checked (see Table 52-8 ) principal File system user for whom the access check is made Usage Notes Whether or not the user invokes this function, a store that supports access control internally performs these checks to guarantee security.