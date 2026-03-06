---
id: 19c__DBMS_AQADM.SET_WATERMARK
name: DBMS_AQADM.SET_WATERMARK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.SET_WATERMARK

This procedure is used for Oracle Database Advanced Queuing notification to specify and limit memory use.

## Syntax

```sql
DBMS_AQADM.SET_WATERMARK (
   wmvalue     IN      NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wmvalue | NUMBER) | IN | Watermark value in megabytes. |

## Usage Notes

Syntax DBMS_AQADM.SET_WATERMARK ( wmvalue IN NUMBER); Parameters Table 23-55 SET_WATERMARK Procedure Parameter Parameter Description wmvalue Watermark value in megabytes.