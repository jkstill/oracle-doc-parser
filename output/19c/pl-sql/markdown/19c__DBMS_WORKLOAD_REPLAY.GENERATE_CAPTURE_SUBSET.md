---
id: 19c__DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET
name: DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET

This procedure creates a new capture from an existing workload capture.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET (
   input_capture_dir          IN   VARCHAR2,
   output_capture_dir         IN   VARCHAR2,
   new_capture_name           IN   VARCHAR2,
   begin_time                 IN   NUMBER,
   begin_include_incomplete   IN   BOOLEAN DEFAULT TRUE,
   end_time                   IN   NUMBER,
   end_include_incomplete     IN   BOOLEAN DEFAULT FALSE,
   parallel_level             IN   NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| input_capture_dir | VARCHAR2 | IN | (Mandatory) Name of the directory object that points to an existing workload capture |
| output_capture_dir | VARCHAR2 | IN | (Mandatory) Name of the directory object that points to the new capture |
| new_capture_name | VARCHAR2 | IN | (Mandatory) Name of new capture |
| begin_time | NUMBER | IN | Start of the time range - time offset in seconds from the start of a workload capture |
| begin_include_incomplete | BOOLEAN | IN | Column to include incomplete calls caused by begin_time |
| end_time | NUMBER | IN | End of the time range - time offset in seconds from the start of a workload capture. If end_time is zero or end_time is less or equal than begin_time , the time range is invalid. The new capture will use the whole duration of the input capture. |
| end_include_incomplete | BOOLEAN | IN | Column to include incomplete calls caused by end_time |
| parallel_level | NUMBER | IN | Number of Oracle processes used to process the input captures in a parallel fashion. The NULL default value will auto-compute the parallelism level based on number of CPUs, whereas a value of 1 will enforce serial execution. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET ( input_capture_dir IN VARCHAR2, output_capture_dir IN VARCHAR2, new_capture_name IN VARCHAR2, begin_time IN NUMBER, begin_include_incomplete IN BOOLEAN DEFAULT TRUE, end_time IN NUMBER, end_include_incomplete IN BOOLEAN DEFAULT FALSE, parallel_level IN NUMBER DEFAULT NULL); Parameters Table 191-15 GENERATE_CAPTURE_SUBSET Procedure Parameters Parameter Description input_capture_dir (Mandatory) Name of the directory object that points to an existing workload capture output_capture_dir (Mandatory) Name of the directory object that points to the new capture new_capture_name (Mandatory) Name of new capture begin_time Start of the time range - time offset in seconds from the start of a workload capture begin_include_incomplete Column to include incomplete calls caused by begin_time end_time End of the time range - time offset in seconds from the start of a workload capture. If end_time is zero or end_time is less or equal than begin_time , the time range is invalid. The new capture will use the whole duration of the input capture. end_include_incomplete Column to include incomplete calls caused by end_time parallel_level Number of Oracle processes used to process the input captures in a parallel fashion. The NULL default value will auto-compute the parallelism level based on number of CPUs, whereas a value of 1 will enforce serial execution.