---
id: 19c__UTL_RECOMP.RECOMP_PARALLEL
name: UTL_RECOMP.RECOMP_PARALLEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RECOMP
tags: [utl_recomp]
source_file: UTL_RECOMP.html
---

# UTL_RECOMP.RECOMP_PARALLEL

This procedure uses the information exposed in the DBA_Dependencies view to recompile invalid objects in the database, or in a given schema, in parallel.

## Syntax

```sql
UTL_RECOMP.RECOMP_PARALLEL(
   threads  IN   PLS_INTEGER DEFAULT NULL,
   schema   IN   VARCHAR2    DEFAULT NULL,
   flags    IN   PLS_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| threads | PLS_INTEGER | IN | The number of recompile threads to run in parallel. If NULL , use the value of ' job_queue_processes '. |
| schema | VARCHAR2 | IN | The schema in which to recompile invalid objects. If NULL , all invalid objects in the database are recompiled. |
| flags | PLS_INTEGER | IN | Flag values are intended for internal testing and diagnosability only. |

## Usage Notes

Syntax UTL_RECOMP.RECOMP_PARALLEL( threads IN PLS_INTEGER DEFAULT NULL, schema IN VARCHAR2 DEFAULT NULL, flags IN PLS_INTEGER DEFAULT 0); Parameters Table 273-2 RECOMP_PARALLEL Procedure Parameters Parameter Description threads The number of recompile threads to run in parallel. If NULL , use the value of ' job_queue_processes '. schema The schema in which to recompile invalid objects. If NULL , all invalid objects in the database are recompiled. flags Flag values are intended for internal testing and diagnosability only. Usage Notes The parallel recompile exploits multiple CPUs to reduce the time taken to recompile invalid objects. However, please note that recompilation writes significant amounts of data to system tables, so the disk system may be a bottleneck and prevent significant speedups.