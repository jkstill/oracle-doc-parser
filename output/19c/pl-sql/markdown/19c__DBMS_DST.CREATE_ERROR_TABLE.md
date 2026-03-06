---
id: 19c__DBMS_DST.CREATE_ERROR_TABLE
name: DBMS_DST.CREATE_ERROR_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.CREATE_ERROR_TABLE

This procedure creates a log error table.

## Syntax

```sql
CREATE TABLE dst$error_table(
   table_owner     VARCHAR2(30),
   table_name      VARCHAR2(30),
   column_name     VARCHAR2(4000),
   rid             ROWID,
   error_number    NUMBER)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2(30) | IN | Name of the table created |

## Usage Notes

The table has the following schema: CREATE TABLE dst$error_table( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) Syntax DBMS_DST.CREATE_ERROR_TABLE ( table_name IN VARCHAR2); Parameters Table 65-6 CREATE_ERROR_TABLE Procedure Parameters Parameter Description table_name Name of the table created Usage Notes This procedures takes a table_name without schema qualification, creating a table within the current user schema. The error number is found when upgrading time zone file and timestamp with time zone data. For more information about error handling when upgrading time zone file and timestamp with time zone data, see Oracle Database Globalization Support Guide