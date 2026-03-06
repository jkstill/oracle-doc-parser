---
id: 19c__UTL_RPADV.ALTER_MONITORING
name: UTL_RPADV.ALTER_MONITORING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.ALTER_MONITORING

This procedure alters the monitoring job submitted by the current user.

## Syntax

```sql
UTL_RPADV.ALTER_MONITORING(
   interval                      IN NUMBER  DEFAULT NULL,
   top_event_threshold           IN NUMBER  DEFAULT NULL,
   bottleneck_idle_threshold     IN NUMBER  DEFAULT NULL,
   bottleneck_flowctrl_threshold IN NUMBER  DEFAULT NULL,
   retention_time                IN NUMBER  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| interval | NUMBER | IN | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. If NULL , then the current value is not changed. |
| top_event_threshold | NUMBER | IN | A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. If NULL , then the current value is not changed. |
| bottleneck_idle_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. If NULL , then the current value is not changed. |
| bottleneck_flowctrl_threshold | NUMBER | IN | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. If NULL , then the current value is not changed. |
| retention_time | NUMBER | IN | The number of hours to retain monitoring results. If NULL , then the current value is not changed. |

## Usage Notes

Syntax UTL_RPADV.ALTER_MONITORING( interval IN NUMBER DEFAULT NULL, top_event_threshold IN NUMBER DEFAULT NULL, bottleneck_idle_threshold IN NUMBER DEFAULT NULL, bottleneck_flowctrl_threshold IN NUMBER DEFAULT NULL, retention_time IN NUMBER DEFAULT NULL); Parameters Table 275-14 ALTER_MONITORING Procedure Parameters Parameter Description interval The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. If NULL , then the current value is not changed. top_event_threshold A percentage that determines whether a top wait event statistic is collected. The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if 15 is specified, then only wait events with a value larger than 15% are collected. If NULL , then the current value is not changed. bottleneck_idle_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its IDLE percentage. The IDLE percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. If NULL , then the current value is not changed. bottleneck_flowctrl_threshold A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its FLOW CONTROL percentage. The FLOW CONTROL percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if 50 is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. If NULL , then the current value is not changed. retention_time The number of hours to retain monitoring results. If NULL , then the current value is not changed. Exceptions Table 275-15 ALTER_MONITORING Procedure Exceptions Exception Description ORA-20113 no active monitoring job found