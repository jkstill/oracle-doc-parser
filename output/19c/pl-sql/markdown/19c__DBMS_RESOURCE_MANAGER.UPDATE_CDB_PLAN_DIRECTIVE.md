---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE

Updates the plan directives for a consolidation resource plan. Plan directives specify the resource allocation policy for pluggable databases (PDBs).

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE (
   plan                        IN    VARCHAR2 (30), 
   pluggable_database          IN    VARCHAR2 (30)
   new_comment                 IN    VARCHAR2 (200)  DEFAULT NULL, 
   new_shares                  IN    NUMBER          DEFAULT NULL, 
   new_utilization_limit       IN    NUMBER          DEFAULT NULL, 
   new_parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   new_memory_limit            IN    NUMBER          DEFAULT NULL,  
   new_memory_min              IN    NUMBER          DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the consolidation plan |
| pluggable_database | VARCHAR2 | IN | Name of the pluggable database |
| new_comment | VARCHAR2 | IN | New user comment |
| new_shares | NUMBER | IN | The share of resource allocation for the pluggable database CPU Resource Manager is enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through the UPDATE_CDB_DEFAULT_DIRECTIVE Procedure . |
| new_utilization_limit | NUMBER | IN | The new maximum percentage of CPU that the pluggable database can utilize |
| new_parallel_server_limit | NUMBER | IN | The new maximum percentage of parallel_servers_target parallel servers that the pluggable database can use |
| new_memory_limit | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| new_memory_ min |  |  | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE ( plan IN VARCHAR2 (30), pluggable_database IN VARCHAR2 (30) new_comment IN VARCHAR2 (200) DEFAULT NULL, new_shares IN NUMBER DEFAULT NULL, new_utilization_limit IN NUMBER DEFAULT NULL, new_parallel_server_limit IN NUMBER DEFAULT NULL, new_memory_limit IN NUMBER DEFAULT NULL, new_memory_min IN NUMBER DEFAULT NULL); Parameters Table 142-31 UPDATE_CDB_PLAN_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan pluggable_database Name of the pluggable database new_comment New user comment new_shares The share of resource allocation for the pluggable database CPU Resource Manager is enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through the UPDATE_CDB_DEFAULT_DIRECTIVE Procedure . new_utilization_limit The new maximum percentage of CPU that the pluggable database can utilize new_parallel_server_limit The new maximum percentage of parallel_servers_target parallel servers that the pluggable database can use new_memory_limit This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. new_memory_ min This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. Usage Notes The default value for the new_* parameters is NULL which indicates that the existing value is left unchanged. If the user does not specify one of the arguments when calling this function, the value is not modified. This procedure can be run only from the CDB root ( CDB$ROOT ). To clear (reset to the directive's default value), use the value -1 .