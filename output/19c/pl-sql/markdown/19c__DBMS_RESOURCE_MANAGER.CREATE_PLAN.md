---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_PLAN
name: DBMS_RESOURCE_MANAGER.CREATE_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_PLAN

This procedure creates entries which define resource plans.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_PLAN (
   plan                       IN   VARCHAR2, 
   comment                    IN   VARCHAR2 DEFAULT NULL, 
   cpu_mth                    IN   VARCHAR2 DEFAULT NULL, -- deprecated
   active_sess_pool_mth       IN   VARCHAR2 DEFAULT 'ACTIVE_SESS_POOL_ABSOLUTE', 
   parallel_degree_limit_mth  IN   VARCHAR2 DEFAULT 
                                      'PARALLEL_DEGREE_LIMIT_ABSOLUTE',
   queueing_mth               IN   VARCHAR2 DEFAULT 'FIFO_TIMEOUT',
   mgmt_mth                   IN   VARCHAR2 DEFAULT 'EMPHASIS',
   sub_plan                   IN   BOOLEAN DEFAULT FALSE,
   max_iops                   IN   NUMBER DEFAULT NULL,
   max_mbps                   IN   NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the resource plan |
| comment | VARCHAR2 | IN | User comment |
| cpu_mth | VARCHAR2 | IN | Allocation method for CPU resources (deprecated) |
| active_sess_pool_mth | VARCHAR2 | IN | Active session pool resource allocation method. Limits the number of active sessions. All other sessions are inactive and wait in a queue to be activated. ACTIVE_SESS_POOL_ABSOLUTE is the default and only method available. |
| parallel_degree_limit_mth | VARCHAR2 | IN | Resource allocation method for specifying a limit on the degree of parallelism of any operation. PARALLEL_DEGREE_LIMIT_ABSOLUTE is the default and only method available. |
| queueing_mth | VARCHAR2 | IN | Queuing resource allocation method. Controls order in which queued inactive sessions will execute. FIFO_TIMEOUT is the default and only method available |
| mgmt_mth | VARCHAR2 | IN | Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets EMPHASIS - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups RATIO - for single-level plans that use ratios to specify how I/O resources are distributed |
| sub_plan | BOOLEAN | IN | If TRUE , indicates that this plan is only intended for use as a sub-plan. Sub-plans are not required to have an OTHER_GROUPS directive. Default is FALSE . |
| max_iops | NUMBER | IN | Nonoperative |
| max_mbps | NUMBER | IN | Nonoperative |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CREATE_PLAN ( plan IN VARCHAR2, comment IN VARCHAR2 DEFAULT NULL, cpu_mth IN VARCHAR2 DEFAULT NULL, -- deprecated active_sess_pool_mth IN VARCHAR2 DEFAULT 'ACTIVE_SESS_POOL_ABSOLUTE', parallel_degree_limit_mth IN VARCHAR2 DEFAULT 'PARALLEL_DEGREE_LIMIT_ABSOLUTE', queueing_mth IN VARCHAR2 DEFAULT 'FIFO_TIMEOUT', mgmt_mth IN VARCHAR2 DEFAULT 'EMPHASIS', sub_plan IN BOOLEAN DEFAULT FALSE, max_iops IN NUMBER DEFAULT NULL, max_mbps IN NUMBER DEFAULT NULL); Parameters Table 142-9 CREATE_PLAN Procedure Parameters Parameter Description plan Name of the resource plan comment User comment cpu_mth Allocation method for CPU resources (deprecated) active_sess_pool_mth Active session pool resource allocation method. Limits the number of active sessions. All other sessions are inactive and wait in a queue to be activated. ACTIVE_SESS_POOL_ABSOLUTE is the default and only method available. parallel_degree_limit_mth Resource allocation method for specifying a limit on the degree of parallelism of any operation. PARALLEL_DEGREE_LIMIT_ABSOLUTE is the default and only method available. queueing_mth Queuing resource allocation method. Controls order in which queued inactive sessions will execute. FIFO_TIMEOUT is the default and only method available mgmt_mth Resource allocation method for specifying how much resources (for example, CPU or I/O) each consumer group or sub-plan gets EMPHASIS - for multilevel plans that use percentages to specify how I/O resources are distributed among consumer groups RATIO - for single-level plans that use ratios to specify how I/O resources are distributed sub_plan If TRUE , indicates that this plan is only intended for use as a sub-plan. Sub-plans are not required to have an OTHER_GROUPS directive. Default is FALSE . max_iops Nonoperative max_mbps Nonoperative Usage Notes If you want to use any default resource allocation method, then you do not need to specify it when creating or updating a plan.