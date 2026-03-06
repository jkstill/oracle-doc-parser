---
id: 19c__DBMS_APPLY_ADM.DELETE_ERROR
name: DBMS_APPLY_ADM.DELETE_ERROR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.DELETE_ERROR

This procedure deletes the specified error transaction.

## Syntax

```sql
DBMS_APPLY_ADM.DELETE_ERROR(
   local_transaction_id  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| local_transaction_id | VARCHAR2) | IN | The identification number of the error transaction to delete. If the specified transaction does not exist in the error queue, then an error is raised. |

## Usage Notes

Syntax DBMS_APPLY_ADM.DELETE_ERROR( local_transaction_id IN VARCHAR2); Parameter Table 21-8 DELETE_ERROR Procedure Parameter Parameter Description local_transaction_id The identification number of the error transaction to delete. If the specified transaction does not exist in the error queue, then an error is raised. Usage Notes The following usage notes apply to this procedure: The DELETE_ERROR Procedure and XStream Outbound Servers Outbound servers do not enqueue error transactions into an error queue. This procedure has no effect on XStream outbound servers.