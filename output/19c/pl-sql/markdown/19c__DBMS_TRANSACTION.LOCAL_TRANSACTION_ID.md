---
id: 19c__DBMS_TRANSACTION.LOCAL_TRANSACTION_ID
name: DBMS_TRANSACTION.LOCAL_TRANSACTION_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.LOCAL_TRANSACTION_ID

This function returns the local (to instance) unique identifier for the current transaction. It returns null if there is no current transaction.

## Syntax

```sql
DBMS_TRANSACTION.LOCAL_TRANSACTION_ID (
   create_transaction BOOLEAN := FALSE)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| create_transaction | BOOLEAN | IN | If true, then start a transaction if one is not currently active. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_TRANSACTION.LOCAL_TRANSACTION_ID ( create_transaction BOOLEAN := FALSE) RETURN VARCHAR2; Parameters Table 179-4 LOCAL_TRANSACTION_ID Function Parameters Parameter Description create_transaction If true, then start a transaction if one is not currently active.