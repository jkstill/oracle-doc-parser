---
id: 19c__DBMS_TRANSACTION.ROLLBACK_SAVEPOINT
name: DBMS_TRANSACTION.ROLLBACK_SAVEPOINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.ROLLBACK_SAVEPOINT

This procedure is equivalent to the SQL statement ROLLBACK TO SAVEPOINT <savepoint_name> .

## Syntax

```sql
DBMS_TRANSACTION.ROLLBACK_SAVEPOINT (
   savept VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| savept | VARCHAR2) | IN | Savepoint identifier. |

## Usage Notes

This procedure is included for completeness, the functionality being already implemented as part of PL/SQL. Syntax DBMS_TRANSACTION.ROLLBACK_SAVEPOINT ( savept VARCHAR2); Parameters Table 179-9 ROLLBACK_SAVEPOINT Procedure Parameters Parameter Description savept Savepoint identifier.