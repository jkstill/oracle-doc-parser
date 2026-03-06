---
id: 19c__DBMS_UTILITY.CREATE_ALTER_TYPE_ERROR_TABLE
name: DBMS_UTILITY.CREATE_ALTER_TYPE_ERROR_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.CREATE_ALTER_TYPE_ERROR_TABLE

This procedure creates an error table to be used in the EXCEPTION clause of the ALTER TYPE statement.

## Syntax

```sql
DBMS_UTILITY.CREATE_ALTER_TYPE_ERROR_TABLE(
   schema_name     IN     VARCHAR2,
   table_name      IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of the schema |
| table_name | VARCHAR2) | IN | Name of the table created |

## Usage Notes

Syntax DBMS_UTILITY.CREATE_ALTER_TYPE_ERROR_TABLE( schema_name IN VARCHAR2, table_name IN VARCHAR2); Parameters Table 187-13 CREATE_ALTER_TYPE_ERROR_TABLE Procedure Parameters Parameter Description schema_name Name of the schema table_name Name of the table created Exceptions An error is returned if the table already exists.