---
id: 19c__DBMS_MONITOR.SERV_MOD_ACT_STAT_DISABLE
name: DBMS_MONITOR.SERV_MOD_ACT_STAT_DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SERV_MOD_ACT_STAT_DISABLE

This procedure will disable statistics accumulation and remove the accumulated results from V$SERV_MOD_ACT_STATS view.

## Syntax

```sql
DBMS_MONITOR.SERV_MOD_ACT_STAT_DISABLE(
   service_name    IN VARCHAR2,
   module_name     IN VARCHAR2,
   action_name     IN VARCHAR2 DEFAULT ALL_ACTIONS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service for which statistic aggregation is disabled |
| module_name | VARCHAR2 | IN | Name of the MODULE . An additional qualifier for the service. It is a required parameter. |
| action_name | VARCHAR2 | IN | Name of the ACTION . An additional qualifier for the Service and MODULE name. Omitting the parameter (or supplying ALL_ACTIONS constant) means enabling aggregation for all Actions for a given Service/MODULE combination. In this case, statistics are aggregated on the module level. |

## Usage Notes

Statistics disabling is persistent for the database. That is, service statistics are disabled for instances of the same database (plus dblinks that have been activated as a result of the enable). Syntax DBMS_MONITOR.SERV_MOD_ACT_STAT_DISABLE( service_name IN VARCHAR2, module_name IN VARCHAR2, action_name IN VARCHAR2 DEFAULT ALL_ACTIONS); Parameters Table 112-8 SERV_MOD_ACT_STAT_DISABLE Procedure Parameters Parameter Description service_name Name of the service for which statistic aggregation is disabled module_name Name of the MODULE . An additional qualifier for the service. It is a required parameter. action_name Name of the ACTION . An additional qualifier for the Service and MODULE name. Omitting the parameter (or supplying ALL_ACTIONS constant) means enabling aggregation for all Actions for a given Service/MODULE combination. In this case, statistics are aggregated on the module level. Usage Notes Regarding statistics gathering, when you change the module or action, the change takes effect when the next user call is executed in the session. For example, if a module is set to 'module 1' in a session, and the module is reset to 'module 2' in a user call in the session, then the module remains 'module 1' during this user call. The module is changed to 'module 2' in the next user call in the session.