---
id: 19c__UTL_RECOMP
name: UTL_RECOMP
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RECOMP
tags: [utl_recomp]
source_file: UTL_RECOMP.html
---

# UTL_RECOMP

These examples show various ways that UTL_RECOMP can recompile objects.

## Syntax

```sql
EXECUTE UTL_RECOMP.RECOMP_SERIAL();
```

## Usage Notes

Recompile all objects sequentially: EXECUTE UTL_RECOMP.RECOMP_SERIAL(); Recompile objects in schema SCOTT sequentially: EXECUTE UTL_RECOMP.RECOMP_SERIAL('SCOTT'); Recompile all objects using 4 parallel threads: EXECUTE UTL_RECOMP.RECOMP_PARALLEL(4); Recompile objects in schema JOE using the number of threads specified in the parameter JOB_QUEUE_PROCESSES : EXECUTE UTL_RECOMP.RECOMP_PARALLEL(NULL, 'JOE');