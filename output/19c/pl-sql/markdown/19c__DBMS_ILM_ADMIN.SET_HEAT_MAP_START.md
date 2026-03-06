---
id: 19c__DBMS_ILM_ADMIN.SET_HEAT_MAP_START
name: DBMS_ILM_ADMIN.SET_HEAT_MAP_START
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM_ADMIN
tags: [dbms_ilm_admin]
source_file: DBMS_ILM_ADMIN.html
---

# DBMS_ILM_ADMIN.SET_HEAT_MAP_START

This procedure sets the start date for collecting heat map data.

## Syntax

```sql
DBMS_ILM_ADMIN.SET_HEAT_MAP_START  (
   start_date  IN   DATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| start_date | DATE) | IN | Indicates the new date from which all statistics are valid |

## Usage Notes

Syntax DBMS_ILM_ADMIN.SET_HEAT_MAP_START ( start_date IN DATE); Parameters Table 87-7 SET_HEAT_MAP_START Procedure Parameters Parameter Description start_date Indicates the new date from which all statistics are valid