---
id: 19c__DBMS_TRANSACTION.SAVEPOINT
name: DBMS_TRANSACTION.SAVEPOINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.SAVEPOINT

This procedure is equivalent to the SQL statement SAVEPOINT <savepoint_name> .

## Syntax

```sql
DBMS_TRANSACTION.SAVEPOINT (
   savept VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| savept | VARCHAR2) | IN | Savepoint identifier. |

## Usage Notes

This procedure is included for completeness, the feature being already implemented as part of PL/SQL. Syntax DBMS_TRANSACTION.SAVEPOINT ( savept VARCHAR2); Parameters Table 179-10 SAVEPOINT Procedure Parameters Parameter Description savept Savepoint identifier.