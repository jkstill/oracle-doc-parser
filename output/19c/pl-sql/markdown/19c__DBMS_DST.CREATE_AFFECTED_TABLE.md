---
id: 19c__DBMS_DST.CREATE_AFFECTED_TABLE
name: DBMS_DST.CREATE_AFFECTED_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.CREATE_AFFECTED_TABLE

This procedure creates a table that has the schema shown in the comments for the FIND_AFFECTED_TABLES Procedure.

## Syntax

```sql
DBMS_DST.CREATE_AFFECTED_TABLE (
   table_name      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2) | IN | Name of the table created |

## Usage Notes

Syntax DBMS_DST.CREATE_AFFECTED_TABLE ( table_name IN VARCHAR2); Parameters Table 65-5 CREATE_AFFECTED_TABLE Procedure Parameters Parameter Description table_name Name of the table created Usage Notes This procedures takes a table_name without schema qualification, creating a table within the current user schema.