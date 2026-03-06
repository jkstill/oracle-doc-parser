---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE

This procedure updates resource plan directives.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE (
   plan                             IN VARCHAR2, 
   group_or_subplan                 IN VARCHAR2, 
   new_comment                      IN VARCHAR2 DEFAULT NULL, 
   new_cpu_p1                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p2                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p3                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p4                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p5                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p6                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p7                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_cpu_p8                       IN NUMBER   DEFAULT NULL, -- deprecated 
   new_active_sess_pool_p1          IN NUMBER   DEFAULT NULL,
   new_queueing_p1                  IN NUMBER   DEFAULT NULL,
   new_parallel_degree_limit_p1     IN NUMBER   DEFAULT NULL,
   new_switch_group                 IN VARCHAR2 DEFAULT NULL, 
   new_switch_time                  IN NUMBER   DEFAULT NULL, 
   new_switch_estimate              IN BOOLEAN  DEFAULT FALSE, 
   new_max_est_exec_time            IN NUMBER   DEFAULT NULL, 
   new_undo_pool                    IN NUMBER   DEFAULT NULL,
   new_max_idle_time                IN NUMBER   DEFAULT NULL,
   new_max_idle_blocker_time        IN NUMBER   DEFAULT NULL,
   switch_time_in_call              IN NUMBER   DEFAULT NULL, -- deprecated
   new_mgmt_p1                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p2                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p3                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p4                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p5                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p6                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p7                      IN NUMBER   DEFAULT NULL,
   new_mgmt_p8                      IN NUMBER   DEFAULT NULL,
   new_switch_io_megabytes          IN NUMBER   DEFAULT NULL,
   new_switch_io_reqs               IN NUMBER   DEFAULT NULL,
   new_switch_for_call              IN BOOLEAN  DEFAULT NULL,
   new_max_utilization_limit        IN NUMBER   DEFAULT NULL,
   new_parallel_target_percentage   IN NUMBER   DEFAULT NULL, 
   new_parallel_queue_timeout       IN NUMBER   DEFAULT NULL,   
   new_parallel_server_limit        IN NUMBER   DEFAULT NULL,
   new_utilization_limit            IN NUMBER   DEFAULT NULL,
   new_switch_io_logical            IN NUMBER   DEFAULT NULL,
   new_switch_elapsed_time          IN NUMBER   DEFAULT NULL,
   new_shares                       IN NUMBER   DEFAULT NULL,
   new_parallel_stmt_critical       IN VARCHAR2 DEFAULT NULL,
   new_session_pga_limit            IN NUMBER   DEFAULT NULL,
   new_pq_timeout_action            IN NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the resource plan |
| group_or_subplan | VARCHAR2 | IN | Name of the consumer group or subplan |
| new_comment | VARCHAR2 | IN | Comment for the plan directive |
| new_cpu_p1 | NUMBER | IN | Deprecated - use new_mgmt_p1 instead |
| new_cpu_p2 | NUMBER | IN | Deprecated - use new_mgmt_p2 instead |
| new_cpu_p3 | NUMBER | IN | Deprecated - use new_mgmt_p3 instead |
| new_cpu_p4 | NUMBER | IN | Deprecated- use new_mgmt_p4 instead |
| new_cpu_p5 | NUMBER | IN | Deprecated - use new_mgmt_p5 instead |
| new_cpu_p6 | NUMBER | IN | Deprecated- use new_mgmt_p6 instead |
| new_cpu_p7 | NUMBER | IN | Deprecated- use new_mgmt_p7 instead |
| new_cpu_p8 | NUMBER | IN | Deprecated- use new_mgmt_p8 instead |
| new_active_sess_pool_p1 | NUMBER | IN | Specifies maximum number of concurrently active sessions for a consumer group. Default is NULL , which means unlimited. |
| new_queueing_p1 | NUMBER | IN | Specified time (in seconds) after which a job in the inactive session queue (waiting for execution) will time out. Default is NULL , which means unlimited. |
| new_parallel_degree_limit_p1 | NUMBER | IN | Specifies a limit on the degree of parallelism for any operation. Default is NULL , which means unlimited. |
| new_switch_group | VARCHAR2 | IN | Specifies consumer group to which this session is switched if other switch criteria are met. Default is NULL . If the group name is ' CANCEL_SQL ', the current call will be canceled when other switch criteria are met. If the group name is ' KILL_SESSION ', the session will be killed when other switch criteria are met. |
| new_switch_time | NUMBER | IN | Specifies time (in CPU seconds) that a session can execute before an action is taken. Default is NULL , which means unlimited. |
| new_switch_estimate | BOOLEAN | IN | If TRUE , tells Oracle to use its execution time estimate to automatically switch the consumer group of an operation before beginning its execution. Default is FALSE . |
| new_max_est_exec_time | NUMBER | IN | Specifies the maximum execution time (in CPU seconds) allowed for a session. If the optimizer estimates that an operation will take longer than MAX_EST_EXEC_TIME , the operation is not started and ORA-07455 is issued. If the optimizer does not provide an estimate, this directive has no effect. Default is NULL , which means unlimited. |
| new_undo_pool | NUMBER | IN | Limits the size in kilobytes of the undo records corresponding to uncommitted transactions by this consumer group |
| new_max_idle_time | NUMBER | IN | Indicates the maximum session idle time. Default is NULL , which means unlimited. |
| new_max_idle_blocker_time | NUMBER | IN | Maximum amount of time in seconds that a session can be idle while blocking another session's acquisition of a resource |
| new_switch_time_in_call |  |  | Deprecated. If this parameter is specified, new_switch_time will be effectively set to new_switch_time_in_call and new_switch_for_call will be effectively set to TRUE . |
| new_mgmt_p1 | NUMBER | IN | Resource allocation value for level 1 (replaces new_cpu_p1 ): EMPHASIS - specifies the resource percentage at the first level RATIO - specifies the weight of resource usage |
| new_mgmt_p2 | NUMBER | IN | Resource allocation value for level 2 (replaces new_cpu_p2 ) EMPHASIS - specifies the resource percentage at the second level RATIO - non-applicable |
| new_mgmt_p3 | NUMBER | IN | Resource allocation value for level 3 (replaces new_cpu_p3 ) EMPHASIS - specifies the resource percentage at the third level RATIO - non-applicable |
| new_mgmt_p4 | NUMBER | IN | Resource allocation value for level 4 (replaces new_cpu_p4 ) EMPHASIS - specifies the resource percentage at the fourth level RATIO - non-applicable |
| new_mgmt_p5 | NUMBER | IN | Resource allocation value for level 5 (replaces new_cpu_p5 ) EMPHASIS - specifies the resource percentage at the fifth level RATIO - non-applicable |
| new_mgmt_p6 | NUMBER | IN | Resource allocation value for level 6 (replaces new_cpu_p6 ) EMPHASIS - specifies the resource percentage at the sixth level RATIO - non-applicable |
| new_mgmt_p7 | NUMBER | IN | Resource allocation value for level 7 (replaces new_cpu_p7 ) EMPHASIS - specifies the resource percentage at the seventh level RATIO - non-applicable |
| new_mgmt_p8 | NUMBER | IN | Resource allocation value for level 8 (replaces new_cpu_p8 ) EMPHASIS - specifies the resource percentage at the eighth level RATIO - non-applicable |
| new_switch_io_megabytes | NUMBER | IN | Specifies the amount of I/O (in MB) that a session can issue before an action is taken. Default is NULL , which means unlimited. |
| new_switch_io_reqs | NUMBER | IN | Specifies the number of I/O requests that a session can issue before an action is taken. Default is NULL , which means unlimited. |
| new_switch_for_call | BOOLEAN | IN | Specifies that if an action is taken because of the new_switch_time , new_switch_io_megabytes , or new_switch_io_reqs parameters, the consumer group is restored to its original consumer group at the end of the top call. Default is FALSE , which means that the original consumer group is not restored at the end of the top call. |
| new_max_utilization_limit | NUMBER | IN | Deprecated - use new_utilization_limit instead |
| new_parallel_target_percentage | NUMBER | IN | Deprecated - use new_parallel_server_limit instead |
| new_parallel_server_limit | NUMBER | IN | Parallel server limit. Setting this overwrites the limit for parallel server set by utilization_limit . |
| new_utilization_limit | NUMBER | IN | Resource limit. For CPU, this limits the CPU utilization for the consumer group. For parallel servers, this limits the parallel servers used as a percentage of parallel_servers_target . |
| new_switch_elapsed_time | NUMBER | IN | Elapsed time that will trigger the action specified by switch_group . As with other switch directives, if new_switch_for_call is TRUE , the elapsed time is accumulated from the start of a call. Otherwise, the elapsed time is accumulated for the length of the session. |
| new_shares | NUMBER | IN | Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If CPU Resource Manager and Exadata I/O Resource Manager are enabled, then the default value is 1 . |
| new_parallel_stmt_critical | VARCHAR2 | IN | If set to BYPASS_QUEUE , parallel statements from this consumer group are not queued. If set to QUEUE , all the parallel statements, irrespective of the parallel_degree_policy parameter value, from the consumer group get queued. Default is FALSE , which means that certain parallel statements are eligible for queuing depending upon the parallel_degree_policy parameter value. |
| new_session_pga_limit | NUMBER | IN | Maximum amount of PGA in MB that sessions in this consumer group can allocate before being terminated. NULL (default) indicates no change. |
| new_parallel_queue_timeout | NUMBER | IN | Specifies the time (in seconds) that a parallel statement may remain in its Consumer Group's parallel statement queue before it is removed. The default action of this parameter is ERROR . This action can be altered using the new_pq_timeout_action parameter. |
| new_pq_timeout_action | NUMBER | IN | Specifies the action to be taken when a parallel statement is removed from the queue due to new_parallel_queue_timeout . The values are: CANCEL — The SQL statement is terminated with error ORA-7454 RUN — The SQL statement runs immediately, and might get downgraded if parallel servers are unavailable |

## Usage Notes

Note: The parameters new_max_utilization_limit and new_parallel_target_percentage are deprecated with Oracle Database 11g Release 1 (12.1.0.1), and are replaced by new_utilization_limit and new_parallel_server_limit . Note: The parameters new_max_utilization_limit and new_parallel_target_percentage are deprecated with Oracle Database 11g Release 1 (12.1.0.1), and are replaced by new_utilization_limit and new_parallel_server_limit . Syntax DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE ( plan IN VARCHAR2, group_or_subplan IN VARCHAR2, new_comment IN VARCHAR2 DEFAULT NULL, new_cpu_p1 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p2 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p3 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p4 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p5 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p6 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p7 IN NUMBER DEFAULT NULL, -- deprecated new_cpu_p8 IN NUMBER DEFAULT NULL, -- deprecated new_active_sess_pool_p1 IN NUMBER DEFAULT NULL, new_queueing_p1 IN NUMBER DEFAULT NULL, new_parallel_degree_limit_p1 IN NUMBER DEFAULT NULL, new_switch_group IN VARCHAR2 DEFAULT NULL, new_switch_time IN NUMBER DEFAULT NULL, new_switch_estimate IN BOOLEAN DEFAULT FALSE, new_max_est_exec_time IN NUMBER DEFAULT NULL, new_undo_pool IN NUMBER DEFAULT NULL, new_max_idle_time IN NUMBER DEFAULT NULL, new_max_idle_blocker_time IN NUMBER DEFAULT NULL, switch_time_in_call IN NUMBER DEFAULT NULL, -- deprecated new_mgmt_p1 IN NUMBER DEFAULT NULL, new_mgmt_p2 IN NUMBER DEFAULT NULL, new_mgmt_p3 IN NUMBER DEFAULT NULL, new_mgmt_p4 IN NUMBER DEFAULT NULL, new_mgmt_p5 IN NUMBER DEFAULT NULL, new_mgmt_p6 IN NUMBER DEFAULT NULL, new_mgmt_p7 IN NUMBER DEFAULT NULL, new_mgmt_p8 IN NUMBER DEFAULT NULL, new_switch_io_megabytes IN NUMBER DEFAULT NULL, new_switch_io_reqs IN NUMBER DEFAULT NULL, new_switch_for_call IN BOOLEAN DEFAULT NULL, new_max_utilization_limit IN NUMBER DEFAULT NULL, new_parallel_target_percentage IN NUMBER DEFAULT NULL, new_parallel_queue_timeout IN NUMBER DEFAULT NULL, new_parallel_server_limit IN NUMBER DEFAULT NULL, new_utilization_limit IN NUMBER DEFAULT NULL, new_switch_io_logical IN NUMBER DEFAULT NULL, new_switch_elapsed_time IN NUMBER DEFAULT NULL, new_shares IN NUMBER DEFAULT NULL, new_parallel_stmt_critical IN VARCHAR2 DEFAULT NULL, new_session_pga_limit IN NUMBER DEFAULT NULL, new_pq_timeout_action IN NUMBER DEFAULT NULL); Parameters Table 142-35 UPDATE_PLAN_DIRECTIVE Procedure Parameters Parameter Description plan Name of the resource plan group_or_subplan Name of the consumer group or subplan new_comment Comment for the plan directive new_cpu_p1 Deprecated - use new_mgmt_p1 instead new_cpu_p2 Deprecated - use new_mgmt_p2 instead new_cpu_p3 Deprecated - use new_mgmt_p3 instead new_cpu_p4 Deprecated- use new_mgmt_p4 instead new_cpu_p5 Deprecated - use new_mgmt_p5 instead new_cpu_p6 Deprecated- use new_mgmt_p6 instead new_cpu_p7 Deprecated- use new_mgmt_p7 instead new_cpu_p8 Deprecated- use new_mgmt_p8 instead new_active_sess_pool_p1 Specifies maximum number of concurrently active sessions for a consumer group. Default is NULL , which means unlimited. new_queueing_p1 Specified time (in seconds) after which a job in the inactive session queue (waiting for execution) will time out. Default is NULL , which means unlimited. new_parallel_degree_limit_p1 Specifies a limit on the degree of parallelism for any operation. Default is NULL , which means unlimited. new_switch_group Specifies consumer group to which this session is switched if other switch criteria are met. Default is NULL . If the group name is ' CANCEL_SQL ', the current call will be canceled when other switch criteria are met. If the group name is ' KILL_SESSION ', the session will be killed when other switch criteria are met. new_switch_time Specifies time (in CPU seconds) that a session can execute before an action is taken. Default is NULL , which means unlimited. new_switch_estimate If TRUE , tells Oracle to use its execution time estimate to automatically switch the consumer group of an operation before beginning its execution. Default is FALSE . new_max_est_exec_time Specifies the maximum execution time (in CPU seconds) allowed for a session. If the optimizer estimates that an operation will take longer than MAX_EST_EXEC_TIME , the operation is not started and ORA-07455 is issued. If the optimizer does not provide an estimate, this directive has no effect. Default is NULL , which means unlimited. new_undo_pool Limits the size in kilobytes of the undo records corresponding to uncommitted transactions by this consumer group new_max_idle_time Indicates the maximum session idle time. Default is NULL , which means unlimited. new_max_idle_blocker_time Maximum amount of time in seconds that a session can be idle while blocking another session's acquisition of a resource new_switch_time_in_call Deprecated. If this parameter is specified, new_switch_time will be effectively set to new_switch_time_in_call and new_switch_for_call will be effectively set to TRUE . new_mgmt_p1 Resource allocation value for level 1 (replaces new_cpu_p1 ): EMPHASIS - specifies the resource percentage at the first level RATIO - specifies the weight of resource usage new_mgmt_p2 Resource allocation value for level 2 (replaces new_cpu_p2 ) EMPHASIS - specifies the resource percentage at the second level RATIO - non-applicable new_mgmt_p3 Resource allocation value for level 3 (replaces new_cpu_p3 ) EMPHASIS - specifies the resource percentage at the third level RATIO - non-applicable new_mgmt_p4 Resource allocation value for level 4 (replaces new_cpu_p4 ) EMPHASIS - specifies the resource percentage at the fourth level RATIO - non-applicable new_mgmt_p5 Resource allocation value for level 5 (replaces new_cpu_p5 ) EMPHASIS - specifies the resource percentage at the fifth level RATIO - non-applicable new_mgmt_p6 Resource allocation value for level 6 (replaces new_cpu_p6 ) EMPHASIS - specifies the resource percentage at the sixth level RATIO - non-applicable new_mgmt_p7 Resource allocation value for level 7 (replaces new_cpu_p7 ) EMPHASIS - specifies the resource percentage at the seventh level RATIO - non-applicable new_mgmt_p8 Resource allocation value for level 8 (replaces new_cpu_p8 ) EMPHASIS - specifies the resource percentage at the eighth level RATIO - non-applicable new_switch_io_megabytes Specifies the amount of I/O (in MB) that a session can issue before an action is taken. Default is NULL , which means unlimited. new_switch_io_reqs Specifies the number of I/O requests that a session can issue before an action is taken. Default is NULL , which means unlimited. new_switch_for_call Specifies that if an action is taken because of the new_switch_time , new_switch_io_megabytes , or new_switch_io_reqs parameters, the consumer group is restored to its original consumer group at the end of the top call. Default is FALSE , which means that the original consumer group is not restored at the end of the top call. new_max_utilization_limit Deprecated - use new_utilization_limit instead new_parallel_target_percentage Deprecated - use new_parallel_server_limit instead new_parallel_server_limit Parallel server limit. Setting this overwrites the limit for parallel server set by utilization_limit . new_utilization_limit Resource limit. For CPU, this limits the CPU utilization for the consumer group. For parallel servers, this limits the parallel servers used as a percentage of parallel_servers_target . new_switch_elapsed_time Elapsed time that will trigger the action specified by switch_group . As with other switch directives, if new_switch_for_call is TRUE , the elapsed time is accumulated from the start of a call. Otherwise, the elapsed time is accumulated for the length of the session. new_shares Specifies the share of resource allocation for the pluggable database. CPU Resource Manager and Exadata I/O Resource Manager are enabled by specifying shares for each PDB. The shares parameter is also used for Parallel Statement Queuing. If CPU Resource Manager and Exadata I/O Resource Manager are enabled, then the default value is 1 . new_parallel_stmt_critical If set to BYPASS_QUEUE , parallel statements from this consumer group are not queued. If set to QUEUE , all the parallel statements, irrespective of the parallel_degree_policy parameter value, from the consumer group get queued. Default is FALSE , which means that certain parallel statements are eligible for queuing depending upon the parallel_degree_policy parameter value. new_session_pga_limit Maximum amount of PGA in MB that sessions in this consumer group can allocate before being terminated. NULL (default) indicates no change. new_parallel_queue_timeout Specifies the time (in seconds) that a parallel statement may remain in its Consumer Group's parallel statement queue before it is removed. The default action of this parameter is ERROR . This action can be altered using the new_pq_timeout_action parameter. new_pq_timeout_action Specifies the action to be taken when a parallel statement is removed from the queue due to new_parallel_queue_timeout . The values are: CANCEL — The SQL statement is terminated with error ORA-7454 RUN — The SQL statement runs immediately, and might get downgraded if parallel servers are unavailable Usage Notes If the parameters for UPDATE_PLAN_DIRECTIVE are left unspecified, then they remain unchanged in the data dictionary. For new_max_idle_time and new_max_idle_blocker_time , PMON will check these limits once a minute. If it finds a session that has exceeded one of the limits, it will forcibly kill the session and clean up all its state. The parameter new_switch_time_in_call is mostly useful for three-tier applications where the mid-tier server is implementing session pooling. By turning on new_switch_time_in_call , the resource usage of one client will not affect the consumer group of a future client that happens to be executed on the same session. To clear (reset to the directive's default value), use the value -1 .