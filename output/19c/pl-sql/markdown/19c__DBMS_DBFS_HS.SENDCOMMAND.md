---
id: 19c__DBMS_DBFS_HS.SENDCOMMAND
name: DBMS_DBFS_HS.SENDCOMMAND
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.SENDCOMMAND

This procedure sends a command to be executed on the external storage device's Media Manager.

## Syntax

```sql
DBMS_DBFS_HS.SENDCOMMAND (
   store_name    IN       VARCHAR2,
   message       IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| message | VARCHAR2) | IN | Message string to be executed |

## Usage Notes

Syntax DBMS_DBFS_HS.SENDCOMMAND ( store_name IN VARCHAR2, message IN VARCHAR2); Parameters Table 54-15 SENDCOMMAND Procedure Parameters Parameter Description store_name Name of store message Message string to be executed