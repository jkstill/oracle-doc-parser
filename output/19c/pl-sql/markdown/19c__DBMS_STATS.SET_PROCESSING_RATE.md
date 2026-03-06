---
id: 19c__DBMS_STATS.SET_PROCESSING_RATE
name: DBMS_STATS.SET_PROCESSING_RATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_PROCESSING_RATE

This procedure sets the value of rate of processing for a given operation.

## Syntax

```sql
DBMS_STATS.SET_PROCESSING_RATE (
   opname      IN    VARCHAR2, 
   procrate    IN    NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| opname | VARCHAR2 | IN | Name of the operation. |
| procrate | NUMBER) | IN | Processing rate. Valid values are as follows: AGGR ALL CPU CPU_ACCESS CPU_AGGR CPU_BYTES_PER_SEC CPU_FILTER CPU_GBY CPU_HASH_JOIN CPU_JOIN CPU_NL_JOIN CPU_RANDOM_ACCESS CPU_SEQUENTIAL_ACCESS CPU_SM_JOIN CPU_SORT HASH IO IO_ACCESS IO_BYTES_PER_SEC IO_RANDOM_ACCESS IO_SEQUENTIAL_ACCESS MEMCMP MEMCPY |

## Usage Notes

Syntax DBMS_STATS.SET_PROCESSING_RATE ( opname IN VARCHAR2, procrate IN NUMBER); Parameters Table 171-127 SET_PROCESSING_RATE Procedure Parameters Parameter Description opname Name of the operation. procrate Processing rate. Valid values are as follows: AGGR ALL CPU CPU_ACCESS CPU_AGGR CPU_BYTES_PER_SEC CPU_FILTER CPU_GBY CPU_HASH_JOIN CPU_JOIN CPU_NL_JOIN CPU_RANDOM_ACCESS CPU_SEQUENTIAL_ACCESS CPU_SM_JOIN CPU_SORT HASH IO IO_ACCESS IO_BYTES_PER_SEC IO_RANDOM_ACCESS IO_SEQUENTIAL_ACCESS MEMCMP MEMCPY Security Model You must have the OPTIMIZER_PROCESSING_RATE role to run this procedure. Usage Notes AUTO DOP uses processing rates to determine the optimal degree of parallelism for a SQL statement. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or illegal input value