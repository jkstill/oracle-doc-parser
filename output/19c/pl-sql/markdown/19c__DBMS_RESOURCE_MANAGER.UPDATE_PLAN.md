---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_PLAN
name: DBMS_RESOURCE_MANAGER.UPDATE_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_PLAN

This procedure updates entries which define resource plans.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_PLAN (
   plan                               IN VARCHAR2, 
   new_comment                        IN VARCHAR2 DEFAULT NULL, 
   new_cpu_mth                        IN VARCHAR2 DEFAULT NULL, -- deprecated
   new_active_sess_pool_mth           IN VARCHAR2 DEFAULT NULL,
   new_parallel_degree_limit_mth      IN VARCHAR2 DEFAULT NULL,
   new_queueing_mth                   IN VARCHAR2 DEFAULT NULL,
   new_mgmt_mth                       IN VARCHAR2 DEFAULT NULL,
   new_sub_plan                       IN BOOLEAN DEFAULT FALSE,
   new_max_iops                       IN NUMBER DEFAULT NULL,
   new_max_mbps                       IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of resource plan |
| new_comment | VARCHAR2 | IN | New user comment |
| new_cpu_mth | VARCHAR2 | IN | Name of new allocation method for CPU resources (deprecated) |
| new_active_sess_pool_mth | VARCHAR2 | IN | Name of new method for maximum active sessions |
| new_parallel_degree_limit_mth | VARCHAR2 | IN | Name of new method for degree of parallelism |
| new_queueing_mth | VARCHAR2 | IN | Specifies type of queuing policy to use with active session pool feature |
| new_mgmt_mth | VARCHAR2 | IN | Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets EMPHASIS - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups. RATIO - for single-level plans that use ratios to specify how I/O resources are distributed. |
| new_sub_plan | BOOLEAN | IN | New setting for whether the plan is only intended for use as a sub-plan |
| new_max_iops | NUMBER | IN | Nonoperative |
| new_max_mbps | NUMBER | IN | Nonoperative |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_PLAN ( plan IN VARCHAR2, new_comment IN VARCHAR2 DEFAULT NULL, new_cpu_mth IN VARCHAR2 DEFAULT NULL, -- deprecated new_active_sess_pool_mth IN VARCHAR2 DEFAULT NULL, new_parallel_degree_limit_mth IN VARCHAR2 DEFAULT NULL, new_queueing_mth IN VARCHAR2 DEFAULT NULL, new_mgmt_mth IN VARCHAR2 DEFAULT NULL, new_sub_plan IN BOOLEAN DEFAULT FALSE, new_max_iops IN NUMBER DEFAULT NULL, new_max_mbps IN NUMBER DEFAULT NULL); Parameters Table 142-34 UPDATE_PLAN Procedure Parameters Parameter Description plan Name of resource plan new_comment New user comment new_cpu_mth Name of new allocation method for CPU resources (deprecated) new_active_sess_pool_mth Name of new method for maximum active sessions new_parallel_degree_limit_mth Name of new method for degree of parallelism new_queueing_mth Specifies type of queuing policy to use with active session pool feature new_mgmt_mth Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets EMPHASIS - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups. RATIO - for single-level plans that use ratios to specify how I/O resources are distributed. new_sub_plan New setting for whether the plan is only intended for use as a sub-plan new_max_iops Nonoperative new_max_mbps Nonoperative Usage Notes If the parameters to UPDATE_PLAN Procedure are not specified, then they remain unchanged in the data dictionary. If you want to use any default resource allocation method, then you do not need to specify it when creating or updating a plan. To clear (reset to the directive's default value), use the value -1 .