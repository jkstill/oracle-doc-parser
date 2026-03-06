---
id: 19c__DBMS_AQADM.MIGRATE_QUEUE_TABLE
name: DBMS_AQADM.MIGRATE_QUEUE_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.MIGRATE_QUEUE_TABLE

This procedure upgrades an 8.0-compatible queue table to an 8.1-compatible or higher queue table, or downgrades an 8.1-compatible or higher queue table to an 8.0-compatible queue table.

## Syntax

```sql
DBMS_AQADM.MIGRATE_QUEUE_TABLE (
   queue_table   IN   VARCHAR2,
   compatible    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_table | VARCHAR2 | IN | Specifies name of the queue table to be migrated. |
| compatible | VARCHAR2) | IN | Set this to 8.1 to upgrade an 8.0-compatible queue table, or set this to 8.0 to downgrade an 8.1-compatible queue table. |

## Usage Notes

Syntax DBMS_AQADM.MIGRATE_QUEUE_TABLE ( queue_table IN VARCHAR2, compatible IN VARCHAR2); Parameters Table 23-43 MIGRATE_QUEUE_TABLE Procedure Parameters Parameter Description queue_table Specifies name of the queue table to be migrated. compatible Set this to 8.1 to upgrade an 8.0-compatible queue table, or set this to 8.0 to downgrade an 8.1-compatible queue table.