---
id: 19c__DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE
name: DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE

This procedure will disable the trace at ALL enabled instances for a given combination of Service Name, MODULE , and ACTION name globally.

## Syntax

```sql
DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE(
   service_name    IN  VARCHAR2,
   module_name     IN  VARCHAR2,
   action_name     IN  VARCHAR2 DEFAULT ALL_ACTIONS,
   instance_name   IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| service_name | VARCHAR2 | IN | Name of the service for which tracing is disabled. |
| module_name | VARCHAR2 | IN | Name of the MODULE . An additional qualifier for the service |
| action_name | VARCHAR2 | IN | Name of the ACTION . An additional qualifier for the Service and MODULE name. |
| instance_name | VARCHAR2 | IN | If set, this restricts tracing to the named instance_name |

## Usage Notes

Syntax DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE( service_name IN VARCHAR2, module_name IN VARCHAR2, action_name IN VARCHAR2 DEFAULT ALL_ACTIONS, instance_name IN VARCHAR2 DEFAULT NULL); Parameters Table 112-10 SERV_MOD_ACT_TRACE_DISABLE Procedure Parameters Parameter Description service_name Name of the service for which tracing is disabled. module_name Name of the MODULE . An additional qualifier for the service action_name Name of the ACTION . An additional qualifier for the Service and MODULE name. instance_name If set, this restricts tracing to the named instance_name Usage Notes Specifying NULL for the module_name parameter means that statistics will no longer be accumulated for the sessions which do not set the MODULE attribute. Examples To enable tracing for a Service named APPS1: EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE('APPS1', DBMS_MONITOR.ALL_MODULES, DBMS_MONITOR.ALL_ACTIONS,TRUE, FALSE,NULL); To disable tracing specified in the previous step: EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE('APPS1'); To enable tracing for a given combination of Service and MODULE (all ACTION s): EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_ENABLE('APPS1','PAYROLL', DBMS_MONITOR.ALL_ACTIONS,TRUE,FALSE,NULL); To disable tracing specified in the previous step: EXECUTE DBMS_MONITOR.SERV_MOD_ACT_TRACE_DISABLE('APPS1','PAYROLL');