---
id: 19c__DBA_CDB_RSRC_PLAN_DIRECTIVES
name: DBA_CDB_RSRC_PLAN_DIRECTIVES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CDB_RSRC_PLAN_DIRECTIVES.html
---

# DBA_CDB_RSRC_PLAN_DIRECTIVES

DBA_CDB_RSRC_PLAN_DIRECTIVES provides information about all the CDB resource plan directives.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PLAN | VARCHAR2(128) | Name of the CDB resource plan to which this directive belongs |
| PLUGGABLE_DATABASE | VARCHAR2(128) | Name of the PDB referred to. NULL for profile directives |
| PROFILE | VARCHAR2(128) | For internal use only |
| DIRECTIVE_TYPE | VARCHAR2(30) | For internal use only |
| SHARES | NUMBER | Resource allocation, expressed in shares |
| UTILIZATION_LIMIT | NUMBER | Maximum resource utilization allowed, expressed in percentage |
| PARALLEL_SERVER_LIMIT | NUMBER | Maximum percentage of the parallel target used before queueing subsequent parallel queries |
| MEMORY_MIN | NUMBER | The percentage of Exadata Smart Flash Cache and Exadata PMEM cache that is guaranteed to the PDB This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache. See Oracle Exadata System Software User's Guide for more information. |
| MEMORY_LIMIT | NUMBER | The maximum percentage of Exadata Smart Flash Cache and Exadata PMEM cache that the PDB can use This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache. See Oracle Exadata System Software User's Guide for more information. |
| COMMENTS | VARCHAR2(2000) | Text comment on the resource plan directive |
| STATUS | VARCHAR2(128) | PENDING if it is part of the pending area, NULL otherwise |
| MANDATORY | VARCHAR2(3) | Whether the resource plan directive is mandatory. Mandatory plans cannot be deleted. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: ORA$DEFAULT_PDB_DIRECTIVE is the default directive for PDBs. For more information about ORA$DEFAULT_PDB_DIRECTIVE , see Oracle Multitenant Administrator's Guide . Note: ORA$DEFAULT_PDB_DIRECTIVE is the default directive for PDBs. For more information about ORA$DEFAULT_PDB_DIRECTIVE , see Oracle Multitenant Administrator's Guide . Note: Oracle recommends that you do not use the parallel_server_limit directive in a CDB resource plan. Note: Oracle recommends that you do not use the parallel_server_limit directive in a CDB resource plan.