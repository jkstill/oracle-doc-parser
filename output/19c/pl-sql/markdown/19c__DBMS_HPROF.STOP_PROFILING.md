---
id: 19c__DBMS_HPROF.STOP_PROFILING
name: DBMS_HPROF.STOP_PROFILING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HPROF
tags: [dbms_hprof]
source_file: DBMS_HPROF.html
---

# DBMS_HPROF.STOP_PROFILING

This procedure stops profiler data collection in the user's session. This subprogram also has the side effect of flushing data collected so far in the session, and it signals the end of a run. When the STOP_PROFILING procedure returns CLOB, it contains the Real-Time Monitoring report for the profiler run.

## Syntax

```sql
DBMS_HPROF.STOP_PROFILING;


DBMS_HPROF.STOP_PROFILING
  RETURN CLOB;
```

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_HPROF.STOP_PROFILING; DBMS_HPROF.STOP_PROFILING RETURN CLOB; Examples Profiling with raw profiler data table DECLARE analyze_runid number; trace_id number; BEGIN -- create raw profiler data and analysis tables -- call create_tables with force_it =>FALSE (default) when -- raw profiler data and analysis tables do not exist already DBMS_HPROF.CREATE_TABLES; -- Start profiling -- Write raw profiler data in raw profiler data table trace_id := DBMS_HPROF.START_PROFILING; -- Run the procedure to be profiled test; -- Stop profiling DBMS_HPROF.STOP_PROFILING; -- analyzes trace_id entry in raw profiler data table and writes -- hierarchical profiler information in hprof’s analysis tables analyze_runid := DBMS_HPROF.ANALYZE(trace_id); END; /