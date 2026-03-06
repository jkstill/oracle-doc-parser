---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE

This procedure updates the plan directives with regard to automated maintenance tasks in the CDB root ( CDB$ROOT ).

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE (
   plan                        IN    VARCHAR2, 
   new_comment                 IN    VARCHAR2       DEFAULT NULL, 
   new_shares                  IN    NUMBER         DEFAULT NULL, 
   new_utilization_limit       IN    NUMBER         DEFAULT NULL, 
   new_parallel_server_limit   IN    NUMBER         DEFAULT NULL,
   new_memory_limit            IN    NUMBER         DEFAULT NULL,   
   new_memory_min              IN    NUMBER         DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the consolidation plan |
| new_comment | VARCHAR2 | IN | New user comment |
| new_shares | NUMBER | IN | Specifies the new share of resource allocation for CDB root’s automated maintenance tasks |
| new_utilization_limit | NUMBER | IN | Specifies the new maximum percentage of CPU that automated maintenance tasks in the CDB root can utilize |
| new_parallel_server_limit | NUMBER | IN | Specifies the new maximum percentage of parallel_servers_target parallel servers that automated maintenance tasks in the CDB root are allowed to use |
| new_memory_limit | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| new_memory_min | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

## Usage Notes

By default, all maintenance tasks occur directly in the PDBs themselves. Syntax DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE ( plan IN VARCHAR2, new_comment IN VARCHAR2 DEFAULT NULL, new_shares IN NUMBER DEFAULT NULL, new_utilization_limit IN NUMBER DEFAULT NULL, new_parallel_server_limit IN NUMBER DEFAULT NULL, new_memory_limit IN NUMBER DEFAULT NULL, new_memory_min IN NUMBER DEFAULT NULL); Parameters Table 142-28 UPDATE_CDB_AUTOTASK_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan new_comment New user comment new_shares Specifies the new share of resource allocation for CDB root’s automated maintenance tasks new_utilization_limit Specifies the new maximum percentage of CPU that automated maintenance tasks in the CDB root can utilize new_parallel_server_limit Specifies the new maximum percentage of parallel_servers_target parallel servers that automated maintenance tasks in the CDB root are allowed to use new_memory_limit This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. new_memory_min This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. Usage Notes By default for automated maintenance tasks, the values are shares : -1 utilization_limit : 90 parallel_server_limit : 100 The shares = -1 means that the automated maintenance tasks get an allocation of 20% of the system. If the user specifies the shares , it behaves the same properties as the other CDB plan directive functions. If the user does not change the shares or later changes it back to -1 , autotask will get 20% of the system. This procedure can be run only from the CDB root. To clear (reset to the directive's default value), use the value -1 .