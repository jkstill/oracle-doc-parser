---
id: 19c__DBMS_APPLY_ADM.EXECUTE_ALL_ERRORS
name: DBMS_APPLY_ADM.EXECUTE_ALL_ERRORS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.EXECUTE_ALL_ERRORS

This procedure re-executes the error transactions in the error queue for the specified apply component.

## Syntax

```sql
DBMS_APPLY_ADM.EXECUTE_ALL_ERRORS(
   apply_name       IN  VARCHAR2  DEFAULT NULL,
   execute_as_user  IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The name of the apply component that raised the errors while processing the transactions. Do not specify an owner. If NULL , then all error transactions for all apply components are re-executed. |
| execute_as_user | BOOLEAN | IN | If TRUE , then the procedure re-executes the transactions in the security context of the current user. If FALSE , then the procedure re-executes each transaction in the security context of the original receiver of the transaction. The original receiver is the user who was processing the transaction when the error was raised. The DBA_APPLY_ERROR data dictionary view lists the original receiver for each error transaction. The user who executes the transactions must have privileges to perform DML and DDL changes on the apply objects and to run any apply handlers. This user must also have dequeue privileges on the queue used by the apply component. |

## Usage Notes

The transactions are re-executed in commit SCN order. Error re-execution stops if an error is raised. Syntax DBMS_APPLY_ADM.EXECUTE_ALL_ERRORS( apply_name IN VARCHAR2 DEFAULT NULL, execute_as_user IN BOOLEAN DEFAULT FALSE); Parameters Table 21-11 EXECUTE_ALL_ERRORS Procedure Parameters Parameter Description apply_name The name of the apply component that raised the errors while processing the transactions. Do not specify an owner. If NULL , then all error transactions for all apply components are re-executed. execute_as_user If TRUE , then the procedure re-executes the transactions in the security context of the current user. If FALSE , then the procedure re-executes each transaction in the security context of the original receiver of the transaction. The original receiver is the user who was processing the transaction when the error was raised. The DBA_APPLY_ERROR data dictionary view lists the original receiver for each error transaction. The user who executes the transactions must have privileges to perform DML and DDL changes on the apply objects and to run any apply handlers. This user must also have dequeue privileges on the queue used by the apply component. Usage Notes The following usage notes apply to this procedure: The EXECUTE_ALL_ERRORS Procedure and XStream Outbound Servers The EXECUTE_ALL_ERRORS Procedure and XStream Inbound Servers The EXECUTE_ALL_ERRORS Procedure and XStream Outbound Servers Outbound servers do not enqueue error transactions into an error queue. This procedure cannot be used with XStream outbound servers. The EXECUTE_ALL_ERRORS Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.