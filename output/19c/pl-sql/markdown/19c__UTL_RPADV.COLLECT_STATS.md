---
id: 19c__UTL_RPADV.COLLECT_STATS
name: UTL_RPADV.COLLECT_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.COLLECT_STATS

This procedure uses the Oracle Replication Performance Advisor to gather statistics about the Oracle Replication components and subcomponents in a distributed database environment.

## Syntax

```sql
UTL_RPADV.COLLECT_STATS(
   interval                      IN NUMBER  DEFAULT 60,
   num_runs                      IN NUMBER  DEFAULT 10,
   comp_stat_table             IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_COMP_STAT',
   path_stat_table             IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_PATH_STAT',
   top_event_threshold           IN NUMBER  DEFAULT 15,
   bottleneck_idle_threshold     IN NUMBER  DEFAULT 50,
   bottleneck_flowctrl_threshold IN NUMBER  DEFAULT 50);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| interval | NUMBER | IN | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. |
| num_runs | NUMBER | IN | The number of times that the Oracle Replication Performance Advisor is run by the procedure. |
| comp_stat_table | VARCHAR2 | IN | The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. The procedure creates the specified table if it does not exist. Oracle recommends that you use the default table STREAMS$_ADVISOR_COMP_STAT . See " Usage Notes " for more information about this parameter. |
| path_stat_table | VARCHAR2 | IN | The name of the table that stores the statistics collected for stream paths. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. The procedure creates the specified table if it does not exist. Oracle recommends that you use the default table STREAMS$_ADVISOR_PATH_STAT . See " Usage Notes " for more information about this parameter. |
| top_event_threshold | NUMBER | IN | A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. |
| bottleneck_idle_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. |
| bottleneck_flowctrl_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. |

## Usage Notes

Note: This procedure commits. Note: This procedure commits. Syntax UTL_RPADV.COLLECT_STATS( interval IN NUMBER DEFAULT 60, num_runs IN NUMBER DEFAULT 10, comp_stat_table IN VARCHAR2 DEFAULT 'STREAMS$_ADVISOR_COMP_STAT', path_stat_table IN VARCHAR2 DEFAULT 'STREAMS$_ADVISOR_PATH_STAT', top_event_threshold IN NUMBER DEFAULT 15, bottleneck_idle_threshold IN NUMBER DEFAULT 50, bottleneck_flowctrl_threshold IN NUMBER DEFAULT 50); Parameters Table 275-16 COLLECT_STATS Procedure Parameters Parameter Description interval The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. num_runs The number of times that the Oracle Replication Performance Advisor is run by the procedure. comp_stat_table The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. The procedure creates the specified table if it does not exist. Oracle recommends that you use the default table STREAMS$_ADVISOR_COMP_STAT . See " Usage Notes " for more information about this parameter. path_stat_table The name of the table that stores the statistics collected for stream paths. Specify the table name as [schema_name.]object_name . If the schema is not specified, then the current user is the default. The procedure creates the specified table if it does not exist. Oracle recommends that you use the default table STREAMS$_ADVISOR_PATH_STAT . See " Usage Notes " for more information about this parameter. top_event_threshold A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. bottleneck_idle_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. bottleneck_flowctrl_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. Usage Notes The table specified in the path_stat_table parameter stores stream path statistics. This table also concatenates the component and subcomponent statistics stored in the table specified in the comp_stat_table parameter. The SHOW_STATS procedure in this package shows only the statistics stored in the table specified in the path_stat_table parameter.