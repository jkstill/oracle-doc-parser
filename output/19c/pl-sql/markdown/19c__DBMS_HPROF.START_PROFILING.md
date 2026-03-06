---
id: 19c__DBMS_HPROF.START_PROFILING
name: DBMS_HPROF.START_PROFILING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HPROF
tags: [dbms_hprof]
source_file: DBMS_HPROF.html
---

# DBMS_HPROF.START_PROFILING

This procedure starts hierarchical profiler data collection in the user's session.

## Syntax

```sql
DBMS_HPROF.START_PROFILING(
   max_depth     IN PLS_INTEGER DEFAULT NULL,
   sqlmonitor    IN BOOLEAN DEFAULT TRUE,
   run_comment   IN VARCHAR2 DEFAULT NULL)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| max_depth | PLS_INTEGER | IN | By default (that is, when max_depth value is NULL ) profile information is gathered for all functions irrespective of their call depth. When a non- NULL value is specified for max_depth , the profiler collects data only for functions up to a call depth level of max_depth . |
| sqlmonitor | BOOLEAN | IN | Generates a real-time monitoring report for a profiler run when the profiler run ends. The default value is TRUE . |
| run_comment | VARCHAR2 | IN | User provided comment for the profiler data collection run. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_HPROF.START_PROFILING( max_depth IN PLS_INTEGER DEFAULT NULL, sqlmonitor IN BOOLEAN DEFAULT TRUE, run_comment IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 83-4 START_PROFILING Procedure Parameters Parameter Description max_depth By default (that is, when max_depth value is NULL ) profile information is gathered for all functions irrespective of their call depth. When a non- NULL value is specified for max_depth , the profiler collects data only for functions up to a call depth level of max_depth . sqlmonitor Generates a real-time monitoring report for a profiler run when the profiler run ends. The default value is TRUE . run_comment User provided comment for the profiler data collection run. Return Values Unique run identifier for this profiler run. This can then be used to look up the results corresponding to this run from the hierarchical profiler tables. Usage Notes Even though the profiler does not individually track functions at depth greater than max_depth , the time spent in such functions is charged to the ancestor function at depth max_depth . Raw profiler data is generated in the raw profiler data table with an unique trace_id . The unique trace_id is used to manage the raw profiler output stored in the raw profiler data table.