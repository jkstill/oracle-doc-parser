---
id: 19c__UTL_RPADV.SHOW_STATS_HTML
name: UTL_RPADV.SHOW_STATS_HTML
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.SHOW_STATS_HTML

This procedure generates HTML output that includes the statistics gathered by the COLLECT_STATS and START_MONITORING procedures.

## Syntax

```sql
UTL_RPADV.SHOW_STATS_HTML(
   directory       IN VARCHAR2,
   reportname      IN VARCHAR2  DEFAULT 'RPADVREPORT.HTML',
   comp_stat_table IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_COMP_STAT',
   path_id         IN NUMBER    DEFAULT NULL,
   bgn_run_id      IN NUMBER    DEFAULT -1,
   end_run_id      IN NUMBER    DEFAULT -10,
   detailed        IN BOOLEAN   DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directory | VARCHAR2 | IN | The directory object for the directory on the local computer system into which the generated HTML report is placed The specified directory object must be created using the SQL statement CREATE DIRECTORY , and the user who invokes the procedure must have READ and WRITE privilege on each one. |
| reportname | VARCHAR2 | IN | The name of the HTML report |
| comp_stat_table | VARCHAR2 | IN | The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. When you gather statistics using the COLLECT_STATS procedure, this table is specified in the comp_stat_table parameter in the COLLECT_STATS procedure. The default table is STREAMS$_ADVISOR_COMP_STAT . When you gather statistics using the START_MONITORING procedure, you can determine the name for this table by querying the SHOW_STATS_TABLE column in the STREAMS$_PA_MONITORING view. The default table for a monitoring job is STREAMS$_PA_SHOW_PATH_STAT . Oracle recommends that you start a monitoring job with the START_MONITORING procedure in this package and use the appropriate the STREAMS$_PA_SHOW_PATH_STAT table. |
| path_id | NUMBER | IN | A stream path ID. If non- NULL , then the procedure shows output for the specified stream path only. If NULL , then the procedure shows output for all active stream paths. |
| bgn_run_id | NUMBER | IN | The first Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. |
| end_run_id | NUMBER | IN | The last Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. |
| detailed | BOOLEAN | IN | If TRUE , then the procedure generates component-level statistics. If FALSE , then the procedure does not generate component-level statistics. |

## Usage Notes

Note: This procedure does not commit. See Also: " COLLECT_STATS Procedure " " START_MONITORING Procedure " Note: This procedure does not commit. See Also: " COLLECT_STATS Procedure " " START_MONITORING Procedure " Syntax UTL_RPADV.SHOW_STATS_HTML( directory IN VARCHAR2, reportname IN VARCHAR2 DEFAULT 'RPADVREPORT.HTML', comp_stat_table IN VARCHAR2 DEFAULT 'STREAMS$_ADVISOR_COMP_STAT', path_id IN NUMBER DEFAULT NULL, bgn_run_id IN NUMBER DEFAULT -1, end_run_id IN NUMBER DEFAULT -10, detailed IN BOOLEAN DEFAULT TRUE); Parameters Table 275-19 SHOW_STATS_HTML Procedure Parameters Parameter Description directory The directory object for the directory on the local computer system into which the generated HTML report is placed The specified directory object must be created using the SQL statement CREATE DIRECTORY , and the user who invokes the procedure must have READ and WRITE privilege on each one. reportname The name of the HTML report comp_stat_table The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. When you gather statistics using the COLLECT_STATS procedure, this table is specified in the comp_stat_table parameter in the COLLECT_STATS procedure. The default table is STREAMS$_ADVISOR_COMP_STAT . When you gather statistics using the START_MONITORING procedure, you can determine the name for this table by querying the SHOW_STATS_TABLE column in the STREAMS$_PA_MONITORING view. The default table for a monitoring job is STREAMS$_PA_SHOW_PATH_STAT . Oracle recommends that you start a monitoring job with the START_MONITORING procedure in this package and use the appropriate the STREAMS$_PA_SHOW_PATH_STAT table. path_id A stream path ID. If non- NULL , then the procedure shows output for the specified stream path only. If NULL , then the procedure shows output for all active stream paths. bgn_run_id The first Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. end_run_id The last Oracle Replication Performance Advisor run ID to show in the range of runs. See " Usage Notes " for more information about this parameter. detailed If TRUE , then the procedure generates component-level statistics. If FALSE , then the procedure does not generate component-level statistics.