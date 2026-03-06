---
id: 19c__DBMS_SESSION.SET_ROLE
name: DBMS_SESSION.SET_ROLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_ROLE

This procedure enables and disables roles. It is equivalent to the SET ROLE SQL statement.

## Syntax

```sql
DBMS_SESSION.SET_ROLE (
   role_cmd VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| role_cmd | VARCHAR2) | IN | Text is appended to "set role" and then run as SQL |

## Usage Notes

Syntax DBMS_SESSION.SET_ROLE ( role_cmd VARCHAR2); Parameters Table 154-22 SET_ROLE Procedure Parameters Parameter Description role_cmd Text is appended to "set role" and then run as SQL Usage Notes Note that the procedure creates a new transaction if it is not invoked from within an existing transaction.