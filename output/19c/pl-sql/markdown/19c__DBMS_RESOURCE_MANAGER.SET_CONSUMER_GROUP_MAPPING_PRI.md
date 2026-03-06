---
id: 19c__DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI
name: DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI

Multiple attributes of a session can be used to map the session to a consumer group. This procedure prioritizes the attribute mappings.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI(
   explicit               IN NUMBER, 
   oracle_user            IN NUMBER, 
   service_name           IN NUMBER, 
   client_os_user         IN NUMBER, 
   client_program         IN NUMBER, 
   client_machine         IN NUMBER, 
   module_name            IN NUMBER, 
   module_name_action     IN NUMBER,
   service_module         IN NUMBER,
   service_module_action  IN NUMBER,
   client_id              IN NUMBER DEFAULT 11);
```

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI( explicit IN NUMBER, oracle_user IN NUMBER, service_name IN NUMBER, client_os_user IN NUMBER, client_program IN NUMBER, client_machine IN NUMBER, module_name IN NUMBER, module_name_action IN NUMBER, service_module IN NUMBER, service_module_action IN NUMBER, client_id IN NUMBER DEFAULT 11); Parameters Table 142-22 SET_CONSUMER_GROUP_MAPPING_PRI Procedure Parameters Parameters Description explicit Priority of the explicit mapping oracle_user Priority of the Oracle user name mapping service_name Priority of the client service name mapping client_os_user Priority of the client operating system user name mapping client_program Priority of the client program mapping client_machine Priority of the client machine mapping module_name Priority of the application module name mapping module_name_action Priority of the application module name and action mapping service_module Priority of the service name and application module name mapping module_name_action Priority of the service name, application module name, and application action mapping client_id Client identifier Usage Notes This procedure requires that you include the pseudo-attribute explicit as an argument. It must be set to 1. It indicates that explicit consumer group switches have the highest priority. You explicitly switch consumer groups with these package procedures: DBMS_SESSION . SWITCH_CURRENT_CONSUMER_GROUP DBMS_RESOURCE_MANAGER . SWITCH_CONSUMER_GROUP_FOR_SESS DBMS_RESOURCE_MANAGER . SWITCH_CONSUMER_GROUP_FOR_USER Each priority value must be a unique integer from 1 to 11. Together, they establish an ordering where 1 is the highest priority and 11 is the lowest.