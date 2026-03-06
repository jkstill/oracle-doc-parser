---
id: 19c__DBMS_ERRLOG.CREATE_ERROR_LOG
name: DBMS_ERRLOG.CREATE_ERROR_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ERRLOG
tags: [dbms_errlog]
source_file: DBMS_ERRLOG.html
---

# DBMS_ERRLOG.CREATE_ERROR_LOG

This procedure creates the error logging table needed to use the DML error logging capability.

## Syntax

```sql
DBMS_ERRLOG.CREATE_ERROR_LOG (
   dml_table_name            IN VARCHAR2,
   err_log_table_name        IN VARCHAR2 := NULL,
   err_log_table_owner       IN VARCHAR2 := NULL,
   err_log_table_space       IN VARCHAR2 := NULL,
   skip_unsupported          IN BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dml_table_name | VARCHAR2 | IN | The name of the DML table to base the error logging table on. The name can be fully qualified (for example, emp , scott.emp , "EMP" , "SCOTT"."EMP" ). If a name component is enclosed in double quotes, it will not be upper cased. |
| err_log_table_name | VARCHAR2 | IN | The name of the error logging table you will create. The default is the first 25 characters in the name of the DML table prefixed with 'ERR$_' . Examples are the following: dml_table_name : 'EMP' , err_log_table_name : 'ERR$_EMP' dml_table_name : '"Emp2"' , err_log_table_name : 'ERR$_Emp2' |
| err_log_table_owner | VARCHAR2 | IN | The name of the owner of the error logging table. You can specify the owner in dml_table_name . Otherwise, the schema of the current connected user is used. |
| err_log_table_space | VARCHAR2 | IN | The tablespace the error logging table will be created in. If not specified, the default tablespace for the user owning the DML error logging table will be used. |
| skip_unsupported | BOOLEAN | IN | When set to TRUE , column types that are not supported by error logging will be skipped over and not added to the error logging table. When set to FALSE , an unsupported column type will cause the procedure to terminate. The default is FALSE . |

## Usage Notes

LONG , CLOB , BLOB , BFILE , and ADT datatypes are not supported in the columns. Syntax DBMS_ERRLOG.CREATE_ERROR_LOG ( dml_table_name IN VARCHAR2, err_log_table_name IN VARCHAR2 := NULL, err_log_table_owner IN VARCHAR2 := NULL, err_log_table_space IN VARCHAR2 := NULL, skip_unsupported IN BOOLEAN := FALSE); Parameters Table 68-2 CREATE_ERROR_LOG Procedure Parameters Parameter Description dml_table_name The name of the DML table to base the error logging table on. The name can be fully qualified (for example, emp , scott.emp , "EMP" , "SCOTT"."EMP" ). If a name component is enclosed in double quotes, it will not be upper cased. err_log_table_name The name of the error logging table you will create. The default is the first 25 characters in the name of the DML table prefixed with 'ERR$_' . Examples are the following: dml_table_name : 'EMP' , err_log_table_name : 'ERR$_EMP' dml_table_name : '"Emp2"' , err_log_table_name : 'ERR$_Emp2' err_log_table_owner The name of the owner of the error logging table. You can specify the owner in dml_table_name . Otherwise, the schema of the current connected user is used. err_log_table_space The tablespace the error logging table will be created in. If not specified, the default tablespace for the user owning the DML error logging table will be used. skip_unsupported When set to TRUE , column types that are not supported by error logging will be skipped over and not added to the error logging table. When set to FALSE , an unsupported column type will cause the procedure to terminate. The default is FALSE . Examples First, create an error log table for the channels table in the SH schema, using the default name generation. Then, see all columns of the table channels : SQL> DESC channels Name Null? Type --------------------------- ------- ----- CHANNEL_ID NOT NULL CHAR(1) CHANNEL_DESC NOT NULL VARCHAR2(20) CHANNEL_CLASS VARCHAR2(20) Finally, see all columns of the generated error log table. Note the mandatory control columns that are created by the package: SQL> DESC ERR$_CHANNELS Name Null? Type ----------------- ---- ---- ORA_ERR_NUMBER$ NUMBER ORA_ERR_MESG$ VARCHAR2(2000) ORA_ERR_ROWID$ ROWID ORA_ERR_OPTYP$ VARCHAR2(2) ORA_ERR_TAG$ VARCHAR2(2000) CHANNEL_ID VARCHAR2(4000) CHANNEL_DESC VARCHAR2(4000) CHANNEL_CLASS VARCHAR2(4000) See Oracle Database Administrator's Guide for more information regarding control columns.