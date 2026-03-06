---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE

This procedure creates the plan directives of the consolidation resource plan. Plan directives specify the resource allocation policy for pluggable databases (PDBs).

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE (
   plan                    IN    VARCHAR2, 
   pluggable_database      IN    VARCHAR2, 
   comment                 IN    VARCHAR2 (2000) DEFAULT '', 
   shares                  IN    NUMBER          DEFAULT NULL, 
   utilization_limit       IN    NUMBER          DEFAULT NULL, 
   parallel_server_limit   IN    NUMBER          DEFAULT NULL,
   memory_limit            IN    NUMBER          DEFAULT 100, 
   memory_min              IN    NUMBER          DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the consolidation plan |
| pluggable_database | VARCHAR2 | IN | Name of the PDB |
| comment | VARCHAR2 | IN | User comment |
| shares | NUMBER | IN | Specifies the share of resource allocation for the PDB. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through UPDATE_CDB_DEFAULT_DIRECTIVE Procedure . |
| utilization_limit | NUMBER | IN | Specifies the maximum percentage of the CDB's CPU and Exadata I/O resources that the PDB can utilize. CPU Resource Manager and Exadata I/O Resource Manager can also be limited by setting the CPU_COUNT parameter for the PDB. |
| parallel_server_limit | NUMBER | IN | Parallel servers that the PDB can use after which parallel statements are queued. Alternatively, you can set the parallel_servers_target at the PDB level. A PDB can set a lower limit for parallel execution servers than the limit specified in the CDB resource plan. When the PARALLEL_SERVERS_TARGET initialization parameter is set in a PDB, and parallel execution server limit is specified for a PDB in the CDB resource plan, then the lower limit is used. For example, assume that the parallel_servers_target initialization parameter is set to 100 in the CDB root and parallel_server_limit is set to 70 for hrpdb in the CDB resource plan. Also, assume that hrpdb has its parallel_servers_target initialization parameter set to 50. In this case, the limit for parallel execution servers for hrpdb is 50, because 50 is lower than the CDB resource plan limit of 70 for hrpdb . Note: Oracle recommends, that you use parallel_servers_target parameter instead of parallel_servers_limit in a CDB resource plan. |
| memory_limit | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |
| memory_min | NUMBER | IN | This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE ( plan IN VARCHAR2, pluggable_database IN VARCHAR2, comment IN VARCHAR2 (2000) DEFAULT '', shares IN NUMBER DEFAULT NULL, utilization_limit IN NUMBER DEFAULT NULL, parallel_server_limit IN NUMBER DEFAULT NULL, memory_limit IN NUMBER DEFAULT 100, memory_min IN NUMBER DEFAULT 0); Parameters Table 142-6 CREATE_CDB_PLAN_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan pluggable_database Name of the PDB comment User comment shares Specifies the share of resource allocation for the PDB. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If no share is specified, the default is obtained from the default directive, specified through UPDATE_CDB_DEFAULT_DIRECTIVE Procedure . utilization_limit Specifies the maximum percentage of the CDB's CPU and Exadata I/O resources that the PDB can utilize. CPU Resource Manager and Exadata I/O Resource Manager can also be limited by setting the CPU_COUNT parameter for the PDB. parallel_server_limit Parallel servers that the PDB can use after which parallel statements are queued. Alternatively, you can set the parallel_servers_target at the PDB level. A PDB can set a lower limit for parallel execution servers than the limit specified in the CDB resource plan. When the PARALLEL_SERVERS_TARGET initialization parameter is set in a PDB, and parallel execution server limit is specified for a PDB in the CDB resource plan, then the lower limit is used. For example, assume that the parallel_servers_target initialization parameter is set to 100 in the CDB root and parallel_server_limit is set to 70 for hrpdb in the CDB resource plan. Also, assume that hrpdb has its parallel_servers_target initialization parameter set to 50. In this case, the limit for parallel execution servers for hrpdb is 50, because 50 is lower than the CDB resource plan limit of 70 for hrpdb . Note: Oracle recommends, that you use parallel_servers_target parameter instead of parallel_servers_limit in a CDB resource plan. memory_limit This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. memory_min This parameter is only applicable to Oracle Exadata storage for configuring the Exadata Smart Flash Cache and Exadata PMEM Cache. Note: Oracle recommends, that you use parallel_servers_target parameter instead of parallel_servers_limit in a CDB resource plan. Usage Notes The default value for shares , utilization_limit , and parallel_server_limit is NULL . When a user specifies NULL , or does not specify a value, this indicates that the default value should be used. This procedure can be run only from the CDB root ( CDB$ROOT ).