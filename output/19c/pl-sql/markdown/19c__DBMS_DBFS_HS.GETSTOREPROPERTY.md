---
id: 19c__DBMS_DBFS_HS.GETSTOREPROPERTY
name: DBMS_DBFS_HS.GETSTOREPROPERTY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.GETSTOREPROPERTY

This function retrieves the values of a property.

## Syntax

```sql
DBMS_DBFS_HS.GETSTOREPROPERTY  (
   store_name      IN     VARCHAR2,
   property_name   IN     VARCHAR2,
   noexcp          IN     BOOLEAN DEFAULT FALSE) RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| property_name | VARCHAR2 | IN | Name of property |
| noexcp | BOOLEAN | IN | If set to FALSE , raises an exception if the property does not exist in the database. If noexcp is set to TRUE , returns NULL if the property does not exist. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_HS.GETSTOREPROPERTY ( store_name IN VARCHAR2, property_name IN VARCHAR2, noexcp IN BOOLEAN DEFAULT FALSE) RETURN VARCHAR2; Parameters Table 54-12 GETSTOREPROPERTY Function Parameters Parameter Description store_name Name of store property_name Name of property noexcp If set to FALSE , raises an exception if the property does not exist in the database. If noexcp is set to TRUE , returns NULL if the property does not exist. Return Values The values of a property. Usage Notes The specified store must already have been created.