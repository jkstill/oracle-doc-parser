---
id: 19c__UTL_RPADV.SHOW_STATS
name: UTL_RPADV.SHOW_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.SHOW_STATS

This procedure generates output that includes the statistics gathered by the COLLECT_STATS and START_MONITORING procedures.

## Syntax

```sql
UTL_RPADV.SHOW_STATS(
   path_stat_table IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_PATH_STAT',
   path_id           IN NUMBER    DEFAULT NULL,
   bgn_run_id        IN NUMBER    DEFAULT -1,
   end_run_id        IN NUMBER    DEFAULT -10,
   show_path_id      IN BOOLEAN   DEFAULT TRUE,
   show_run_id       IN BOOLEAN   DEFAULT TRUE,
   show_run_time     IN BOOLEAN   DEFAULT TRUE,
   show_optimization IN BOOLEAN   DEFAULT TRUE,
   show_setting      IN BOOLEAN   DEFAULT FALSE,
   show_stat         IN BOOLEAN   DEFAULT TRUE,
   show_sess         IN BOOLEAN   DEFAULT FALSE,
   show_legend       IN BOOLEAN   DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path_stat_table | VARCHAR2 | IN | The name of the table that contains the stream path statistics. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. When you gather statistics using the COLLECT_STATS procedure, this table is specified in the path_stat_table parameter in the COLLECT_STATS procedure. The default table is STREAMS$_ADVISOR_PATH_STAT . When you gather statistics using the START_MONITORING procedure, you can determine the name for this table by querying the SHOW_STATS_TABLE column in the STREAMS$_PA_MONITORING view. The default table for a monitoring job is STREAMS$_PA_SHOW_PATH_STAT . |
| path_id | NUMBER | IN | A stream path ID. If non- NULL , then the procedure shows output for the specified stream path only. If NULL , then the procedure shows output for all active stream paths. |
| bgn_run_id | NUMBER | IN | The first Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. |
| end_run_id | NUMBER | IN | The last Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. |
| show_path_id | BOOLEAN | IN | If TRUE , then the path ID for each stream path is included in the output. If FALSE , then the path ID for each stream path is not included in the output. |
| show_run_id | BOOLEAN | IN | If TRUE , then the Oracle Replication Performance Advisor run ID is included in the output. If FALSE , then the Oracle Replication Performance Advisor run ID is not included in the output. |
| show_run_time | BOOLEAN | IN | If TRUE , then the Oracle Replication Performance Advisor run time is included in the output. If FALSE , then the Oracle Replication Performance Advisor run time is not included in the output. |
| show_optimization | BOOLEAN | IN | If TRUE , then path output includes information pertaining to the combined capture and apply optimization. If FALSE , then path output does not include information pertaining to the combined capture and apply optimization. |
| show_setting | BOOLEAN | IN | If TRUE , then the settings for the threshold parameters are included in the output. The threshold parameters are the top_event_threshold , bottleneck_idle_threshold , and bottleneck_flowctrl_threshold parameters in the COLLECT_STATS procedure. If FALSE , then the settings for the threshold parameters are not included in the output. |
| show_stat | BOOLEAN | IN | If TRUE , then the component-level and subcomponent-level statistics are included in the output. These components include capture processes, queues, propagation senders, propagation receivers, and apply processes. The subcomponents are the subcomponents for capture processes and apply processes. If FALSE , then the component-level and subcomponent-level statistics are not included in the output. |
| show_sess | BOOLEAN | IN | If TRUE , then the session-level statistics are included in the output. Session-level statistics include IDLE , FLOW CONTROL , and EVENT statistics. If FALSE , then the session-level statistics are not included in the output. |
| show_legend | BOOLEAN | IN | If TRUE , then the legend is included in the output. The legend describes the abbreviations used in the output. If FALSE , then the legend is not included in the output. |

## Usage Notes

The output is formatted so that it can be imported into a spreadsheet for analysis. Note: This procedure does not commit. See Also: " COLLECT_STATS Procedure " " START_MONITORING Procedure " Note: This procedure does not commit. See Also: " COLLECT_STATS Procedure " " START_MONITORING Procedure " Syntax UTL_RPADV.SHOW_STATS( path_stat_table IN VARCHAR2 DEFAULT 'STREAMS$_ADVISOR_PATH_STAT', path_id IN NUMBER DEFAULT NULL, bgn_run_id IN NUMBER DEFAULT -1, end_run_id IN NUMBER DEFAULT -10, show_path_id IN BOOLEAN DEFAULT TRUE, show_run_id IN BOOLEAN DEFAULT TRUE, show_run_time IN BOOLEAN DEFAULT TRUE, show_optimization IN BOOLEAN DEFAULT TRUE, show_setting IN BOOLEAN DEFAULT FALSE, show_stat IN BOOLEAN DEFAULT TRUE, show_sess IN BOOLEAN DEFAULT FALSE, show_legend IN BOOLEAN DEFAULT TRUE); Parameters Table 275-18 SHOW_STATS Procedure Parameters Parameter Description path_stat_table The name of the table that contains the stream path statistics. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. When you gather statistics using the COLLECT_STATS procedure, this table is specified in the path_stat_table parameter in the COLLECT_STATS procedure. The default table is STREAMS$_ADVISOR_PATH_STAT . When you gather statistics using the START_MONITORING procedure, you can determine the name for this table by querying the SHOW_STATS_TABLE column in the STREAMS$_PA_MONITORING view. The default table for a monitoring job is STREAMS$_PA_SHOW_PATH_STAT . path_id A stream path ID. If non- NULL , then the procedure shows output for the specified stream path only. If NULL , then the procedure shows output for all active stream paths. bgn_run_id The first Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. end_run_id The last Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. show_path_id If TRUE , then the path ID for each stream path is included in the output. If FALSE , then the path ID for each stream path is not included in the output. show_run_id If TRUE , then the Oracle Replication Performance Advisor run ID is included in the output. If FALSE , then the Oracle Replication Performance Advisor run ID is not included in the output. show_run_time If TRUE , then the Oracle Replication Performance Advisor run time is included in the output. If FALSE , then the Oracle Replication Performance Advisor run time is not included in the output. show_optimization If TRUE , then path output includes information pertaining to the combined capture and apply optimization. If FALSE , then path output does not include information pertaining to the combined capture and apply optimization. show_setting If TRUE , then the settings for the threshold parameters are included in the output. The threshold parameters are the top_event_threshold , bottleneck_idle_threshold , and bottleneck_flowctrl_threshold parameters in the COLLECT_STATS procedure. If FALSE , then the settings for the threshold parameters are not included in the output. show_stat If TRUE , then the component-level and subcomponent-level statistics are included in the output. These components include capture processes, queues, propagation senders, propagation receivers, and apply processes. The subcomponents are the subcomponents for capture processes and apply processes. If FALSE , then the component-level and subcomponent-level statistics are not included in the output. show_sess If TRUE , then the session-level statistics are included in the output. Session-level statistics include IDLE , FLOW CONTROL , and EVENT statistics. If FALSE , then the session-level statistics are not included in the output. show_legend If TRUE , then the legend is included in the output. The legend describes the abbreviations used in the output. If FALSE , then the legend is not included in the output.