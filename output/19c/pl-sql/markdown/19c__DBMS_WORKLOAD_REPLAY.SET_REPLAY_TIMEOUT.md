---
id: 19c__DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT
name: DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT

This procedure sets the replay timeout setting. The purpose is to abort user calls that might make the replay much slower or even cause a replay hang.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT (
   enabled       OUT  BOOLEAN DEFAULT TRUE, 
   min_delay     OUT  NUMBER DEFAULT 10,
   max_delay     OUT  NUMBER DEFAULT 120,
   delay_factor  OUT  NUMBER DEFAULT 8);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enabled | BOOLEAN | OUT | TRUE to enable the timeout action, and FALSE to disable. |
| min_delay | NUMBER | OUT | Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than min_delay . Default = 10. |
| max_delay | NUMBER | OUT | Upper bound of call delay in minutes. The timeout action throws ORA-15569 when the delay is more than max_delay . Default = 120. |
| delay_factor | NUMBER | OUT | Factor for the call delay that is between min_delay and max_delay . The timeout action throws ORA-15569 when the current replay elapsed time is more than the product of capture elapsed time and delay_factor . Default = 8. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT ( enabled OUT BOOLEAN DEFAULT TRUE, min_delay OUT NUMBER DEFAULT 10, max_delay OUT NUMBER DEFAULT 120, delay_factor OUT NUMBER DEFAULT 8); Parameters Table 191-34 SET_REPLAY_TIMEOUT Procedure Parameters Parameter Description enabled TRUE to enable the timeout action, and FALSE to disable. min_delay Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than min_delay . Default = 10. max_delay Upper bound of call delay in minutes. The timeout action throws ORA-15569 when the delay is more than max_delay . Default = 120. delay_factor Factor for the call delay that is between min_delay and max_delay . The timeout action throws ORA-15569 when the current replay elapsed time is more than the product of capture elapsed time and delay_factor . Default = 8. Usage Notes This procedure can be called anytime during replay. Call delay is defined as the difference between replay and capture if replay elapsed time is longer than call elapsed time. Once a replay timeout action is enabled, a user call will exit with ORA-15569 if it has been delayed more than the condition specified by the replay action. The call and its error are reported as error divergence. Replay timeout operates as follows: The timeout action has no effect if it is not enabled. If the call delay in minutes is less than a lower bound specified by parameter min_delay , then the timeout action is non-operational. If the delay in minutes is more than a upper bound specified by parameter max_delay , the timeout action will abort the user call and throw ORA-15569 . For delay that is between the lower bound and upper bound, the user call will abort with ORA-15569 only when the current replay elapsed time is more than the product of capture elapsed time and parameter delay_factor .