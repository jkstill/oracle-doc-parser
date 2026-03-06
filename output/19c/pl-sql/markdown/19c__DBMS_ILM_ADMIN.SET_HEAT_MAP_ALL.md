---
id: 19c__DBMS_ILM_ADMIN.SET_HEAT_MAP_ALL
name: DBMS_ILM_ADMIN.SET_HEAT_MAP_ALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM_ADMIN
tags: [dbms_ilm_admin]
source_file: DBMS_ILM_ADMIN.html
---

# DBMS_ILM_ADMIN.SET_HEAT_MAP_ALL

This procedure sets an HTTP request header. The request header is sent to the Web server as soon as it is set.

## Syntax

```sql
DBMS_ILM_ADMIN.SET_HEAT_MAP_ALL  (
   access_date            IN DATE,
   segment_access_summary IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| access_date | DATE | IN | Date for the entry in HEAT_MAP_STAT$ to be added |
| segment_access_summary | NUMBER) | IN | Summary of segment access constants indicating access operations performed on the segment |

## Usage Notes

Syntax DBMS_ILM_ADMIN.SET_HEAT_MAP_ALL ( access_date IN DATE, segment_access_summary IN NUMBER); Parameters Table 87-6 SET_HEAT_MAP_ALL Procedure Parameters Parameter Description access_date Date for the entry in HEAT_MAP_STAT$ to be added segment_access_summary Summary of segment access constants indicating access operations performed on the segment