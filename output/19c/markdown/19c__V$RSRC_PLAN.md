---
id: 19c__V$RSRC_PLAN
name: V$RSRC_PLAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_PLAN.html
---

# V$RSRC_PLAN

V$RSRC_PLAN displays the names of all currently active resource plans.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| IS_TOP_PLAN | VARCHAR2(5) |  |
| CPU_MANAGED | VARCHAR2(3) |  |
| INSTANCE_CAGING | VARCHAR2(3) |  |
| PARALLEL_SERVERS_ACTIVE | NUMBER |  |
| PARALLEL_SERVERS_TOTAL | NUMBER |  |
| PARALLEL_EXECUTION_MANAGED | VARCHAR2(32) |  |
| CON_ID | NUMBER |  |
| DIRECTIVE_TYPE | VARCHAR2(32) |  |
| SHARES | NUMBER |  |
| UTILIZATION_LIMIT | NUMBER |  |
| PARALLEL_SERVER_LIMIT | NUMBER |  |
| MEMORY_MIN | NUMBER |  |
| MEMORY_LIMIT | NUMBER |  |
| PROFILE | VARCHAR2(32) |  |

## Usage Notes

The resource plan with CON_ID=ROOT is the CDB resource plan. See Also: " DBA_RSRC_PLANS " for a listing of all plans in the database " DBA_CDB_RSRC_PLANS " for information about CDB resource plans " DBA_CDB_RSRC_PLAN_DIRECTIVES " for information about CDB resource plan directives " DB_PERFORMANCE_PROFILE " Oracle Database Administrator’s Guide for information on resource plans Oracle Database PL/SQL Packages and Types Reference for information on defining resource allocation methods for consumer groups with the DBMS_RESOURCE_MANAGER package See Also: " DBA_RSRC_PLANS " for a listing of all plans in the database " DBA_CDB_RSRC_PLANS " for information about CDB resource plans " DBA_CDB_RSRC_PLAN_DIRECTIVES " for information about CDB resource plan directives " DB_PERFORMANCE_PROFILE " Oracle Database Administrator’s Guide for information on resource plans Oracle Database PL/SQL Packages and Types Reference for information on defining resource allocation methods for consumer groups with the DBMS_RESOURCE_MANAGER package