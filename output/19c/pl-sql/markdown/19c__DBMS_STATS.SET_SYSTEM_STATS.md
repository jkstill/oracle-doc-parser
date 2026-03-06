---
id: 19c__DBMS_STATS.SET_SYSTEM_STATS
name: DBMS_STATS.SET_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SET_SYSTEM_STATS

This procedure sets systems statistics.

## Syntax

```sql
DBMS_STATS.SET_SYSTEM_STATS (
   pname          VARCHAR2,
   pvalue         NUMBER,
   stattab   IN   VARCHAR2 DEFAULT NULL, 
   statid    IN   VARCHAR2 DEFAULT NULL,
   statown   IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2 | IN | The parameter name to get, which can have one of the following values: iotfrspeed —I/O transfer speed in bytes for each millisecond ioseektim - Seek time + latency time + operating system overhead time, in milliseconds sreadtim - Average time to read single block (random read), in milliseconds mreadtim - Average time to read an mbrc block at once (sequential read), in milliseconds cpuspeed - Average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' INTERVAL ' or ' START ' and ' STOP ' options) cpuspeednw - Average number of CPU cycles for each second, in millions, captured for the no-workload (statistics collected using ' NOWORKLOAD ' option. mbrc - Average multiblock read count for sequential read, in blocks maxthr - Maximum I/O system throughput, in bytes/second slavethr - Average slave I/O throughput, in bytes/second |
| pvalue | NUMBER | IN | Parameter value to get |
| stattab | VARCHAR2 | IN | Identifier of the user statistics table where the statistics will be obtained. If stattab is null, the statistics will be obtained from the dictionary. |
| statid | VARCHAR2 | IN | Optional identifier associated with the statistics saved in the stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.SET_SYSTEM_STATS ( pname VARCHAR2, pvalue NUMBER, stattab IN VARCHAR2 DEFAULT NULL, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL); Parameters Table 171-130 SET_SYSTEM_STATS Procedure Parameters Parameter Description pname The parameter name to get, which can have one of the following values: iotfrspeed —I/O transfer speed in bytes for each millisecond ioseektim - Seek time + latency time + operating system overhead time, in milliseconds sreadtim - Average time to read single block (random read), in milliseconds mreadtim - Average time to read an mbrc block at once (sequential read), in milliseconds cpuspeed - Average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' INTERVAL ' or ' START ' and ' STOP ' options) cpuspeednw - Average number of CPU cycles for each second, in millions, captured for the no-workload (statistics collected using ' NOWORKLOAD ' option. mbrc - Average multiblock read count for sequential read, in blocks maxthr - Maximum I/O system throughput, in bytes/second slavethr - Average slave I/O throughput, in bytes/second pvalue Parameter value to get stattab Identifier of the user statistics table where the statistics will be obtained. If stattab is null, the statistics will be obtained from the dictionary. statid Optional identifier associated with the statistics saved in the stattab statown Schema containing stattab (if different from current schema) Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid input value ORA-20002 : Bad user statistics table; may need to be upgraded ORA-20003 : Unable to set system statistics ORA-20004 : Parameter does not exist Usage Notes To run this procedure, you need the GATHER_SYSTEM_STATISTICS role.