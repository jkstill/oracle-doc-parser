---
id: 19c__DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE
name: DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE

This procedure enables statistic gathering for a given combination of Service Name, MODULE and ACTION .

## Syntax

```sql
DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(
   service_name    IN VARCHAR2,
   module_name     IN VARCHAR2,
   action_name     IN VARCHAR2 DEFAULT ALL_ACTIONS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service for which statistic aggregation is enabled |
| module_name | VARCHAR2 | IN | Name of the MODULE . An additional qualifier for the service. It is a required parameter. |
| action_name | VARCHAR2 | IN | Name of the ACTION . An additional qualifier for the Service and MODULE name. Omitting the parameter (or supplying ALL_ACTIONS constant) means enabling aggregation for all Actions for a given Service/MODULE combination. In this case, statistics are aggregated on the module level. |

## Usage Notes

Calling this procedure enables statistic gathering for a hierarchical combination of Service name, MODULE name, and ACTION name on all instances for the same database. Statistics are accessible by means of the V$SERV_MOD_ACT_STATS view. Syntax DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE( service_name IN VARCHAR2, module_name IN VARCHAR2, action_name IN VARCHAR2 DEFAULT ALL_ACTIONS); Parameters Table 112-9 SERV_MOD_ACT_STAT_ENABLE Procedure Parameters Parameter Description service_name Name of the service for which statistic aggregation is enabled module_name Name of the MODULE . An additional qualifier for the service. It is a required parameter. action_name Name of the ACTION . An additional qualifier for the Service and MODULE name. Omitting the parameter (or supplying ALL_ACTIONS constant) means enabling aggregation for all Actions for a given Service/MODULE combination. In this case, statistics are aggregated on the module level. Usage Notes Enabling statistic aggregation for the given combination of Service/Module/Action names is slightly complicated by the fact that the Module/Action values can be empty strings which are indistinguishable from NULLs. For this reason, we adopt the following conventions: A special constant (unlikely to be a real action names) is defined: ALL_ACTIONS constant VARCHAR2 := '###ALL_ACTIONS'; Using ALL_ACTIONS for an action specification means that aggregation is enabled for all actions with a given module name, while using NULL (or empty string) means that aggregation is enabled for an action whose name is an empty string. Regarding statistics gathering, when you change the module or action, the change takes effect when the next user call is executed in the session. For example, if a module is set to 'module 1' in a session, and the module is reset to 'module 2' in a user call in the session, then the module remains 'module 1' during this user call. The module is changed to 'module 2' in the next user call in the session. Examples To enable statistic accumulation for a given combination of Service name and MODULE : EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE( 'APPS1','PAYROLL'); To enable statistic accumulation for a given combination of Service name, MODULE and ACTION : EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE('APPS1','GLEDGER','DEBIT_ENTRY'); If both of the preceding commands are issued, statistics are accumulated as follows: For the APPS1 service, because accumulation for each Service Name is the default. For all actions in the PAYROLL Module. For the DEBIT_ENTRY Action within the GLEDGER Module.