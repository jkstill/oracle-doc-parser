---
id: 19c__DBA_RSRC_PLANS
name: DBA_RSRC_PLANS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_PLANS.html
---

# DBA_RSRC_PLANS

DBA_RSRC_PLANS displays information about all resource plans in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PLAN_ID | NUMBER | ID number of the resource plan |
| PLAN | VARCHAR2(128) | Name of the resource plan |
| NUM_PLAN_DIRECTIVES | NUMBER | Number of plan directives for the plan |
| CPU_METHOD | VARCHAR2(128) | CPU resource allocation method for the plan |
| MGMT_METHOD | VARCHAR2(128) | Resource allocation method for the plan |
| ACTIVE_SESS_POOL_MTH | VARCHAR2(128) | Active session pool resource allocation method for the plan |
| PARALLEL_DEGREE_LIMIT_MTH | VARCHAR2(128) | Parallel degree limit resource allocation method for the plan |
| QUEUING_MTH | VARCHAR2(128) | Queuing resource allocation method for the plan |
| SUB_PLAN | VARCHAR2(3) | Indicates whether the plan is a subplan ( YES ) or not ( NO ) |
| COMMENTS | VARCHAR2(2000) | Text comment on the plan |
| STATUS | VARCHAR2(128) | Indicates whether the plan is part of the pending area ( PENDING ) or not (NULL) |
| MANDATORY | VARCHAR2(3) | Indicates whether the plan is mandatory ( YES ) or not ( NO ). Mandatory plans cannot be deleted. |

## Usage Notes

For a list of currently active plans, see " V$RSRC_PLAN " . See Also: Oracle Database Administrator’s Guide for information on resource plans in general Oracle Database PL/SQL Packages and Types Reference for more information on creating resource plans with the DBMS_RESOURCE_MANAGER package See Also: Oracle Database Administrator’s Guide for information on resource plans in general Oracle Database PL/SQL Packages and Types Reference for more information on creating resource plans with the DBMS_RESOURCE_MANAGER package