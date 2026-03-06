---
id: 19c__DBMS_XMLSTORAGE_MANAGE.EXCHANGEPOSTPROC
name: DBMS_XMLSTORAGE_MANAGE.EXCHANGEPOSTPROC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORAGE_MANAGE
tags: [dbms_xmlstorage_manage]
source_file: DBMS_XMLSTORAGE_MANAGE.html
---

# DBMS_XMLSTORAGE_MANAGE.EXCHANGEPOSTPROC

This procedure enable constraints after exchange partition.

## Syntax

```sql
DBMS_XMLSTORAGE_MANAGE.EXCHANGEPOSTPROC (
   owner_name   IN VARCHAR2 DEFAULT USER, 
   table_name   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_user |  |  | Owner's name |
| table_name | VARCHAR2) | IN | Name of the table that the indexes and constraints are being removed from |

## Usage Notes

Syntax DBMS_XMLSTORAGE_MANAGE. EXCHANGEPOSTPROC ( owner_name IN VARCHAR2 DEFAULT USER, table_name IN VARCHAR2); Parameters Table 213-4 EXCHANGEPOSTPROC Procedure Parameters Parameter Description owner_user Owner's name table_name Name of the table that the indexes and constraints are being removed from