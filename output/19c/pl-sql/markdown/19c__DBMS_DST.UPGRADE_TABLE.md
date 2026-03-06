---
id: 19c__DBMS_DST.UPGRADE_TABLE
name: DBMS_DST.UPGRADE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.UPGRADE_TABLE

This procedure upgrades a specified list of tables that have one or more columns defined on the TSTZ type, or an ADT containing the TSTZ type.

## Syntax

```sql
DBMS_DST.UPGRADE_TABLE  (
   num_of_failures             OUT BINARY_INTEGER,
   table_list                  IN  VARCHAR2,
   upgrade_data                IN  BOOLEAN := TRUE,
   parallel                    IN  BOOLEAN := FALSE,
   continue_after_errors       IN  BOOLEAN := TRUE,
   log_errors                  IN  BOOLEAN := FALSE,
   log_errors_table            IN  VARCHAR2 =: 'sys.dst$error_table' ,
   error_on_overlap_time       IN  BOOLEAN := FALSE,
   error_on_nonexisting_time   IN  BOOLEAN := FALSE,
   log_triggers_table          IN  VARCHAR2 := 'sys.dst$trigger_table',
   atomic_upgrade              IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| num_of_failures | BINARY_INTEGER | OUT | Number of tables that fail to complete |
| table_list | VARCHAR2 | IN | Table name list (comma separated strings) |
| upgrade_data | BOOLEAN | IN | Boolean flag indicating whether to convert TSTZ data using the new Time Zone patch File ( TRUE ), or to leave unconverted ( FALSE ). The default is TRUE . |
| parallel | BOOLEAN | IN | Boolean flag indicating whether to convert tables using PDML (Parallel DML), or Serial DML. The default is FALSE . |
| continue_after_errors | BOOLEAN | IN | Boolean flag indicating whether to continue after upgrade fails on the current table. The default is TRUE . |
| log_errors | BOOLEAN | IN | Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . |
| log_errors_table | VARCHAR2 | IN | Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid parameter records the rowids of the offending rows and the corresponding error number. |
| error_on_overlap_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is TRUE . |
| error_on_nonexisting_time | BOOLEAN | IN | Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default is TRUE . |
| log_triggers_table | VARCHAR2 | IN | Table to log triggers that are disabled before upgrade, having not been enabled due to a fatal failure when performing an upgrade |
| atomic_upgrade | BOOLEAN | IN | Boolean flag indicating whether to convert the listed tables atomically (in a single transaction). If FALSE , each table is converted in its own transaction. The default is FALSE . |

## Usage Notes

Syntax DBMS_DST.UPGRADE_TABLE ( num_of_failures OUT BINARY_INTEGER, table_list IN VARCHAR2, upgrade_data IN BOOLEAN := TRUE, parallel IN BOOLEAN := FALSE, continue_after_errors IN BOOLEAN := TRUE, log_errors IN BOOLEAN := FALSE, log_errors_table IN VARCHAR2 =: 'sys.dst$error_table' , error_on_overlap_time IN BOOLEAN := FALSE, error_on_nonexisting_time IN BOOLEAN := FALSE, log_triggers_table IN VARCHAR2 := 'sys.dst$trigger_table', atomic_upgrade IN BOOLEAN := FALSE); Parameters Table 65-12 UPGRADE_TABLE Procedure Parameters Parameter Description num_of_failures Number of tables that fail to complete table_list Table name list (comma separated strings) upgrade_data Boolean flag indicating whether to convert TSTZ data using the new Time Zone patch File ( TRUE ), or to leave unconverted ( FALSE ). The default is TRUE . parallel Boolean flag indicating whether to convert tables using PDML (Parallel DML), or Serial DML. The default is FALSE . continue_after_errors Boolean flag indicating whether to continue after upgrade fails on the current table. The default is TRUE . log_errors Boolean flag indicating whether to log errors during upgrade. If FALSE , no error is logged into the log_errors_table after aborting conversion of the current table. If TRUE , the error is logged to the log_errors_table . The default is FALSE . log_errors_table Table name with the following schema: CREATE TABLE dst$error_table ( table_owner VARCHAR2(30), table_name VARCHAR2(30), column_name VARCHAR2(4000), rid ROWID, error_number NUMBER) The table can be created with the CREATE_ERROR_TABLE Procedure . The rid parameter records the rowids of the offending rows and the corresponding error number. error_on_overlap_time Boolean flag indicating whether to report errors on the 'overlap' time semantic conversion error. The default is TRUE . error_on_nonexisting_time Boolean flag indicating whether to report errors on the 'non-existing' time semantic conversion error. The default is TRUE . log_triggers_table Table to log triggers that are disabled before upgrade, having not been enabled due to a fatal failure when performing an upgrade atomic_upgrade Boolean flag indicating whether to convert the listed tables atomically (in a single transaction). If FALSE , each table is converted in its own transaction. The default is FALSE . Usage Notes This procedure can only be invoked after an upgrade window has been started. The table list has to satisfy the following partial ordering: If a base table has a materialized view log table, the log table must be the next item in the list. If the container table for a materialized view appears in the list, the materialized view's 'non-upgraded' base tables and log tables must appear in the table list and before the container table. A base table and its materialized view log table need to be upgraded in an atomic transaction by specifying atomic_upgrade to TRUE .