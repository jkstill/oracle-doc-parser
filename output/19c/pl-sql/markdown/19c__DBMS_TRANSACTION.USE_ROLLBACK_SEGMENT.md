---
id: 19c__DBMS_TRANSACTION.USE_ROLLBACK_SEGMENT
name: DBMS_TRANSACTION.USE_ROLLBACK_SEGMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSACTION
tags: [dbms_transaction]
source_file: DBMS_TRANSACTION.html
---

# DBMS_TRANSACTION.USE_ROLLBACK_SEGMENT

This procedure is equivalent to the SQL statement SET TRANSACTION USE ROLLBACK SEGMENT <rb_seg_name> .

## Syntax

```sql
DBMS_TRANSACTION.USE_ROLLBACK_SEGMENT (
   rb_name VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rb_name | VARCHAR2) | IN | Name of rollback segment to use. |

## Usage Notes

Syntax DBMS_TRANSACTION.USE_ROLLBACK_SEGMENT ( rb_name VARCHAR2); Parameters Table 179-11 USE_ROLLBACK_SEGMENT Procedure Parameters Parameter Description rb_name Name of rollback segment to use.