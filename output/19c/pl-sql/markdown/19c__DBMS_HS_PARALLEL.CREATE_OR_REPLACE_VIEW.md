---
id: 19c__DBMS_HS_PARALLEL.CREATE_OR_REPLACE_VIEW
name: DBMS_HS_PARALLEL.CREATE_OR_REPLACE_VIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PARALLEL
tags: [dbms_hs_parallel]
source_file: DBMS_HS_PARALLEL.html
---

# DBMS_HS_PARALLEL.CREATE_OR_REPLACE_VIEW

This procedure creates (or replaces) a read-only view to be referenced for retrieving the data from a remote table in parallel.

## Syntax

```sql
CREATE_OR_REPLACE_VIEW (remote_table, database_link, oracle_view, parallel_degree)
```

## Usage Notes

Syntax CREATE_OR_REPLACE_VIEW (remote_table, database_link, oracle_view, parallel_degree) Parameters Table 84-2 CREATE_OR_REPLACE_VIEW Procedure Parameters Parameters Description remote_table The name of the remote database table. It is specified as [remote_schema_name.]remote_table_name . database_link The remote database link name. The call can only be applied to a heterogeneous services database link. oracle_view The name of the Oracle view. It is specified as [schema_name.]oracle_view_name . The default schema name is the current user. If the oracle_view parameter is not specified, the remote table name will be used as the view name. parallel_degree The number of parallel processes for the operation is computed based on the range-partition number if applicable, or the number of CPUs. The range of values is 2 to 16 . Usage Notes The specified Oracle view is created and future reference of this view utilizes internal database objects for parallel retrieval of remote non-Oracle table data. If the Oracle view already exists, the following Oracle error message is raised: ORA-00955: name is already used by an existing object This view is created as a read-only view. If you attempt to insert and update the view, the following Oracle error message is raised: ORA-01733: virtual column not allowed here If the remote table or the database link does not exist, one of the following Oracle error messages is raised: ORA-00942: table or view does not exist or ORA-02019: connection description for remote database not found You need the CREATE VIEW , CREATE TABLE , CREATE TYPE , CREATE PACKAGE , and CREATE FUNCTION privileges to execute the CREATE_OR_REPLACE_VIEW procedure. If you encounter either of the following Oracle error messages, increase the PROCESSES and SESSIONS parameter in the Oracle initialization parameter file: ORA-12801: error signaled in parallel query server P003 or ORA-00018: maximum number of session exceeded Because the CREATE_OR_REPLACE_VIEW procedure creates some internal objects, use the DROP_VIEW procedure to drop the view and the internal objects. The SQL DROP VIEW statement only drops the view and not the internal objects.