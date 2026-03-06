---
id: 19c__DBMS_TRANSACTION.STEP_ID
name: DBMS_TRANSACTION.STEP_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.STEP_ID

This function returns local (to local transaction) unique positive integer that orders the DML operations of a transaction.

## Syntax

```sql
DBMS_TRANSACTION.STEP_ID 
   RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_TRANSACTION.STEP_ID RETURN NUMBER;