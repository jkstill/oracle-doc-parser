---
id: 19c__DBMS_DEBUG.PROBE_VERSION
name: DBMS_DEBUG.PROBE_VERSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.PROBE_VERSION

This procedure returns the version number of DBMS_DEBUG on the server.

## Syntax

```sql
DBMS_DEBUG.PROBE_VERSION (
   major out BINARY_INTEGER,
   minor out BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| major | BINARY_INTEGER | out | Major version number |
| minor | BINARY_INTEGER) | out | Minor version number: increments as functionality is added |

## Usage Notes

Syntax DBMS_DEBUG.PROBE_VERSION ( major out BINARY_INTEGER, minor out BINARY_INTEGER); Parameters Table 57-40 PROBE_VERSION Procedure Parameters Parameter Description major Major version number minor Minor version number: increments as functionality is added