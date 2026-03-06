---
id: 19c__DBMS_TRANSACTION.ROLLBACK_FORCE
name: DBMS_TRANSACTION.ROLLBACK_FORCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.ROLLBACK_FORCE

This procedure is equivalent to the SQL statement ROLLBACK FORCE <text> .

## Syntax

```sql
DBMS_TRANSACTION.ROLLBACK_FORCE (
   xid VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | VARCHAR2) | IN | Local or global transaction ID. |

## Usage Notes

Syntax DBMS_TRANSACTION.ROLLBACK_FORCE ( xid VARCHAR2); Parameters Table 179-8 ROLLBACK_FORCE Procedure Parameters Parameter Description xid Local or global transaction ID.