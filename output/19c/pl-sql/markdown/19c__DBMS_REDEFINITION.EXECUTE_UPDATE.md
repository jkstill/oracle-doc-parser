---
id: 19c__DBMS_REDEFINITION.EXECUTE_UPDATE
name: DBMS_REDEFINITION.EXECUTE_UPDATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.EXECUTE_UPDATE

This procedure can optimize the performance of bulk updates to a table. Performance is optimized because the updates are not logged in the redo log.

## Syntax

```sql
DBMS_REDEFINITION.EXECUTE_UPDATE (
   update_stmt  IN  CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| update_stmt | CLOB) | IN | The SQL UPDATE statement |

## Usage Notes

The EXECUTE_UPDATE procedure automatically uses the components of online table redefinition, such an interim table, a materialized view, and a materialized view log, to enable optimized bulk updates to a table. The EXECUTE_UPDATE procedure also removes fragmentation of the affected rows and ensures that the update is atomic. If the bulk updates raise any errors, then you can use the ABORT_UPDATE procedure to undo the changes made by the EXECUTE_UPDATE procedure. Syntax DBMS_REDEFINITION.EXECUTE_UPDATE ( update_stmt IN CLOB); Parameters Table 138-8 EXECUTE_UPDATE Procedure Parameters Parameter Description update_stmt The SQL UPDATE statement See Also: Oracle Database Administrator's Guide See Also: Oracle Database Administrator's Guide