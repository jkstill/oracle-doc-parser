---
id: 19c__V$SQLAREA_PLAN_HASH
name: V$SQLAREA_PLAN_HASH
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQLAREA_PLAN_HASH.html
---

# V$SQLAREA_PLAN_HASH

First thousand characters of the SQL text for the current cursor

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQL_TEXT | VARCHAR2(1000) |  |
| SQL_FULLTEXT | CLOB |  |
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| PLAN_HASH_VALUE | NUMBER |  |
| VERSION_COUNT | NUMBER |  |
| LAST_ACTIVE_CHILD_ADDRESS | RAW(4 | 8) |  |
| SHARABLE_MEM | NUMBER |  |
| PERSISTENT_MEM | NUMBER |  |
| RUNTIME_MEM | NUMBER |  |
| SORTS | NUMBER |  |
| LOADED_VERSIONS | NUMBER |  |
| OPEN_VERSIONS | NUMBER |  |
| USERS_OPENING | NUMBER |  |
| USERS_EXECUTING | NUMBER |  |
| FETCHES | NUMBER |  |
| EXECUTIONS | NUMBER |  |
| PX_SERVERS_EXECUTIONS | NUMBER |  |
| END_OF_FETCH_COUNT | NUMBER |  |
| LOADS | NUMBER |  |
| FIRST_LOAD_TIME | DATE |  |
| LAST_LOAD_TIME | DATE |  |
| LAST_ACTIVE_TIME | DATE |  |
| LAST_EXEC_START_TIME | DATE |  |
| INVALIDATIONS | NUMBER |  |
| PARSE_CALLS | NUMBER |  |
| DISK_READS | NUMBER |  |
| DIRECT_WRITES | NUMBER |  |
| BUFFER_GETS | NUMBER |  |
| CPU_TIME | NUMBER |  |
| ELAPSED_TIME | NUMBER |  |
| APPLICATION_WAIT_TIME | NUMBER |  |
| CONCURRENCY_WAIT_TIME | NUMBER |  |
| CLUSTER_WAIT_TIME | NUMBER |  |
| USER_IO_WAIT_TIME | NUMBER |  |
| PLSQL_EXEC_TIME | NUMBER |  |
| JAVA_EXEC_TIME | NUMBER |  |
| ROWS_PROCESSED | NUMBER |  |
| COMMAND_TYPE | NUMBER |  |
| OPTIMIZER_MODE | VARCHAR2(10) |  |
| OPTIMIZER_COST | NUMBER |  |
| OPTIMIZER_ENV | RAW(2000) |  |
| OPTIMIZER_ENV_HASH_VALUE | NUMBER |  |
| PARSING_USER_ID | NUMBER |  |
| PARSING_SCHEMA_ID | NUMBER |  |
| PARSING_SCHEMA_NAME | VARCHAR2(128) |  |
| KEPT_VERSIONS | NUMBER |  |
| MODULE | VARCHAR2(64) |  |
| MODULE_HASH | NUMBER |  |
| ACTION | VARCHAR2(64) |  |
| ACTION_HASH | NUMBER |  |
| SERIALIZABLE_ABORTS | NUMBER |  |
| OUTLINE_CATEGORY | VARCHAR2(64) |  |
| OUTLINE_SID | VARCHAR2(40) |  |
| REMOTE | VARCHAR2(1) |  |
| OBJECT_STATUS | VARCHAR2(19) |  |
| LITERAL_HASH_VALUE | NUMBER |  |
| SQL_PROFILE | VARCHAR2(64) |  |
| PROGRAM_ID | NUMBER |  |
| PROGRAM_LINE# | NUMBER |  |
| EXACT_MATCHING_SIGNATURE | NUMBER |  |
| FORCE_MATCHING_SIGNATURE | NUMBER |  |
| BIND_DATA | RAW(2000) |  |
| TYPECHECK_MEM | NUMBER |  |
| IO_CELL_OFFLOAD_ELIGIBLE_BYTES | NUMBER |  |
| IO_INTERCONNECT_BYTES | NUMBER |  |
| PHYSICAL_READ_REQUESTS | NUMBER |  |
| PHYSICAL_READ_BYTES | NUMBER |  |
| PHYSICAL_WRITE_REQUESTS | NUMBER |  |
| PHYSICAL_WRITE_BYTES | NUMBER |  |
| OPTIMIZED_PHY_READ_REQUESTS | NUMBER |  |
| IO_CELL_UNCOMPRESSED_BYTES | NUMBER |  |
| IO_CELL_OFFLOAD_RETURNED_BYTES | NUMBER |  |
| CON_ID | NUMBER |  |
| CON_DBID | NUMBER |  |

## Usage Notes

See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL package Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SHARED_POOL package Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_MODULE procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLICATION_INFO.SET_ACTION procedure