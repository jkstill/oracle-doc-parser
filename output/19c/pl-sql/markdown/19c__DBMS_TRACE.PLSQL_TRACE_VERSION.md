---
id: 19c__DBMS_TRACE.PLSQL_TRACE_VERSION
name: DBMS_TRACE.PLSQL_TRACE_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRACE
tags: [dbms_trace]
source_file: DBMS_TRACE.html
---

# DBMS_TRACE.PLSQL_TRACE_VERSION

This procedure gets the version number of the trace package. It returns the major and minor version number of the DBMS_TRACE package.

## Syntax

```sql
DBMS_TRACE.PLSQL_TRACE_VERSION ( 
   major OUT BINARY_INTEGER, 
   minor OUT BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| major | BINARY_INTEGER | OUT | Major version number of DBMS_TRACE . |
| minor | BINARY_INTEGER) | OUT | Minor version number of DBMS_TRACE . |

## Usage Notes

Syntax DBMS_TRACE.PLSQL_TRACE_VERSION ( major OUT BINARY_INTEGER, minor OUT BINARY_INTEGER); Parameters Table 178-4 PLSQL_TRACE_VERSION Procedure Parameters Parameter Description major Major version number of DBMS_TRACE . minor Minor version number of DBMS_TRACE .