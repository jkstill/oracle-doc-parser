---
id: 19c__DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER
name: DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER

This procedure sets an advanced parameter for replay besides the ones used with the PREPARE_REPLAY Procedure.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   VARCHAR2);

DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   NUMBER);

DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2 | IN | Name of the parameter (case insensitive) |
| pvalue | VARCHAR2) | IN | Value of the parameter |

## Usage Notes

The advanced parameters control aspects of the replay that are more specialized. The advanced parameters are reset to their default values after the replay has finished. Syntax DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( pname IN VARCHAR2, pvalue IN VARCHAR2); DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( pname IN VARCHAR2, pvalue IN NUMBER); DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( pname IN VARCHAR2, pvalue IN BOOLEAN); Parameters Table 191-32 SET_ADVANCED_PARAMETER Procedure Parameters Parameter Description pname Name of the parameter (case insensitive) pvalue Value of the parameter Usage Notes The current parameters and values that can be used are: 'DO_NO_WAIT_COMMITS': (default: FALSE) This parameter controls whether the COMMIT issued by replay sessions is NOWAIT . The default value for this parameter is FALSE . In this case all the COMMIT s are issued with the mode they were captured ( wait , no-wait , batch , no-batch ). If the parameter is set to TRUE , then all COMMIT s are issued in no-wait mode. This is useful in cases where the replay is becoming noticeably slow because of a high volume of concurrent COMMIT s. Setting the parameter to TRUE will significantly decrease the waits on the 'log file sync' event during the replay with respect to capture.