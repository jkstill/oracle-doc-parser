---
id: 19c__DBMS_STATS.GET_SYSTEM_STATS
name: DBMS_STATS.GET_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_SYSTEM_STATS

This procedure gets system statistics from stattab , or from the dictionary if stattab is NULL .

## Syntax

```sql
DBMS_STATS.GET_SYSTEM_STATS (
   status    OUT  VARCHAR2,
   dstart    OUT  DATE,
   dstop     OUT  DATE,
   pname     IN   VARCHAR2,
   pvalue    OUT  NUMBER,
   stattab   IN   VARCHAR2 DEFAULT NULL, 
   statid    IN   VARCHAR2 DEFAULT NULL,
   statown   IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| status | VARCHAR2 | OUT | Output is one of the following: COMPLETED: AUTOGATHERING: MANUALGATHERING: BADSTATS: |
| dstart | DATE | OUT | Date when statistics gathering started. If status = MANUALGATHERING , the start date is returned. |
| dstop | DATE | OUT | Date when statistics gathering stopped. If status = COMPLETE , the finish date is returned. If status = AUTOGATHERING , the future finish date is returned. If status = BADSTATS , the must-finished-by date is returned. |
| pname | VARCHAR2 | IN | The parameter name to get, which can have one of the following values: iotfrspeed - I/O transfer speed in bytes for each millisecond ioseektim - seek time + latency time + operating system overhead time, in milliseconds sreadtim - average time to read single block (random read), in milliseconds mreadtim - average time to read an mbrc block at once (sequential read), in milliseconds cpuspeed - average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' INTERVAL ' or ' START ' and ' STOP ' options) cpuspeednw - average number of CPU cycles for each second, in millions, captured for the no-workload (statistics collected using ' NOWORKLOAD ' option. mbrc - average multiblock read count for sequential read, in blocks maxthr - maximum I/O system throughput, in bytes/second slavethr - average slave I/O throughput, in bytes/second |
| pvalue | NUMBER | OUT | Parameter value to get |
| stattab | VARCHAR2 | IN | Identifier of the user statistics table where the statistics will be obtained. If stattab is NULL , the statistics will be obtained from the dictionary. |
| statid | VARCHAR2 | IN | Optional identifier associated with the statistics saved in the stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.GET_SYSTEM_STATS ( status OUT VARCHAR2, dstart OUT DATE, dstop OUT DATE, pname IN VARCHAR2, pvalue OUT NUMBER, stattab IN VARCHAR2 DEFAULT NULL, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL); Parameters Table 171-68 GET_SYSTEM_STATS Procedure Parameters Parameter Description status Output is one of the following: COMPLETED: AUTOGATHERING: MANUALGATHERING: BADSTATS: dstart Date when statistics gathering started. If status = MANUALGATHERING , the start date is returned. dstop Date when statistics gathering stopped. If status = COMPLETE , the finish date is returned. If status = AUTOGATHERING , the future finish date is returned. If status = BADSTATS , the must-finished-by date is returned. pname The parameter name to get, which can have one of the following values: iotfrspeed - I/O transfer speed in bytes for each millisecond ioseektim - seek time + latency time + operating system overhead time, in milliseconds sreadtim - average time to read single block (random read), in milliseconds mreadtim - average time to read an mbrc block at once (sequential read), in milliseconds cpuspeed - average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' INTERVAL ' or ' START ' and ' STOP ' options) cpuspeednw - average number of CPU cycles for each second, in millions, captured for the no-workload (statistics collected using ' NOWORKLOAD ' option. mbrc - average multiblock read count for sequential read, in blocks maxthr - maximum I/O system throughput, in bytes/second slavethr - average slave I/O throughput, in bytes/second pvalue Parameter value to get stattab Identifier of the user statistics table where the statistics will be obtained. If stattab is NULL , the statistics will be obtained from the dictionary. statid Optional identifier associated with the statistics saved in the stattab statown Schema containing stattab (if different from current schema) Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20002 : Bad user statistics table; may need to be upgraded ORA-20003 : Unable to gather system statistics ORA-20004 : Parameter does not exist Usage Notes To run this procedure, you need the GATHER_SYSTEM_STATISTICS role.