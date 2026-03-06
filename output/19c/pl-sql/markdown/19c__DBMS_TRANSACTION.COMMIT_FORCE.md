---
id: 19c__DBMS_TRANSACTION.COMMIT_FORCE
name: DBMS_TRANSACTION.COMMIT_FORCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.COMMIT_FORCE

This procedure is equivalent to the SQL statement: COMMIT FORCE <text>, <number>"

## Syntax

```sql
DBMS_TRANSACTION.COMMIT_FORCE (
   xid VARCHAR2, 
   scn VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xid | VARCHAR2 | IN | Local or global transaction ID. |
| scn | VARCHAR2 | IN | System change number. |

## Usage Notes

Syntax DBMS_TRANSACTION.COMMIT_FORCE ( xid VARCHAR2, scn VARCHAR2 DEFAULT NULL); Parameters Table 179-3 COMMIT_FORCE Procedure Parameters Parameter Description xid Local or global transaction ID. scn System change number.