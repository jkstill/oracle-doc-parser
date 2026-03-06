---
id: 19c__DBMS_STATS.GATHER_SYSTEM_STATS
name: DBMS_STATS.GATHER_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GATHER_SYSTEM_STATS

This procedure gathers system statistics.

## Syntax

```sql
DBMS_STATS.GATHER_SYSTEM_STATS (
   gathering_mode   VARCHAR2 DEFAULT 'NOWORKLOAD',
   interval         INTEGER  DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL,
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| gathering_mode | VARCHAR2 | IN | Specifies the mode in which the database gathers system statistics. Possible values are: NOWORKLOAD The database captures performance characteristics of the I/O system. Gathering may take a few minutes and depends on the size of the database. During this period, the database estimates the average read seek time and transfer speed for the I/O system. This mode is suitable for the all workloads. To fine tune system statistics for the workload, use START and STOP or the INTERVAL option. If you gather both NOWORKLOAD and workload-specific statistics (statistics collected using INTERVAL or START and STOP ), the optimizer uses the workload statistics. Collected components include cpuspeednw , ioseektim , and iotfrspeed . INTERVAL The database captures system activity during a specified interval in minutes. This parameter works in combination with the interval parameter. The database creates or updates system statistics in the dictionary or stattab . You can use GATHER_SYSTEM_STATS (gathering_mode=>'STOP') to stop gathering earlier than scheduled. Collected components include maxthr , slavethr , cpuspeed , sreadtim , mreadtim , and mbrc . START | STOP The database captures system activity during specified start and stop times and refreshes the dictionary or stattab with statistics for the elapsed period. The database ignores the INTERVAL value. Collected components include maxthr , slavethr , cpuspeed , sreadtim , mreadtim , and mbrc . EXADATA In this mode, gathered system statistics take into account the unique capabilities of Oracle Exadata, such as large I/O size and high I/O throughput. The database sets multiblock read count and I/O throughput statistics along with CPU speed. |
| interval | TEGER | IN | Specifies the number of minutes in which to gather system statistics. This parameter applies only when gathering_mode='INTERVAL' . |
| stattab | VARCHAR2 | IN | Specifies the table in which the database stores the statistics. |
| statid | VARCHAR2 | IN | Specifies an optional identifier associated with the statistics saved in stattab . |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab , if different from the current schema. |

## Usage Notes

Syntax DBMS_STATS.GATHER_SYSTEM_STATS ( gathering_mode VARCHAR2 DEFAULT 'NOWORKLOAD', interval INTEGER DEFAULT NULL, stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-58 GATHER_SYSTEM_STATS Procedure Parameters Parameter Description gathering_mode Specifies the mode in which the database gathers system statistics. Possible values are: NOWORKLOAD The database captures performance characteristics of the I/O system. Gathering may take a few minutes and depends on the size of the database. During this period, the database estimates the average read seek time and transfer speed for the I/O system. This mode is suitable for the all workloads. To fine tune system statistics for the workload, use START and STOP or the INTERVAL option. If you gather both NOWORKLOAD and workload-specific statistics (statistics collected using INTERVAL or START and STOP ), the optimizer uses the workload statistics. Collected components include cpuspeednw , ioseektim , and iotfrspeed . INTERVAL The database captures system activity during a specified interval in minutes. This parameter works in combination with the interval parameter. The database creates or updates system statistics in the dictionary or stattab . You can use GATHER_SYSTEM_STATS (gathering_mode=>'STOP') to stop gathering earlier than scheduled. Collected components include maxthr , slavethr , cpuspeed , sreadtim , mreadtim , and mbrc . START | STOP The database captures system activity during specified start and stop times and refreshes the dictionary or stattab with statistics for the elapsed period. The database ignores the INTERVAL value. Collected components include maxthr , slavethr , cpuspeed , sreadtim , mreadtim , and mbrc . EXADATA In this mode, gathered system statistics take into account the unique capabilities of Oracle Exadata, such as large I/O size and high I/O throughput. The database sets multiblock read count and I/O throughput statistics along with CPU speed. interval Specifies the number of minutes in which to gather system statistics. This parameter applies only when gathering_mode='INTERVAL' . stattab Specifies the table in which the database stores the statistics. statid Specifies an optional identifier associated with the statistics saved in stattab . statown Specifies the schema containing stattab , if different from the current schema. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid input value ORA-20002 : Bad user statistics table; may need to be upgraded ORA-20003 : Unable to gather system statistics ORA-20004 : Error in the INTERVAL mode: system parameter job_queue_processes must be >0 Usage Notes To run this procedure, you must have the GATHER_SYSTEM_STATISTICS role. Examples Assume that you want to perform database application processing OLTP transactions during the day and run reports at night. To collect daytime system statistics, gather statistics for 720 minutes. Store the statistics in the MYSTATS table. BEGIN DBMS_STATS.GATHER_SYSTEM_STATS ( interval => 720, stattab => 'mystats', statid => 'OLTP'); END; To collect nighttime system statistics, gather statistics for 720 minutes. Store the statistics in the MYSTATS table. BEGIN DBMS_STATS.GATHER_SYSTEM_STATS ( interval => 720, stattab => 'mystats', statid => 'OLAP'); END; Update the dictionary with the gathered statistics. VARIABLE jobno number; BEGIN DBMS_JOB.SUBMIT (:jobno, 'DBMS_STATS.IMPORT_SYSTEM_STATS (''mystats'',''OLTP'');' sysdate, 'sysdate + 1'); COMMIT; END; BEGIN DBMS_JOB.SUBMIT (:jobno, 'DBMS_STATS.IMPORT_SYSTEM_STATS (''mystats'',''OLAP'');' sysdate + 0.5, 'sysdate + 1'); COMMIT; END;