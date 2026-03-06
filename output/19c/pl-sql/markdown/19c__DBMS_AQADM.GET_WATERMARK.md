---
id: 19c__DBMS_AQADM.GET_WATERMARK
name: DBMS_AQADM.GET_WATERMARK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.GET_WATERMARK

This procedure retrieves the value of watermark set by SET_WATERMARK .

## Syntax

```sql
DBMS_AQADM.GET_WATERMARK (
   wmvalue     IN      NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wmvalue | NUMBER) | IN | Watermark value in megabytes. |

## Usage Notes

Syntax DBMS_AQADM.GET_WATERMARK ( wmvalue IN NUMBER); Parameters Table 23-40 GET_WATERMARK Procedure Parameter Parameter Description wmvalue Watermark value in megabytes.