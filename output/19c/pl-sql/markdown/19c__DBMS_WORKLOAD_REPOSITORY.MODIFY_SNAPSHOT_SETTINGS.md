---
id: 19c__DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS
name: DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS

This procedure controls three aspects of snapshot generation.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(
   retention          IN  NUMBER    DEFAULT  NULL,
   interval           IN  NUMBER    DEFAULT  NULL,
   topnsql            IN  NUMBER    DEFAULT  NULL,
   dbid               IN  NUMBER    DEFAULT  NULL,
   tablespace_name    IN  VARCHAR2  DEFAULT  NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| retention | NUMBER | IN | New retention time (in minutes). The specified value must be in the range of MIN_RETENTION (1 day) to MAX_RETENTION (100 years). If ZERO is specified, snapshots will be retained forever. A large system-defined value will be used as the retention setting. If NULL is specified, the old value for retention is preserved. NOTE: The retention setting must be greater than or equal to the window size of the ' SYSTEM_MOVING_WINDOW ' baseline. If the retention needs to be less than the window size, the MODIFY_BASELINE_WINDOW_SIZE Procedure can be used to adjust the window size. |
| interval | NUMBER | IN | New interval setting between each snapshot, in units of minutes. The specified value must be in the range MIN_INTERVAL (10 minutes) to MAX_INTERVAL (1 year). If ZERO is specified, automatic and manual snapshots will be disabled. A large system-defined value will be used as the retention setting. If NULL is specified, the current value is preserved. |
| topnsql | NUMBER | IN | If NUMBER : Top N SQL size. The number of Top SQL to flush for each SQL criteria (Elapsed Time, CPU Time, Parse Calls, Shareable Memory, Version Count). The value for this setting will not be affected by the statistics/flush level and will override the system default behavior for the AWR SQL collection. The setting will have a minimum value of 30 and a maximum value of 50,000. Specifying NULL will keep the current setting. If VARCHAR2 : Users are allowed to specify the following values: ( DEFAULT , MAXIMUM , N ), where N is the number of Top SQL to flush for each SQL criteria. Specifying DEFAULT will revert the system back to the default behavior of Top 30 for statistics level TYPICAL and Top 100 for statistics level ALL . Specifying MAXIMUM will cause the system to capture the complete set of SQL in the cursor cache. Specifying the number N is equivalent to setting the Top N SQL with the NUMBER type. Specifying NULL for this argument will keep the current setting. |
| dbid | NUMBER | IN | Database identifier in AWR for which to modify the snapshot settings. If NULL is specified, the local dbid will be used. Defaults to NULL . |
| tablespace_name | VARCHAR2 | IN | Specify a user-defined tablespace for storing AWR data (snapshot data). If this parameter is not used, then AWR data is stored in the SYSAUX tablespace by default. |

## Usage Notes

The INTERVAL setting affects how often snapshots are automatically captured. The RETENTION setting affects how long snapshots are retained in the Workload Repository. The number of SQL captured for each Top criteria. If the user manually specifies a value for Top N SQL, the AWR SQL collection will use the user-specified number for both automatic and manual snapshots. There are two overloads. The first takes a NUMBER and the second takes a VARCHAR2 for the topnsql argument. The differences are described under the Parameters description. Syntax DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS( retention IN NUMBER DEFAULT NULL, interval IN NUMBER DEFAULT NULL, topnsql IN NUMBER DEFAULT NULL, dbid IN NUMBER DEFAULT NULL, tablespace_name IN VARCHAR2 DEFAULT NULL); Parameters Table 192-35 MODIFY_SNAPSHOT_SETTINGS Procedure Parameters Parameter Description retention New retention time (in minutes). The specified value must be in the range of MIN_RETENTION (1 day) to MAX_RETENTION (100 years). If ZERO is specified, snapshots will be retained forever. A large system-defined value will be used as the retention setting. If NULL is specified, the old value for retention is preserved. NOTE: The retention setting must be greater than or equal to the window size of the ' SYSTEM_MOVING_WINDOW ' baseline. If the retention needs to be less than the window size, the MODIFY_BASELINE_WINDOW_SIZE Procedure can be used to adjust the window size. interval New interval setting between each snapshot, in units of minutes. The specified value must be in the range MIN_INTERVAL (10 minutes) to MAX_INTERVAL (1 year). If ZERO is specified, automatic and manual snapshots will be disabled. A large system-defined value will be used as the retention setting. If NULL is specified, the current value is preserved. topnsql If NUMBER : Top N SQL size. The number of Top SQL to flush for each SQL criteria (Elapsed Time, CPU Time, Parse Calls, Shareable Memory, Version Count). The value for this setting will not be affected by the statistics/flush level and will override the system default behavior for the AWR SQL collection. The setting will have a minimum value of 30 and a maximum value of 50,000. Specifying NULL will keep the current setting. If VARCHAR2 : Users are allowed to specify the following values: ( DEFAULT , MAXIMUM , N ), where N is the number of Top SQL to flush for each SQL criteria. Specifying DEFAULT will revert the system back to the default behavior of Top 30 for statistics level TYPICAL and Top 100 for statistics level ALL . Specifying MAXIMUM will cause the system to capture the complete set of SQL in the cursor cache. Specifying the number N is equivalent to setting the Top N SQL with the NUMBER type. Specifying NULL for this argument will keep the current setting. dbid Database identifier in AWR for which to modify the snapshot settings. If NULL is specified, the local dbid will be used. Defaults to NULL . tablespace_name Specify a user-defined tablespace for storing AWR data (snapshot data). If this parameter is not used, then AWR data is stored in the SYSAUX tablespace by default. Examples This example changes the interval setting to one hour and the retention setting to two weeks for the local database: EXECUTE DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS( interval => 60, retention => 20160); If you query the DBA_HIST_WR_CONTROL table after this procedure is executed, you will see the changes to these settings.