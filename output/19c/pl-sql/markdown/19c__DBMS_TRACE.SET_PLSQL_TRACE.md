---
id: 19c__DBMS_TRACE.SET_PLSQL_TRACE
name: DBMS_TRACE.SET_PLSQL_TRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRACE
tags: [dbms_trace]
source_file: DBMS_TRACE.html
---

# DBMS_TRACE.SET_PLSQL_TRACE

This procedure enables PL/SQL trace data collection.

## Syntax

```sql
DBMS_TRACE.SET_PLSQL_TRACE ( 
   trace_level INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trace_level | TEGER) | IN | You must supply one or more of the constants as listed in Table 178-1 . By summing the constants, you can enable tracing of multiple PL/SQL language features simultaneously. The control constants " TRACE_PAUSE ", " TRACE_RESUME " and " TRACE_STOP " should not be used in combination with other constants. Also see DBMS_TRACE Operational Notes: Collecting Trace Data for more information. |

## Usage Notes

Syntax DBMS_TRACE.SET_PLSQL_TRACE ( trace_level INTEGER); Parameters Table 178-5 SET_PLSQL_TRACE Procedure Parameters Parameter Description trace_level You must supply one or more of the constants as listed in Table 178-1 . By summing the constants, you can enable tracing of multiple PL/SQL language features simultaneously. The control constants " TRACE_PAUSE ", " TRACE_RESUME " and " TRACE_STOP " should not be used in combination with other constants. Also see DBMS_TRACE Operational Notes: Collecting Trace Data for more information.