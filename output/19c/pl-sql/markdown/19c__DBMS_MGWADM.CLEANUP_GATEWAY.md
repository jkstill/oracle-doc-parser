---
id: 19c__DBMS_MGWADM.CLEANUP_GATEWAY
name: DBMS_MGWADM.CLEANUP_GATEWAY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.CLEANUP_GATEWAY

This procedure cleans up Messaging Gateway. The procedure performs cleanup or recovery actions that may be needed when Messaging Gateway is left in some abnormal or unexpected condition. The MGW_GATEWAY view lists Messaging Gateway status and configuration information that pertains to the cleanup actions.

## Syntax

```sql
DBMS_MGWADM.CLEANUP_GATEWAY(
   action       IN   BINARY_INTEGER,
   sarg         IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| action | BINARY_INTEGER | IN | The cleanup action to be performed. Values: DBMS_MGWADM.CLEAN_STARTUP_STATE for Messaging Gateway start up state recovery DBMS_MGWADM.CLEAN_LOG_QUEUES for log queue cleanup DBMS_MGWADM.RESET_SUB_MISSING_LOG_REC for propagation job recovery due to missing log record DBMS_MGWADM.RESET_SUB_MISSING_MESSAGE for propagation job recovery due to missing message |
| sarg | VARCHAR2 | IN | Optional argument whose meaning depends on the value specified for action . This should be NULL if it is not used for the specified action. |
| agent_name |  |  | Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |

## Usage Notes

Syntax DBMS_MGWADM.CLEANUP_GATEWAY( action IN BINARY_INTEGER, sarg IN VARCHAR2 DEFAULT NULL); DBMS_MGWADM.CLEANUP_GATEWAY( agent_name IN VARCHAR2, action IN BINARY_INTEGER, sarg IN VARCHAR2 DEFAULT NULL ); Parameters Table 110-27 CLEANUP_GATEWAY Procedure Parameters Parameter Description action The cleanup action to be performed. Values: DBMS_MGWADM.CLEAN_STARTUP_STATE for Messaging Gateway start up state recovery DBMS_MGWADM.CLEAN_LOG_QUEUES for log queue cleanup DBMS_MGWADM.RESET_SUB_MISSING_LOG_REC for propagation job recovery due to missing log record DBMS_MGWADM.RESET_SUB_MISSING_MESSAGE for propagation job recovery due to missing message sarg Optional argument whose meaning depends on the value specified for action . This should be NULL if it is not used for the specified action. agent_name Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. Usage Notes CLEAN_STARTUP_STATE sarg is not used and must be NULL . The CLEAN_STARTUP_STATE action recovers Messaging Gateway to a known state when the Messaging Gateway agent has crashed or some other abnormal event occurs, and Messaging Gateway cannot be restarted. This should be done only when the Messaging Gateway agent has been started but appears to have crashed or has been nonresponsive for an extended period of time. The CLEAN_STARTUP_STATE action may be needed when the MGW_GATEWAY view shows that the AGENT_STATUS value is something other than NOT_STARTED or START_SCHEDULED, and the AGENT_PING value is UNREACHABLE for an extended period of time. If the AGENT_STATUS value is BROKEN , then the Messaging Gateway agent cannot be started until the problem has been resolved and the CLEAN_STARTUP_STATE action used to reset the agent status. A BROKEN status can indicate that the Messaging Gateway start job detected a Messaging Gateway agent already running. This condition that should never occur under normal use. Cleanup tasks include: Removing the Scheduler job used to start the external Messaging Gateway agent process. Setting certain configuration information to a known state. For example, setting the agent status to NOT_STARTED. Execution of this command fails if: The agent status is NOT_STARTED or START_SCHEDULED. No shutdown attempt has been made prior to calling this procedure, except if the agent status is STARTING. The Messaging Gateway agent is successfully contacted. The assumption is that the agent is active, and this procedure fails. If the agent does not respond after several attempts have been made, then the cleanup tasks are performed. This procedure takes at least several seconds and possibly up to one minute. This is expected behavior under conditions where this particular cleanup action is appropriate and necessary. Note: Terminate any Messaging Gateway agent process that may still be running after a CLEAN_STARTUP_STATE action has been successfully performed. This should be done before calling DBMS_MGWADM . STARTUP to start Messaging Gateway. The process is usually named extprocmgwextproc . CLEAN_LOG_QUEUES sarg is not used and must be NULL . The Messaging Gateway agent will clean log queues for all configured messaging system links. The agent will temporarily stop all propagation activity and then remove all obsolete and bad log records from the log queues for all links. The procedure will fail if the Messaging Gateway agent is not running. This cleanup action is automatically performed each time the Messaging Gateway agent is started. Note: The CLEAN_LOG_QUEUES action is performed only on agent startup. If this procedure is called when the agent is running, then the Messaging Gateway agent ignores it. RESET_SUB_MISSING_LOG_REC sarg specifies a Messaging Gateway job name (or subscriber ID) to be reset. It must not be NULL . The Messaging Gateway agent recovers a Messaging Gateway propagation job that has failed due to a missing log record. The agent will reset the source and destination log records. The procedure will fail if the Messaging Gateway agent is not running. Note: If the messages in the source queue had already been propagated to the destination queue, then this action may result in duplicate messages. RESET_SUB_MISSING_MESSAGE sarg specifies a Messaging Gateway job name (or subscriber ID) to be reset. It must not be NULL . The Messaging Gateway agent recovers a Messaging Gateway propagation job that has failed due to a missing persistent source message. The agent will treat the message as a non-persistent message and continue processing that propagation job. The procedure will fail if the Messaging Gateway agent is not running. Note: Terminate any Messaging Gateway agent process that may still be running after a CLEAN_STARTUP_STATE action has been successfully performed. This should be done before calling DBMS_MGWADM . STARTUP to start Messaging Gateway. The process is usually named extprocmgwextproc . Note: The CLEAN_LOG_QUEUES action is performed only on agent startup. If this procedure is called when the agent is running, then the Messaging Gateway agent ignores it.