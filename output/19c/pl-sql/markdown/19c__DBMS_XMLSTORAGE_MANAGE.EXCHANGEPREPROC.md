---
id: 19c__DBMS_XMLSTORAGE_MANAGE.EXCHANGEPREPROC
name: DBMS_XMLSTORAGE_MANAGE.EXCHANGEPREPROC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.EXCHANGEPREPROC

This procedure disable constraints before exchange partition.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.EXCHANGEPREPROC (
   owner_name   IN VARCHAR2 DEFAULT USER, 
   table_name   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_user |  |  | Owner's name |
| table_name | VARCHAR2) | IN | Name of the table that the indexes and constraints are being removed from |

## Usage Notes

Syntax DBMS_XMLSTORAGE_MANAGE. EXCHANGEPREPROC ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2); Parameters Table 213-5 EXCHANGEPREPROC Procedure Parameters Parameter Description owner_user Owner's name table_name Name of the table that the indexes and constraints are being removed from