---
id: 19c__DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL
name: DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL

This procedure chunks the table (associated with the specified task) by means of a user-provided SELECT statement.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL (
   task_name       IN  VARCHAR2,
   sql_stmt        IN  CLOB,
   by_rowid        IN  BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| sql_stmt | CLOB | IN | SQL that returns the chunk ranges |
| by_rowid | BOOLEAN) | IN | TRUE if the table is chunked by rowids |

## Usage Notes

The SELECT statement that returns the range of each chunk must have two columns: start_id and end_id . If the task is to chunk by ROWID , then the two columns must be of ROWID type. If the task is to chunk the table by NUMBER column, then the two columns must be of NUMBER type. The procedure provides the flexibility to users who want to deploy user-defined chunk algorithms. Syntax DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL ( task_name IN VARCHAR2, sql_stmt IN CLOB, by_rowid IN BOOLEAN); Parameters Table 121-12 CREATE_CHUNKS_BY_SQL Procedure Parameters Parameter Description task_name Name of the task sql_stmt SQL that returns the chunk ranges by_rowid TRUE if the table is chunked by rowids