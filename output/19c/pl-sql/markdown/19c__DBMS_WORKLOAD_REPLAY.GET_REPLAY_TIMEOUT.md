---
id: 19c__DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT
name: DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT

This procedure gets the replay timeout setting.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT (
   enabled       OUT  BOOLEAN, 
   min_delay     OUT  NUMBER,
   max_delay     OUT  NUMBER,
   delay_factor  OUT  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enabled | BOOLEAN | OUT | TRUE if the timeout action is enabled, FALSE otherwise. |
| min_delay | NUMBER | OUT | Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than min_delay . |
| max_delay | NUMBER | OUT | Upper bound of call delay in minutes. The timeout action throws ORA-15569 when the delay is more than max_delay . |
| delay_factor | NUMBER) | OUT | Factor for the call delay that is between min_delay and max_delay . The timeout action throws ORA-15569 when the current replay elapsed time is more than the product of capture elapsed time and delay_factor . |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT ( enabled OUT BOOLEAN, min_delay OUT NUMBER, max_delay OUT NUMBER, delay_factor OUT NUMBER); Parameters Table 191-18 GET_REPLAY_TIMEOUT Procedure Parameters Parameter Description enabled TRUE if the timeout action is enabled, FALSE otherwise. min_delay Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than min_delay . max_delay Upper bound of call delay in minutes. The timeout action throws ORA-15569 when the delay is more than max_delay . delay_factor Factor for the call delay that is between min_delay and max_delay . The timeout action throws ORA-15569 when the current replay elapsed time is more than the product of capture elapsed time and delay_factor . Usage Notes This procedure can be called anytime during replay.