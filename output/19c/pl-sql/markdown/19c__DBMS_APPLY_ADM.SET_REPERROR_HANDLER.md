---
id: 19c__DBMS_APPLY_ADM.SET_REPERROR_HANDLER
name: DBMS_APPLY_ADM.SET_REPERROR_HANDLER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.SET_REPERROR_HANDLER

This procedure specifies how a particular error is handled based on its error number.

## Syntax

```sql
DBMS_APPLY_ADM.SET_REPERROR_HANDLER(
  apply_name     IN  VARCHAR2,
  object         IN  VARCHAR2,
  error_number   IN  NUMBER,
  method         IN  VARCHAR2,
  source_object  IN  VARCHAR2  DEFAULT NULL,
  max_retries    IN  NUMBER    DEFAULT NULL,
  delay_csecs    IN  NUMBER    DEFAULT 6000);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The name of the apply process. |
| object | VARCHAR2 | IN | The schema and name of the target table, specified as [ schema name .] table name for which an error handler is being added, modified, or removed. The table must exist. For example, if an update conflict handler is being added for table employees owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. |
| error_number | NUMBER | IN | The error handling number. If 0 , then use the default for all error handling for object . |
| method | VARCHAR2 | IN | Specifies the action to take when the given error_number occurs. If NULL , remove the error handler for error_number The possible actions are: ABEND : Stop the apply process when the error occurs. RECORD : Move the LCR to the error queue when the error is encountered. IGNORE : Silently ignore the error and do not apply the LCR. RETRY : Retry the LCR max_retries times. RETRY_TRANSACTION : Retry the transaction max_retries times. Wait delay_csecs centiseconds before each retry. RECORD_TRANSACTION : Move the entire transaction to the error queue if this error occurs. |
| source_object | VARCHAR2 | IN | The schema and object name of the source table, specified as [ schema_name .] table_name for the table where the change originated. For example, if the change originated at the employees table owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. |
| max_retires |  |  | Maximum number of times to retry for RETRY and RETRY_TRANSACTION actions in method . Must be specified with either the RETRY or RETRY_TRANSACTION |
| delay_csecs | NUMBER | IN | The number of centiseconds between retries for RETRY and RETRY_TRANSACTION action in method . |

## Usage Notes

You can choose between several predefined actions for a given error. Syntax DBMS_APPLY_ADM.SET_REPERROR_HANDLER( apply_name IN VARCHAR2, object IN VARCHAR2, error_number IN NUMBER, method IN VARCHAR2, source_object IN VARCHAR2 DEFAULT NULL, max_retries IN NUMBER DEFAULT NULL, delay_csecs IN NUMBER DEFAULT 6000); Parameters Table 21-24 SET_REPERROR_HANDLER Procedure Parameters Parameter Description apply_name The name of the apply process. object The schema and name of the target table, specified as [ schema name .] table name for which an error handler is being added, modified, or removed. The table must exist. For example, if an update conflict handler is being added for table employees owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. error_number The error handling number. If 0 , then use the default for all error handling for object . method Specifies the action to take when the given error_number occurs. If NULL , remove the error handler for error_number The possible actions are: ABEND : Stop the apply process when the error occurs. RECORD : Move the LCR to the error queue when the error is encountered. IGNORE : Silently ignore the error and do not apply the LCR. RETRY : Retry the LCR max_retries times. RETRY_TRANSACTION : Retry the transaction max_retries times. Wait delay_csecs centiseconds before each retry. RECORD_TRANSACTION : Move the entire transaction to the error queue if this error occurs. source_object The schema and object name of the source table, specified as [ schema_name .] table_name for the table where the change originated. For example, if the change originated at the employees table owned by user hr , then specify hr.employees . If the schema is not specified, then the current user is the default. max_retires Maximum number of times to retry for RETRY and RETRY_TRANSACTION actions in method . Must be specified with either the RETRY or RETRY_TRANSACTION delay_csecs The number of centiseconds between retries for RETRY and RETRY_TRANSACTION action in method . Usage Notes The following usage notes apply to this procedure: Priority of Error Handlers Priority of Error Handlers Any conflict handling specified by SET_UPDATE_CONFLICT_HANDLER or SET_DML_CONFLICT_HANDLER is tried before the actions specified by SET_REPERROR_HANDLER . The PL/SQL procedure specified by SET_DML_HANDLER is called to handle the error if none of the previously mentioned methods resolve it.