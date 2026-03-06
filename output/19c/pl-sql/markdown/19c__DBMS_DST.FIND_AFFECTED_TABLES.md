---
id: 19c__DBMS_DST.FIND_AFFECTED_TABLES
name: DBMS_DST.FIND_AFFECTED_TABLES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.FIND_AFFECTED_TABLES

This procedure finds all the tables which have affected TSTZ data due to the new timezone version.

## Syntax

```sql
DBMS_DST.FIND_AFFECTED_TABLES (
   affected_tables             IN  VARCHAR2 =: 'sys.dst$affected_tables',
   log_errors                  IN  BOOLEAN := FALSE,
   log_errors_table            IN  VARCHAR2 =: 'sys.dst$error_table',
   parallel                    IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| affected_tables | VARCHAR2 | IN | Name of table with the following schema: CREATE TABLE dst$affected_tables ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), row_count NUMBER, error_count NUMBER) The table can be created with the CREATE_AFFECTED_TABLE Procedure . |
| log_errors | BOOLEAN | IN | Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . |
| log_errors_table | VARCHAR2 | IN | Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid column records the rowids of the offending rows, and the error_number column records the corresponding error number. |
| parallel | BOOLEAN | IN | Boolean flag indicating whether to find the affected tables using parallel queries or serial queries. The default is FALSE . |

## Usage Notes

This procedure can only be invoked during a prepare window. The tables which have affected TSTZ data are recorded into a table indicated by parameter affected_tables . If semantic errors must be logged, they are recorded into a table indicated by parameter log_errors_table . Syntax DBMS_DST.FIND_AFFECTED_TABLES ( affected_tables IN VARCHAR2 =: 'sys.dst$affected_tables', log_errors IN BOOLEAN := FALSE, log_errors_table IN VARCHAR2 =: 'sys.dst$error_table', parallel IN BOOLEAN := FALSE); Parameters Table 65-9 FIND_AFFECTED_TABLES Procedure Parameters Parameter Description affected_tables Name of table with the following schema: CREATE TABLE dst$affected_tables ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), row_count NUMBER, error_count NUMBER) The table can be created with the CREATE_AFFECTED_TABLE Procedure . log_errors Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . log_errors_table Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid column records the rowids of the offending rows, and the error_number column records the corresponding error number. parallel Boolean flag indicating whether to find the affected tables using parallel queries or serial queries. The default is FALSE .