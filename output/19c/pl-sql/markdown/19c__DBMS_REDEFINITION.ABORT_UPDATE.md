---
id: 19c__DBMS_REDEFINITION.ABORT_UPDATE
name: DBMS_REDEFINITION.ABORT_UPDATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.ABORT_UPDATE

This procedure can aborts an update started with the EXECUTE_UPDATE procedure in the RDBMS_REDEFINITION package.

## Syntax

```sql
DBMS_REDEFINITION.ABORT_UPDATE (
   update_stmt  IN  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| update_stmt | CLOB) | IN | The SQL UPDATE statement to be aborted The SQL statement must exactly match the SQL statement in the EXECUTE_UPDATE procedure. |

## Usage Notes

Syntax DBMS_REDEFINITION.ABORT_UPDATE ( update_stmt IN CLOB); Parameters Table 138-5 ABORT_UPDATE Procedure Parameters Parameter Description update_stmt The SQL UPDATE statement to be aborted The SQL statement must exactly match the SQL statement in the EXECUTE_UPDATE procedure. See Also: Oracle Database Administrator's Guide See Also: Oracle Database Administrator's Guide