---
id: 19c__DBMS_DST.UPGRADE_SCHEMA
name: DBMS_DST.UPGRADE_SCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.UPGRADE_SCHEMA

This procedure upgrades tables in a specified list of schemas that have one or more columns defined on the TSTZ type, or an ADT containing the TSTZ type.

## Syntax

```sql
DBMS_DST.UPGRADE_SCHEMA (
   num_of_failures             OUT BINARY_INTEGER,
   schema_list                 IN  VARCHAR2,
   upgrade_data                IN  BOOLEAN := TRUE,
   parallel                    IN  BOOLEAN := FALSE,
   continue_after_errors       IN  BOOLEAN := TRUE,
   log_errors                  IN  BOOLEAN := FALSE,
   log_errors_table            IN  VARCHAR2 =: 'sys.dst$error_table' ,
   error_on_overlap_time       IN  BOOLEAN := FALSE,
   error_on_nonexisting_time   IN  BOOLEAN := FALSE,
   log_triggers_table          IN  VARCHAR2 := 'sys.dst$trigger_table');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| num_of_failures | BINARY_INTEGER | OUT | Number of tables that fail to complete |
| schema_list | VARCHAR2 | IN | Schema name list (comma separated strings) |
| upgrade_data | BOOLEAN | IN | Boolean flag indicating whether to convert TSTZ data using the new Time Zone patch File ( TRUE ) or to leave unconverted ( FALSE ).The default is TRUE . |
| parallel | BOOLEAN | IN | Boolean flag indicating whether to convert tables using PDML (Parallel DML) or Serial DML.The default is FALSE . |
| continue_after_errors | BOOLEAN | IN | Boolean flag indicating whether to continue after upgrade fails on the current table.The default is TRUE . |
| log_errors | BOOLEAN | IN | Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . |
| log_errors_table | VARCHAR2 | IN | Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid column records the rowids of the offending rows, and the error_number column records the corresponding error number. |
| error_on_overlap_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is TRUE . |
| error_on_nonexisting_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default is TRUE . |
| log_triggers_table | VARCHAR2 | IN | Table to log triggers that are disabled before upgrade, having not been enabled due to a fatal failure when performing an upgrade |

## Usage Notes

This procedure can be invoked only after an upgrade window has been started. Each table is upgraded in an atomic transaction. Note that a base table and its materialized view log table are upgraded in an atomic transaction. Syntax DBMS_DST.UPGRADE_SCHEMA ( num_of_failures OUT BINARY_INTEGER, schema_list IN VARCHAR2, upgrade_data IN BOOLEAN := TRUE, parallel IN BOOLEAN := FALSE, continue_after_errors IN BOOLEAN := TRUE, log_errors IN BOOLEAN := FALSE, log_errors_table IN VARCHAR2 =: 'sys.dst$error_table' , error_on_overlap_time IN BOOLEAN := FALSE, error_on_nonexisting_time IN BOOLEAN := FALSE, log_triggers_table IN VARCHAR2 := 'sys.dst$trigger_table'); Parameters Table 65-11 UPGRADE_SCHEMA Procedure Parameters Parameter Description num_of_failures Number of tables that fail to complete schema_list Schema name list (comma separated strings) upgrade_data Boolean flag indicating whether to convert TSTZ data using the new Time Zone patch File ( TRUE ) or to leave unconverted ( FALSE ).The default is TRUE . parallel Boolean flag indicating whether to convert tables using PDML (Parallel DML) or Serial DML.The default is FALSE . continue_after_errors Boolean flag indicating whether to continue after upgrade fails on the current table.The default is TRUE . log_errors Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . log_errors_table Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid column records the rowids of the offending rows, and the error_number column records the corresponding error number. error_on_overlap_time Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is TRUE . error_on_nonexisting_time Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default is TRUE . log_triggers_table Table to log triggers that are disabled before upgrade, having not been enabled due to a fatal failure when performing an upgrade