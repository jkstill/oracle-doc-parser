---
id: 19c__DBMS_CUBE_LOG.TABLE_CREATE
name: DBMS_CUBE_LOG.TABLE_CREATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TABLE_CREATE

This procedure creates the table targets for the OLAP logs. You must have the CREATE TABLE privilege to use this procedure.

## Syntax

```sql
DBMS_CUBE_LOG.TABLE_CREATE (
          LOG_TYPE       IN   BINARY_INTEGER  DEFAULT,
          TBLNAME        IN   VARCHAR2        DEFAULT );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . |
| tblname | VARCHAR2 | IN | A table name for the log. These are the default names: CUBE_OPERATIONS_LOG CUBE_REJECTED_RECORDS CUBE_DIMENSION_COMPILE CUBE_BUILD_LOG |

## Usage Notes

TABLE_CREATE also upgrades existing log tables to the current version while preserving the data. Syntax DBMS_CUBE_LOG.TABLE_CREATE ( LOG_TYPE IN BINARY_INTEGER DEFAULT, TBLNAME IN VARCHAR2 DEFAULT ); Parameters Table 46-9 TABLE_CREATE Procedure Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . tblname A table name for the log. These are the default names: CUBE_OPERATIONS_LOG CUBE_REJECTED_RECORDS CUBE_DIMENSION_COMPILE CUBE_BUILD_LOG Examples This example creates a Cube Operations log table named CUBE_OPERATIONS_LOG : EXECUTE dbms_cube_log.table_create; This example creates a Cube Rejected Records log table named CUBE_REJECTED_RECORDS : EXECUTE dbms_cube_log.table_create(dbms_cube_log.type_rejected_records); The next example creates a Cube Build log table named MY_BUILD_LOG : EXECUTE dbms_cube_log.table_create - (dbms_cube_log.type_build, 'MY_BUILD_LOG');