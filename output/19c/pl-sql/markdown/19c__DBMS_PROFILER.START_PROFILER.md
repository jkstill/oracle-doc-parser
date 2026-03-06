---
id: 19c__DBMS_PROFILER.START_PROFILER
name: DBMS_PROFILER.START_PROFILER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER.START_PROFILER

This function starts profiler data collection in the user's session.

## Syntax

```sql
DBMS_PROFILER.START_PROFILER(
   run_comment   IN VARCHAR2 := sysdate,
   run_comment1  IN VARCHAR2 :='',
   run_number    OUT BINARY_INTEGER)
 RETURN BINARY_INTEGER;

DBMS_PROFILER.START_PROFILER(
   run_comment IN VARCHAR2 := sysdate,
   run_comment1 IN VARCHAR2 :='')
RETURN BINARY_INTEGER;

DBMS_PROFILER.START_PROFILER(
   run_comment   IN VARCHAR2 := sysdate,
   run_comment1  IN VARCHAR2 :='',
   run_number    OUT BINARY_INTEGER);

DBMS_PROFILER.START_PROFILER(
   run_comment IN VARCHAR2 := sysdate,
   run_comment1 IN VARCHAR2 :='');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| run_comment | VARCHAR2 | IN | Each profiler run can be associated with a comment. For example, the comment could provide the name and version of the benchmark test that was used to collect data. |
| run_number | BINARY_INTEGER) | OUT | Stores the number of the run so you can store and later recall the run's data. |
| run_comment1 | VARCHAR2 | IN | Allows you to make interesting comments about the run. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

There are two overloaded forms of the START_PROFILER function; one returns the run number of the started run, as well as the result of the call. The other does not return the run number. The first form is intended for use with GUI-based tools controlling the profiler. Syntax DBMS_PROFILER.START_PROFILER( run_comment IN VARCHAR2 := sysdate, run_comment1 IN VARCHAR2 :='', run_number OUT BINARY_INTEGER) RETURN BINARY_INTEGER; DBMS_PROFILER.START_PROFILER( run_comment IN VARCHAR2 := sysdate, run_comment1 IN VARCHAR2 :='') RETURN BINARY_INTEGER; DBMS_PROFILER.START_PROFILER( run_comment IN VARCHAR2 := sysdate, run_comment1 IN VARCHAR2 :='', run_number OUT BINARY_INTEGER); DBMS_PROFILER.START_PROFILER( run_comment IN VARCHAR2 := sysdate, run_comment1 IN VARCHAR2 :=''); Parameters Table 133-7 START_PROFILER Function Parameters Parameter Description run_comment Each profiler run can be associated with a comment. For example, the comment could provide the name and version of the benchmark test that was used to collect data. run_number Stores the number of the run so you can store and later recall the run's data. run_comment1 Allows you to make interesting comments about the run.