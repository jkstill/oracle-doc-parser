---
id: 19c__DBMS_AQADM.GET_MIN_STREAMS_POOL
name: DBMS_AQADM.GET_MIN_STREAMS_POOL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.GET_MIN_STREAMS_POOL

This procedure retrieves the value of Oracle Database Advanced Queuing minimum streams pool memory limit.

## Syntax

```sql
DBMS_AQADM.GET_MIN_STREAMS_POOL (
   value     OUT      NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| value | NUMBER) | OUT | Value in megabytes. |

## Usage Notes

Syntax DBMS_AQADM.GET_MIN_STREAMS_POOL ( value OUT NUMBER); Parameters Table 23-36 GET_MIN_STREAMS_POOL Procedure Parameter Parameter Description value Value in megabytes.