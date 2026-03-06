---
id: 19c__DBMS_WORKLOAD_REPOSITORY.PURGE_SQL_DETAILS
name: DBMS_WORKLOAD_REPOSITORY.PURGE_SQL_DETAILS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.PURGE_SQL_DETAILS

This procedure purges SQL details, specifically rows from WRH$_SQLTEXT , WRH$_SQL_PLAN , and WRH$_SQL_BIND_METADATA that do not have corresponding rows ( DBID , SQL_ID ) in WRH$_SQLSTAT .

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.PURGE_SQL_DETAILS(
   numrows IN NUMBER DEFAULT NULL,  
   dbid    IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| numrows | NUMBER | IN | Number of rows |
| dbid | NUMBER | IN | Database ID (default to local DBID) |

## Usage Notes

The subprogram calls for the DBID for which to run the purge. If the DBID is not specified, the database DBID is used. You can constrain runtime by specifying the maximum number of rows to purge per table. If no maximum is specified, the subprograms tries to purge all applicable rows. Syntax DBMS_WORKLOAD_REPOSITORY.PURGE_SQL_DETAILS( numrows IN NUMBER DEFAULT NULL, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-36 PURGE_SQL_DETAILS Procedure Parameters Parameter Description numrows Number of rows dbid Database ID (default to local DBID)