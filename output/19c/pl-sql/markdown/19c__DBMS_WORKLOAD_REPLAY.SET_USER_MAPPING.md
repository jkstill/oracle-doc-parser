---
id: 19c__DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING
name: DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING

This procedure sets a new schema or user name to be used during replay instead of the captured user.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING (
   schedule_cap_id      IN NUMBER,
   capture_user         IN VARCHAR2,
   replay_user          IN VARCHAR2);

DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING (
   capture_user         IN VARCHAR2,
   replay_user          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_cap_id | NUMBER | IN | ID of the a capture in the schedule |
| capture_user | VARCHAR2 | IN | User name during the time of the workload capture |
| replay_user | VARCHAR2) | IN | User name to which captured user is remapped during replay. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING ( schedule_cap_id IN NUMBER, capture_user IN VARCHAR2, replay_user IN VARCHAR2); DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING ( capture_user IN VARCHAR2, replay_user IN VARCHAR2); Parameters Table 191-36 SET_USER_MAPPING Procedure Parameters Parameter Description schedule_cap_id ID of the a capture in the schedule capture_user User name during the time of the workload capture replay_user User name to which captured user is remapped during replay. Usage Notes A schedule_cap_id of NULL is used for regular non-consolidate replay. The replay must be initialized but not prepared in order to use this subprogram. If replay_user is set to NULL , then the mapping is disabled. After multiple calls with the same capture_user , the last call always takes effect. To list all the mappings that will be in effect during the subsequent replay execute the following: SELECT * FROM DBA_WORKLOAD_ACTIVE_USER_MAP The overloaded version without the schedule_cap_id calls the one with the schedule_cap_id argument by passing in NULL . Mappings are stored in a table made public through the view DBA_WORKLOAD_USER_MAP . To remove old mappings execute DELETE * FROM DBA_WORKLOAD_USER_MAP