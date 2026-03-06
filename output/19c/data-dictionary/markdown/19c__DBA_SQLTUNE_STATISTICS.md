---
id: 19c__DBA_SQLTUNE_STATISTICS
name: DBA_SQLTUNE_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_SQLTUNE_STATISTICS.html
---

# DBA_SQLTUNE_STATISTICS

DBA_SQLTUNE_STATISTICS displays statistics associated with all SQL statements in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER(38) | Tuning task identifier |
| OBJECT_ID | NUMBER(38) | Advisor framework object identifier |
| PARSING_SCHEMA_ID | NUMBER | Schema under which the SQL is parsed |
| MODULE | VARCHAR2(64) | Last application module recorded for the SQL |
| ACTION | VARCHAR2(64) | Last application action recorded for the SQL |
| ELAPSED_TIME | NUMBER | Elapsed time for the SQL statement |
| CPU_TIME | NUMBER | CPU time for the SQL |
| BUFFER_GETS | NUMBER | Number of buffer gets |
| DISK_READS | NUMBER | Number of disk reads |
| DIRECT_WRITES | NUMBER | Number of disk writes |
| ROWS_PROCESSED | NUMBER | Number of rows processed by the SQL |
| FETCHES | NUMBER | Number of fetches |
| EXECUTIONS | NUMBER | Number of executions |
| END_OF_FETCH_COUNT | NUMBER | End of fetch count |
| OPTIMIZER_COST | NUMBER | Optimizer cost for the SQL |
| OPTIMIZER_ENV | RAW(2000) | Optimizer environment |
| COMMAND_TYPE | NUMBER | Command type |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_SQLTUNE_STATISTICS displays statistics associated with the SQL statements owned by the current user. See Also: " USER_SQLTUNE_STATISTICS " See Also: " USER_SQLTUNE_STATISTICS "