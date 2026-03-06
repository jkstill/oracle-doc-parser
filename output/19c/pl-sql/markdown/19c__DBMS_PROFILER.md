---
id: 19c__DBMS_PROFILER
name: DBMS_PROFILER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER

DBMS_PROFILER throws the exceptions described in this topic.

## Syntax

```sql
error_param constant binary_integer := 1;
```

## Usage Notes

A 0 return value from any function denotes successful completion; a nonzero return value denotes an error condition. The possible errors are as follows: 'A subprogram was called with an incorrect parameter.' error_param constant binary_integer := 1; 'Data flush operation failed. Check whether the profiler tables have been created, are accessible, and that there is adequate space.' error_io constant binary_integer := 2; There is a mismatch between package and database implementation. Oracle returns this error if an incorrect version of the DBMS_PROFILER package is installed, and if the version of the profiler package cannot work with this database version. The only recovery is to install the correct version of the package. error_version constant binary_integer := -1;