---
id: 19c__DBMS_STATS.DELETE_PROCESSING_RATE
name: DBMS_STATS.DELETE_PROCESSING_RATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DELETE_PROCESSING_RATE

This procedure deletes the processing rate of a given statistics source. If the source is not specified, it deletes the statistics of all the sources.

## Syntax

```sql
DBMS_STATS.DELETE_PROCESSING_RATE (
   stat_source      IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stat_source | VARCHAR2 | IN | Source of processing rates: 'MANUAL' : values set by the user manually using the SET_PROCESSING_RATE Procedure 'CALIBRATION' : values collected by the calibration GATHER_PROCESSING_RATE Procedure run explicitly by the user 'FEEDBACK' : values obtained by time feedback |

## Usage Notes

Syntax DBMS_STATS.DELETE_PROCESSING_RATE ( stat_source IN VARCHAR2 DEFAULT NULL); Parameters Table 171-25 DELETE_PROCESSING_RATE Procedure Parameters Parameter Description stat_source Source of processing rates: 'MANUAL' : values set by the user manually using the SET_PROCESSING_RATE Procedure 'CALIBRATION' : values collected by the calibration GATHER_PROCESSING_RATE Procedure run explicitly by the user 'FEEDBACK' : values obtained by time feedback Usage Notes You require the OPTIMIZER_PROCESSING_RATE role to run this procedure since AUTO DOP uses processing rates to determine the optimal degree of parallelism for a SQL statement. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or illegal input value