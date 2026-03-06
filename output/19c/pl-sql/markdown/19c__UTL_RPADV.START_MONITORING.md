---
id: 19c__UTL_RPADV.START_MONITORING
name: UTL_RPADV.START_MONITORING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.START_MONITORING

This procedure starts a monitoring job.

## Syntax

```sql
UTL_RPADV.START_MONITORING(
   job_name                      IN VARCHAR2  DEFAULT 'STREAMS$_MONITORING_JOB',
   client_name                   IN VARCHAR2  DEFAULT NULL,
   query_user_name               IN VARCHAR2  DEFAULT NULL,
   interval                      IN NUMBER    DEFAULT 60,
   top_event_threshold           IN NUMBER    DEFAULT 15,
   bottleneck_idle_threshold     IN NUMBER    DEFAULT 50,
   bottleneck_flowctrl_threshold IN NUMBER    DEFAULT 50,
   retention_time                IN NUMBER    DEFAULT 24);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the monitoring job to create. |
| client_name | VARCHAR2 | IN | The name of the client. |
| query_user_name | VARCHAR2 | IN | The user who will query the result tables. This procedure grants privileges to the specified user to enable the user to query the result tables. |
| interval | NUMBER | IN | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. The specified interval is used for the interval parameter in the COLLECT_STATS procedure. |
| top_event_threshold | NUMBER | IN | A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. |
| bottleneck_idle_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. |
| bottleneck_flowctrl_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. |
| retention_time | NUMBER | IN | The number of hours to retain monitoring results. |

## Usage Notes

This procedure runs the COLLECT_STATS procedure to gather statistics about the Oracle Replication components and subcomponents in a distributed database environment. Note: This procedure commits. See Also: " COLLECT_STATS Procedure " Note: This procedure commits. See Also: " COLLECT_STATS Procedure " Syntax UTL_RPADV.START_MONITORING( job_name IN VARCHAR2 DEFAULT 'STREAMS$_MONITORING_JOB', client_name IN VARCHAR2 DEFAULT NULL, query_user_name IN VARCHAR2 DEFAULT NULL, interval IN NUMBER DEFAULT 60, top_event_threshold IN NUMBER DEFAULT 15, bottleneck_idle_threshold IN NUMBER DEFAULT 50, bottleneck_flowctrl_threshold IN NUMBER DEFAULT 50, retention_time IN NUMBER DEFAULT 24); Parameters Table 275-20 START_MONITORING Procedure Parameters Parameter Description job_name The name of the monitoring job to create. client_name The name of the client. query_user_name The user who will query the result tables. This procedure grants privileges to the specified user to enable the user to query the result tables. interval The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. The specified interval is used for the interval parameter in the COLLECT_STATS procedure. top_event_threshold A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. bottleneck_idle_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. bottleneck_flowctrl_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. retention_time The number of hours to retain monitoring results.