---
id: 19c__DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS
name: DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS

This procedure rebuilds all indexes and enables the constraints on an XMLType table including its child tables and out-of-line tables.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.ENABLEINDEXESANDCONSTRAINTS (
   owner_name   IN VARCHAR2 DEFAULT USER, 
   table_name   IN VARCHAR2, 
   column_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_user |  |  | Owner's name |
| table_name | VARCHAR2 | IN | Name of the table that the indexes and constraints are being removed from |
| column_name | VARCHAR2 | IN | Column name |

## Usage Notes

When column_name is passed, it does the same for this XMLType column. Syntax DBMS_XMLSTORAGE_MANAGE. ENABLEINDEXESANDCONSTRAINTS ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2, column_name IN VARCHAR2 DEFAULT NULL); Parameters Table 213-3 ENABLEINDEXESANDCONSTRAINTS Procedure Parameters Parameter Description owner_user Owner's name table_name Name of the table that the indexes and constraints are being removed from column_name Column name Usage Notes This procedure reverses DISABLEINDEXESANDCONSTRAINTS Procedure . Example See DISABLEINDEXESANDCONSTRAINTS Procedure