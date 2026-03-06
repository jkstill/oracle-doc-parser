---
id: 19c__DBMS_WORKLOAD_REPLAY.CALIBRATE
name: DBMS_WORKLOAD_REPLAY.CALIBRATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.CALIBRATE

This function operates on a processed workload capture directory to estimate the number of hosts and workload replay clients needed to faithfully replay the given workload. This function returns the results as an XML CLOB .

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.CALIBRATE (
   capture_dir          IN VARCHAR2,
   process_per_cpu      IN BINARY_INTEGER DEFAULT 4,
   threads_per_process  IN BINARY_INTEGER DEFAULT 50)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_dir | VARCHAR2 | IN | Name of the directory object that points to the (case sensitive) OS directory that contains processed capture data |
| process_per_cpu | BINARY_INTEGER | IN | Maximum number of processes allowed for each CPU (default is 4) |
| threads_per_process | BINARY_INTEGER | IN | Maximum number of threads allowed for each process (default is 50) |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.CALIBRATE ( capture_dir IN VARCHAR2, process_per_cpu IN BINARY_INTEGER DEFAULT 4, threads_per_process IN BINARY_INTEGER DEFAULT 50) RETURN CLOB; Parameters Table 191-7 CALIBRATE Function Parameters Parameter Description capture_dir Name of the directory object that points to the (case sensitive) OS directory that contains processed capture data process_per_cpu Maximum number of processes allowed for each CPU (default is 4) threads_per_process Maximum number of threads allowed for each process (default is 50) Return Values Returns a CLOB formatted as XML that contains: Information about the capture Current database version Input parameters to this function Number of CPUs and replay clients needed to replay the given workload Information about the sessions captured (total number and maximum concurrency) Usage Notes Prerequisite: The input workload capture was already processed using the PROCESS_CAPTURE Procedure in the same database version. This procedure will return the same results as the workload replay client in calibrate mode, which can be run as follows. $ wrc mode=calibrate replaydir=