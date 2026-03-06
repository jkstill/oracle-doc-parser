---
id: 19c__DBMS_AQADM.SET_MIN_STREAMS_POOL
name: DBMS_AQADM.SET_MIN_STREAMS_POOL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.SET_MIN_STREAMS_POOL

This procedure is used for Oracle Database AQ to specify and limit minimum streams pool memory use.

## Syntax

```sql
DBMS_AQADM.SET_MIN_STREAMS_POOL (
   value     IN      NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| value | NUMBER) | IN | Value in megabytes. |

## Usage Notes

Syntax DBMS_AQADM.SET_MIN_STREAMS_POOL ( value IN NUMBER); Parameters Table 23-54 SET_MIN_STREAMS_POOL Procedure Parameter Parameter Description value Value in megabytes.