---
id: 19c__DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY
name: DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY

Similar to the PREPARE_REPLAY Procedure, this procedure puts the database in a special "Prepare" mode for a multiple-capture replay. The difference is that this subprogram should be used only for consolidated replays.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY (
   synchronization           IN BOOLEAN,
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);

DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY (
   synchronization           IN VARCHAR2  DEFAULT 'SCN',
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| synchronization | BOOLEAN | IN | Sets the synchronization mode for replay: ‘TIME’ — The synchronization will be based on the time the action took place during capture (clock-based time). ‘SCN’ — The synchronization will be based on the capture-time commits; the commit order will be preserved during replay. This is the default mode. ‘OBJECT_ID’ — Every replayed action will be executed only after the relevant commits have finished execution. The relevant commits are those that were issued before the given action in the captured workload and that modified at least one of the database objects the given action is referencing (either implicitly or explicitly). This synchronization mode makes sure that any replay action will see the same data that the action saw during capture, but allows greater concurrency for the actions that do not touch the same objects/tables. This value is deprecated. For compatibility, an overloaded version of this procedure uses BOOLEAN for this parameter: TRUE means ‘SCN’ FALSE means ‘TIME’ |
| connect_time_scale | NUMBER | IN | Scales the time elapsed between the instant the workload capture was started and the session connects with the given value. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. DEFAULT VALUE is 100. See " Example 191-1 " . |
| think_time_scale | NUMBER | IN | Scales the time elapsed between two successive user calls " Example 191-1 " from the same session. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. DEFAULT VALUE is 100. See " Example 191-2 " . |
| think_time_auto_correct | BOOLEAN | IN | Auto corrects the think time between calls appropriately when user calls takes longer to complete during replay than during the original capture. DEFAULT is TRUE which is to reduce think time if replay goes slower than capture. See " Example 191-3 " . |
| capture_sts | BOOLEAN | IN | If this parameter is TRUE , then a SQL tuning set capture is also started in parallel with workload replay. The resulting SQL tuning set can be exported using the EXPORT_AWR Procedure along with the Automatic Workload Repository (AWR) data. Currently, parallel SQL tuning set (STS) capture is not supported in an Oracle RAC environment. So, this parameter has no effect in that context. The calling user must have the appropriate privileges (' ADMINISTER SQL TUNING SET '). The default value is FALSE . |
| sts_cap_interval | NUMBER | IN | Specifies the capture interval of the SQL set capture from the cursor cache in seconds. The default value is 300. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY ( synchronization IN BOOLEAN, connect_time_scale IN NUMBER DEFAULT 100, think_time_scale IN NUMBER DEFAULT 100, think_time_auto_correct IN BOOLEAN DEFAULT TRUE, capture_sts IN BOOLEAN DEFAULT FALSE, sts_cap_interval IN NUMBER DEFAULT 300); DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY ( synchronization IN VARCHAR2 DEFAULT 'SCN', connect_time_scale IN NUMBER DEFAULT 100, think_time_scale IN NUMBER DEFAULT 100, think_time_auto_correct IN BOOLEAN DEFAULT TRUE, capture_sts IN BOOLEAN DEFAULT FALSE, sts_cap_interval IN NUMBER DEFAULT 300); Parameters Table 191-24 PREPARE_CONSOLIDATED_REPLAY Procedure Parameters Parameter Description synchronization Sets the synchronization mode for replay: ‘TIME’ — The synchronization will be based on the time the action took place during capture (clock-based time). ‘SCN’ — The synchronization will be based on the capture-time commits; the commit order will be preserved during replay. This is the default mode. ‘OBJECT_ID’ — Every replayed action will be executed only after the relevant commits have finished execution. The relevant commits are those that were issued before the given action in the captured workload and that modified at least one of the database objects the given action is referencing (either implicitly or explicitly). This synchronization mode makes sure that any replay action will see the same data that the action saw during capture, but allows greater concurrency for the actions that do not touch the same objects/tables. This value is deprecated. For compatibility, an overloaded version of this procedure uses BOOLEAN for this parameter: TRUE means ‘SCN’ FALSE means ‘TIME’ connect_time_scale Scales the time elapsed between the instant the workload capture was started and the session connects with the given value. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. DEFAULT VALUE is 100. See " Example 191-1 " . think_time_scale Scales the time elapsed between two successive user calls " Example 191-1 " from the same session. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. DEFAULT VALUE is 100. See " Example 191-2 " . think_time_auto_correct Auto corrects the think time between calls appropriately when user calls takes longer to complete during replay than during the original capture. DEFAULT is TRUE which is to reduce think time if replay goes slower than capture. See " Example 191-3 " . capture_sts If this parameter is TRUE , then a SQL tuning set capture is also started in parallel with workload replay. The resulting SQL tuning set can be exported using the EXPORT_AWR Procedure along with the Automatic Workload Repository (AWR) data. Currently, parallel SQL tuning set (STS) capture is not supported in an Oracle RAC environment. So, this parameter has no effect in that context. The calling user must have the appropriate privileges (' ADMINISTER SQL TUNING SET '). The default value is FALSE . sts_cap_interval Specifies the capture interval of the SQL set capture from the cursor cache in seconds. The default value is 300. Usage Notes A consolidated replay replays multiple captures in one replay. Each capture records different system change number (SCN) values. For this reason SCN-based sync is not supported for consolidated replays. Consolidated replays only support non-sync mode and the Object-ID based synchronization, and SCN-based synchronization is currently not supported.