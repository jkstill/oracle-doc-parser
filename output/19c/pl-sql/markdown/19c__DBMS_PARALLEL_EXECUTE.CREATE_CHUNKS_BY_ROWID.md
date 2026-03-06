---
id: 19c__DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID
name: DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID

This procedure chunks the table (associated with the specified task) by ROWID .

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID (
   task_name       IN  VARCHAR2,
   table_owner     IN  VARCHAR2,
   table_name      IN  VARCHAR2,
   by_row          IN  BOOLEAN,
   chunk_size      IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| table_owner | VARCHAR2 | IN | Owner of the table |
| table_name | VARCHAR2 | IN | Name of the table |
| by_row | BOOLEAN | IN | TRUE if chunk_size refers to the number of rows, otherwise, chunk_size refers to the number of blocks |
| chunk_size | NUMBER) | IN | Approximate number of rows/blocks to process for each commit cycle |

## Usage Notes

num_row and num_block are approximate guidance for the size of each chunk. The table to be chunked must be a physical table with physical ROWID having views and table functions. Index-organized tables are not allowed. Syntax DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID ( task_name IN VARCHAR2, table_owner IN VARCHAR2, table_name IN VARCHAR2, by_row IN BOOLEAN, chunk_size IN NUMBER); Parameters Table 121-11 CREATE_CHUNKS_BY_ROWID Procedure Parameters Parameter Description task_name Name of the task table_owner Owner of the table table_name Name of the table by_row TRUE if chunk_size refers to the number of rows, otherwise, chunk_size refers to the number of blocks chunk_size Approximate number of rows/blocks to process for each commit cycle