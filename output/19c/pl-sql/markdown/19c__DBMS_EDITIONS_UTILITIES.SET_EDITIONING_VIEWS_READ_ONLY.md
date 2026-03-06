---
id: 19c__DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY
name: DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EDITIONS_UTILITIES
tags: [dbms_editions_utilities]
source_file: DBMS_EDITIONS_UTILITIES.html
---

# DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY

Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to READ ONLY or READ/WRITE .

## Syntax

```sql
DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY (
   table_name IN VARCHAR2,
   owner      IN VARCHAR2 DEFAULT NULL,
   read_only  IN BOOLEAN  DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Base table of the editioning views |
| owner | VARCHAR2 | IN | Base table schema. The default (or NULL ) is the current schema. |
| read_only | BOOLEAN | IN | TRUE to set the views to read-only; FALSE (or NULL ) sets the views to READ/WRITE . Default is TRUE . |

## Usage Notes

Syntax DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY ( table_name IN VARCHAR2, owner IN VARCHAR2 DEFAULT NULL, read_only IN BOOLEAN DEFAULT TRUE); Parameters Table 66-3 SET_EDITIONING_VIEWS_READ_ONLY Procedure Parameters Parameter Description table_name Base table of the editioning views owner Base table schema. The default (or NULL ) is the current schema. read_only TRUE to set the views to read-only; FALSE (or NULL ) sets the views to READ/WRITE . Default is TRUE . Usage Notes The user must have the following privileges: Owner of the table, or have the ALTER ANY TABLE system privileges USE object privilege on all the editions for which the views are defined