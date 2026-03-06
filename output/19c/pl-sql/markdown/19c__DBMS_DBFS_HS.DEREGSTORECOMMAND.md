---
id: 19c__DBMS_DBFS_HS.DEREGSTORECOMMAND
name: DBMS_DBFS_HS.DEREGSTORECOMMAND
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.DEREGSTORECOMMAND

This procedure removes a command that had been previously associated with a store through the REGISTERSTORECOMMAND Procedure.

## Syntax

```sql
DBMS_DBFS_HS.DEREGSTORECOMMAND (
   store_name      IN     VARCHAR2,
   message         IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| message | VARCHAR2) | IN | Message to be deregistered |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_DBFS_HS.DEREGSTORECOMMAND ( store_name IN VARCHAR2, message IN VARCHAR2); Parameters Table 54-9 DEREGSTORECOMMAND Procedure Parameters Parameter Description store_name Name of store message Message to be deregistered Usage Notes If this subprogram successfully executes, its actions cannot be rolled back by the user. If the user wants to restore the previous state, the user must call the REGISTERSTORECOMMAND Procedure .