---
id: 19c__DBMS_HS_PARALLEL.LOAD_TABLE
name: DBMS_HS_PARALLEL.LOAD_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PARALLEL
tags: [dbms_hs_parallel]
source_file: DBMS_HS_PARALLEL.html
---

# DBMS_HS_PARALLEL.LOAD_TABLE

This procedure loads the data from a remote table to a local Oracle table in parallel. If the local Oracle table does not already exist, it is created automatically.

## Syntax

```sql
LOAD_TABLE (remote_table, database_link, oracle_table, truncate, parallel_degree, row_count)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| remote_table |  |  | The name of the remote database table. It is specified as [remote_schema_name.]remote_table_name |
| database_link |  |  | The remote database link name. The call can only be applied to a heterogeneous services database link. |
| oracle_table |  |  | The name of the local Oracle table the data will be loaded into. It is specified as [schema_name.]oracle_table_name . The default schema name is the current user. If the oracle_table parameter is not specified, the remote table name will be used as the local Oracle name. |
| truncate |  |  | Determines whether the Oracle table is truncated before the data is loaded. The value is either TRUE or FALSE . The default value is TRUE which means the Oracle table is truncated first. When set to FALSE , the Oracle table will not be truncated before the data is loaded. |
| parallel_degree |  |  | The number of parallel processes for the operation is computed based on the range-partition number if applicable, or the number of CPUs. The range of values is 2 to 16 . |
| row_count |  |  | Contains the number of rows just added with the load table operation. |

## Usage Notes

Syntax LOAD_TABLE (remote_table, database_link, oracle_table, truncate, parallel_degree, row_count) Parameters Table 84-5 LOAD_TABLE Procedure Parameters Parameter Description remote_table The name of the remote database table. It is specified as [remote_schema_name.]remote_table_name database_link The remote database link name. The call can only be applied to a heterogeneous services database link. oracle_table The name of the local Oracle table the data will be loaded into. It is specified as [schema_name.]oracle_table_name . The default schema name is the current user. If the oracle_table parameter is not specified, the remote table name will be used as the local Oracle name. truncate Determines whether the Oracle table is truncated before the data is loaded. The value is either TRUE or FALSE . The default value is TRUE which means the Oracle table is truncated first. When set to FALSE , the Oracle table will not be truncated before the data is loaded. parallel_degree The number of parallel processes for the operation is computed based on the range-partition number if applicable, or the number of CPUs. The range of values is 2 to 16 . row_count Contains the number of rows just added with the load table operation. Usage Notes This procedure only loads the remote table data into Oracle local table. It does not create a key, index, constraints or any other dependencies such as triggers. It is recommended that you create these dependencies after the table data is loaded as performance will improve greatly. You will need to decide whether to create the dependencies before or after the data is loaded based on your knowledge of the remote table data and dependencies. If the local table does not exist, the LOAD_TABLE procedure creates a simple (non-partitioned) local table based on the exact column matching of the remote table after which the data is inserted into the local table. If the remote table or the database link does not exist, an error message is returned. If the local table is incompatible with the remote table, an error message is returned. You need the CREATE TABLE , CREATE TYPE , CREATE PACKAGE , and CREATE FUNCTION privileges to execute the LOAD_TABLE procedure. If you encounter either of the following Oracle error messages, increase the PROCESSES and SESSIONS parameter in Oracle initialization parameter file: ORA-12801: error signaled in parallel query server P003 or ORA-00018: maximum number of session exceeded One of the following is required for parallel processing: The remote table is range partitioned. Histogram information for a numeric column is available. There is a numeric index or primary key. To drop the local table, use the DROP TABLE SQL statement.