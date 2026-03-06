---
id: 19c__DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE
name: DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE

This procedure will enable SQL tracing for a given combination of Service Name, MODULE and ACTION globally unless an instance_name is specified.

## Syntax

```sql
DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE(
   service_name    IN VARCHAR2,
   module_name     IN VARCHAR2 DEFAULT ANY_MODULE,
   action_name     IN VARCHAR2 DEFAULT ANY_ACTION,
   waits           IN BOOLEAN DEFAULT TRUE,
   binds           IN BOOLEAN DEFAULT FALSE,
   instance_name   IN VARCHAR2 DEFAULT NULL, 
   plan_stat       IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service for which SQL trace is enabled |
| module_name | VARCHAR2 | IN | Name of the MODULE for which SQL trace is enabled. An optional additional qualifier for the service. If omitted, SQL trace is enabled or all modules and actions in a given service. |
| action_name | VARCHAR2 | IN | Name of the ACTION for which SQL trace is enabled. An optional additional qualifier for the Service and MODULE name. If omitted, SQL trace is enabled for all actions in a given module. |
| waits | BOOLEAN | IN | If TRUE , wait information is present in the trace |
| binds | BOOLEAN | IN | If TRUE , bind information is present in the trace |
| instance_name | VARCHAR2 | IN | If set, this restricts tracing to the named instance_name |
| plan_stat | VARCHAR2 | IN | Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. |

## Usage Notes

Syntax DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE( service_name IN VARCHAR2, module_name IN VARCHAR2 DEFAULT ANY_MODULE, action_name IN VARCHAR2 DEFAULT ANY_ACTION, waits IN BOOLEAN DEFAULT TRUE, binds IN BOOLEAN DEFAULT FALSE, instance_name IN VARCHAR2 DEFAULT NULL, plan_stat IN VARCHAR2 DEFAULT NULL); Parameters Table 112-11 SERV_MOD_ACT_TRACE_ENABLE Procedure Parameters Parameter Description service_name Name of the service for which SQL trace is enabled module_name Name of the MODULE for which SQL trace is enabled. An optional additional qualifier for the service. If omitted, SQL trace is enabled or all modules and actions in a given service. action_name Name of the ACTION for which SQL trace is enabled. An optional additional qualifier for the Service and MODULE name. If omitted, SQL trace is enabled for all actions in a given module. waits If TRUE , wait information is present in the trace binds If TRUE , bind information is present in the trace instance_name If set, this restricts tracing to the named instance_name plan_stat Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. Usage Notes The procedure enables a trace for a given combination of Service, MODULE and ACTION name. The specification is strictly hierarchical: Service Name or Service Name/ MODULE , or Service Name, MODULE, and ACTION name must be specified. Omitting a qualifier behaves like a wild-card, so that not specifying an ACTION means all ACTION s. Using the ALL_ACTIONS constant achieves the same purpose. This tracing is useful when an application MODULE and optionally known ACTION is experiencing poor service levels. By default, tracing is enabled globally for the database. The instance_name parameter is provided to restrict tracing to named instances that are known, for example, to exhibit poor service levels. Tracing information is present in multiple trace files and you must use the trcsess tool to collect it into a single file. Specifying NULL for the module_name parameter means that statistics will be accumulated for the sessions which do not set the MODULE attribute. Examples To enable tracing for a Service named APPS1 : EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE('APPS1', DBMS_MONITOR.ALL_MODULES, DBMS_MONITOR.ALL_ACTIONS,TRUE, FALSE,NULL); To enable tracing for a given combination of Service and MODULE (all ACTION s): EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE('APPS1','PAYROLL', DBMS_MONITOR.ALL_ACTIONS,TRUE,FALSE,NULL);