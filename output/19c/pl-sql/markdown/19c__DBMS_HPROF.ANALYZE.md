---
id: 19c__DBMS_HPROF.ANALYZE
name: DBMS_HPROF.ANALYZE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HPROF
tags: [dbms_hprof]
source_file: DBMS_HPROF.html
---

# DBMS_HPROF.ANALYZE

This function analyzes the raw profiler output and produces hierarchical profiler information in database tables or generates out-of-the-box HTML reports.

## Syntax

```sql
DBMS_HPROF.ANALYZE (
   trace_id         IN NUMBER,
   summary_mode     IN BOOLEAN DEFAULT FALSE,
   trace            IN VARCHAR2 DEFAULT NULL,
   skip             IN PLS_INTEGER DEFAULT 0,
   collect          IN PLS_INTEGER DEFAULT NULL,
   run_comment      IN VARCHAR2 DEFAULT NULL)
  RETURN NUMBER;

DBMS_HPROF.ANALYZE (
   trace_id         IN NUMBER,
   report_clob      OUT CLOB,
   trace            IN VARCHAR2 DEFAULT NULL,
   skip             IN PLS_INTEGER DEFAULT 0,
   collect          IN PLS_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trace_id | NUMBER | IN | The trace_id of the raw profiler data entry in the raw profiler data table ( dbmshp_trace_data ). |
| summary_mode | BOOLEAN | IN | By default (that is, when summary_mode is FALSE ), a detailed analysis is done. When summary_mode is TRUE , only top-level summary information is generated into the database table. |
| report_clob | CLOB | OUT | The analyzed HTML report. |
| trace | VARCHAR2 | IN | Analyzes only the subtrees rooted at the specified trace entry. By default (when trace is NULL ), the analysis/reporting is generated for the entire run. The trace entry must be specified in a special quoted qualified format. For example, '" HR "." PKG "." FOO "' or '"".""." __plsql_vm "'. If multiple overloads exist for the specified name, all of them will be analyzed. |
| skip | PLS_INTEGER | IN | Used only when trace is specified. Analyze only the subtrees rooted at the specified trace, but ignore the first skip invocations to trace. The default value for skip is 0 . |
| collect | PLS_INTEGER | IN | Used only when trace is specified. Analyze collect number of invocations of traces (starting from skip +1'th invocation). By default, only 1 invocation is collected. |
| run_comment | VARCHAR2 | IN | User-provided comment for this run. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_HPROF.ANALYZE ( trace_id IN NUMBER, summary_mode IN BOOLEAN DEFAULT FALSE, trace IN VARCHAR2 DEFAULT NULL, skip IN PLS_INTEGER DEFAULT 0, collect IN PLS_INTEGER DEFAULT NULL, run_comment IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; DBMS_HPROF.ANALYZE ( trace_id IN NUMBER, report_clob OUT CLOB, trace IN VARCHAR2 DEFAULT NULL, skip IN PLS_INTEGER DEFAULT 0, collect IN PLS_INTEGER DEFAULT NULL); Parameters Table 83-2 ANALYZE Function Parameters Parameter Description trace_id The trace_id of the raw profiler data entry in the raw profiler data table ( dbmshp_trace_data ). summary_mode By default (that is, when summary_mode is FALSE ), a detailed analysis is done. When summary_mode is TRUE , only top-level summary information is generated into the database table. report_clob The analyzed HTML report. trace Analyzes only the subtrees rooted at the specified trace entry. By default (when trace is NULL ), the analysis/reporting is generated for the entire run. The trace entry must be specified in a special quoted qualified format. For example, '" HR "." PKG "." FOO "' or '"".""." __plsql_vm "'. If multiple overloads exist for the specified name, all of them will be analyzed. skip Used only when trace is specified. Analyze only the subtrees rooted at the specified trace, but ignore the first skip invocations to trace. The default value for skip is 0 . collect Used only when trace is specified. Analyze collect number of invocations of traces (starting from skip +1'th invocation). By default, only 1 invocation is collected. run_comment User-provided comment for this run. Return Values A unique run identifier for this run of the analyzer. This can then be used to look up the results corresponding to this run from the hierarchical profiler tables. Usage Notes Use the DBMS_HPROF.CREATE_TABLES subprogram to create the hierarchical profiler database tables and other data structures required for persistently storing the results of analyzing the raw profiler data. Calling the DBMS_HPROF.CREATE_TABLES with default value ( FALSE ) will raise error if table already exists. Use DBMS_HPROF.CREATE_TABLES(TRUE) to drop any previously created hierarchical profiler tables. Use the DBMS_HPROF.CREATE_TABLES to drop any previously created hierarchical profiler tables. By default, force_it is FALSE ; therefore, to drop any previously created hierarchical profiler tables you must set the value of force_it to TRUE . If trace_id entry is NULL , error is raised. If trace_id entry in the raw profiler data table does not exist, error is raised. If raw data of the trace_id entry in the raw profiler data table is NULL or is zero size, error is raised. Examples The following snippet installs the hierarchical profiler tables in HR schema. connect HR/ <password> ; The following example analyzes and generates HTML CLOB report from a raw profiler data table. DECLARE reportclob clob; trace_id number; BEGIN -- create raw profiler data and analysis tables -- force_it =>TRUE will dropped the tables if table exists DBMS_HPROF.CREATE_TABLES(force_it =>TRUE); -- Start profiling -- Write raw profiler data in raw profiler data table trace_id := DBMS_HPROF.START_PROFILING; -- Run procedure to be profiled test; -- Stop profiling DBMS_HPROF.STOP_PROFILING; -- analyzes trace_id entry in raw profiler data table and produce -- analyzed HTML report in reportclob DBMS_HPROF.ANALYZE(trace_id , reportclob); END; /