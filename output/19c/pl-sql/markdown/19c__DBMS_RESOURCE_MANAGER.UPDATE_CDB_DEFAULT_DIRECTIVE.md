---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE

This procedure updates the plan directives of the consolidation resource plan.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE (
   plan                        IN    VARCHAR2    DEFAULT NULL, 
   new_comment                 IN    VARCHAR2    DEFAULT NULL, 
   new_shares                  IN    NUMBER      DEFAULT NULL, 
   new_utilization_limit       IN    NUMBER      DEFAULT NULL, 
   new_parallel_server_limit   IN    NUMBER      DEFAULT NULL,
   new_memory_limit            IN    NUMBER      DEFAULT NULL,      
   new_memory_min              IN    NUMBER      DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the consolidation plan |
| new_commnent |  |  | New user comment |
| new_shares | NUMBER | IN | Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The new_shares parameter is also used for Parallel Statement Queuing. |
| new_utilization_limit | NUMBER | IN | Specifies the maximum percentage of CPU that the pluggable database can utilize. |
| new_parallel_server_limit | NUMBER | IN | Specifies the maximum percentage of parallel_servers_target parallel servers that the pluggable database can use. |
| new_memory_limit | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |
| new_memory_min | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE ( plan IN VARCHAR2 DEFAULT NULL, new_comment IN VARCHAR2 DEFAULT NULL, new_shares IN NUMBER DEFAULT NULL, new_utilization_limit IN NUMBER DEFAULT NULL, new_parallel_server_limit IN NUMBER DEFAULT NULL, new_memory_limit IN NUMBER DEFAULT NULL, new_memory_min IN NUMBER DEFAULT NULL); Parameters Table 142-29 UPDATE_CDB_DEFAULT_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan new_commnent New user comment new_shares Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The new_shares parameter is also used for Parallel Statement Queuing. new_utilization_limit Specifies the maximum percentage of CPU that the pluggable database can utilize. new_parallel_server_limit Specifies the maximum percentage of parallel_servers_target parallel servers that the pluggable database can use. new_memory_limit This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. new_memory_min This parameter is only applicable to Oracle Exadata storage for configuring the Database Smart Flash Cache and PMEM Cache. Usage Notes By default, the default values are new_shares : 1 utilization_limit : 100 parallel_server_limit : 100 Note that the default values are NULL . This has the same meaning as in UPDATE_CDB_PLAN_DIRECTIVE Procedure . If the user does not specify a value, the value will not be modified. This procedure can be run only from the CDB root ( CDB$ROOT ). To clear (reset to the directive's default value), use the value -1 .