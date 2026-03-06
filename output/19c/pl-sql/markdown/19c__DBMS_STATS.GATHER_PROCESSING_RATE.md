---
id: 19c__DBMS_STATS.GATHER_PROCESSING_RATE
name: DBMS_STATS.GATHER_PROCESSING_RATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GATHER_PROCESSING_RATE

This procedure starts the job of gathering the processing rates which end after an interval defined in minutes.

## Syntax

```sql
DBMS_STATS.GATHER_PROCESSING_RATE (
   gathering_mode      IN    VARCHAR2  DEFAULT 'START',
   interval            IN    NUMBER    DEFAULT  NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| gathering_mode | VARCHAR2 | IN | Mode: 'START' or 'END' . The mode is based on the Active Session History (ASH) data when invoked with 'START' option. It stops gathering when invoked with 'END' option. When invoked with 'START' , 'interval' option can be specified optionally. If interval is not specified, its default value is set to 60 minutes. |
| interval | NUMBER | IN | Time interval (number of minutes) for which the processing must be gathered |

## Usage Notes

Syntax DBMS_STATS.GATHER_PROCESSING_RATE ( gathering_mode IN VARCHAR2 DEFAULT 'START', interval IN NUMBER DEFAULT NULL); Parameters Table 171-56 GATHER_PROCESSING_RATE Procedure Parameters Parameter Description gathering_mode Mode: 'START' or 'END' . The mode is based on the Active Session History (ASH) data when invoked with 'START' option. It stops gathering when invoked with 'END' option. When invoked with 'START' , 'interval' option can be specified optionally. If interval is not specified, its default value is set to 60 minutes. interval Time interval (number of minutes) for which the processing must be gathered Usage Notes You require the OPTIMIZER_PROCESSING_RATE role to run this procedure. AUTO DOP uses processing rates to determine the optimal degree of parallelism for a SQL statement. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or illegal input value