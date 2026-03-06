---
id: 19c__DBMS_PROFILER.GET_VERSION
name: DBMS_PROFILER.GET_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER.GET_VERSION

This procedure gets the version of this API.

## Syntax

```sql
DBMS_PROFILER.GET_VERSION ( 
   major  OUT BINARY_INTEGER, 
   minor  OUT BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| major | BINARY_INTEGER | OUT | Major version of DBMS_PROFILER . |
| minor | BINARY_INTEGER) | OUT | Minor version of DBMS_PROFILER . |

## Usage Notes

Syntax DBMS_PROFILER.GET_VERSION ( major OUT BINARY_INTEGER, minor OUT BINARY_INTEGER); Parameters Table 133-6 GET_VERSION Procedure Parameters Parameter Description major Major version of DBMS_PROFILER . minor Minor version of DBMS_PROFILER .