---
id: 19c__DBMS_DEBUG.GET_MORE_SOURCE
name: DBMS_DEBUG.GET_MORE_SOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_MORE_SOURCE

When the source does not fit in the buffer provided by the SHOW_SOURCE Procedure version which produced a formatted buffer, this procedure provides additional source.

## Syntax

```sql
DBMS_DEBUG.GET_MORE_SOURCE (
   buffer          IN OUT VARCHAR2,
   buflen          IN BINARY_INTEGER,
   piece#          IN BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buffer | VARCHAR2 | IN OUT | The buffer |
| buflen | BINARY_INTEGER | IN | The length of the buffer |
| piece# | BINARY_INTEGER) | IN | A value between 2 and the value returned in the parameter pieces from the call to the relevant version of the SHOW_SOURCE Procedures |

## Usage Notes

Syntax DBMS_DEBUG.GET_MORE_SOURCE ( buffer IN OUT VARCHAR2, buflen IN BINARY_INTEGER, piece# IN BINARY_INTEGER); Parameters Table 57-27 GET_MORE_SOURCE Procedure Parameters Parameter Description buffer The buffer buflen The length of the buffer piece# A value between 2 and the value returned in the parameter pieces from the call to the relevant version of the SHOW_SOURCE Procedures Usage Notes This procedure should be called only after the version of SHOW_SOURCE that returns a formatted buffer.