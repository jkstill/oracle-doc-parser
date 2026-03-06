---
id: 19c__DBMS_APPLY_ADM.DELETE_ALL_ERRORS
name: DBMS_APPLY_ADM.DELETE_ALL_ERRORS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.DELETE_ALL_ERRORS

This procedure deletes all the error transactions for the specified apply component.

## Syntax

```sql
DBMS_APPLY_ADM.DELETE_ALL_ERRORS(
   apply_name  IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| apply_name | VARCHAR2 | IN | The name of the apply component that raised the errors while processing the transactions. Do not specify an owner. If NULL , then all error transactions for all apply components are deleted. |

## Usage Notes

Syntax DBMS_APPLY_ADM.DELETE_ALL_ERRORS( apply_name IN VARCHAR2 DEFAULT NULL); Parameter Table 21-7 DELETE_ALL_ERRORS Procedure Parameter Parameter Description apply_name The name of the apply component that raised the errors while processing the transactions. Do not specify an owner. If NULL , then all error transactions for all apply components are deleted. Usage Notes The following usage notes apply to this procedure: The DELETE_ALL_ERRORS Procedure and XStream Outbound Servers The DELETE_ALL_ERRORS Procedure and XStream Inbound Servers The DELETE_ALL_ERRORS Procedure and XStream Outbound Servers Outbound servers do not enqueue error transactions into an error queue. This procedure has no effect on XStream outbound servers.