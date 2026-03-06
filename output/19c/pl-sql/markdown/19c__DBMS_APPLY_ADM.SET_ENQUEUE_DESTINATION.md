---
id: 19c__DBMS_APPLY_ADM.SET_ENQUEUE_DESTINATION
name: DBMS_APPLY_ADM.SET_ENQUEUE_DESTINATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.SET_ENQUEUE_DESTINATION

This procedure sets the queue where the apply component automatically enqueues a message that satisfies the specified rule.

## Syntax

```sql
DBMS_APPLY_ADM.SET_ENQUEUE_DESTINATION(
  rule_name               IN  VARCHAR2,
  destination_queue_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule, specified as [ schema_name .] rule_name . For example, to specify a rule named hr5 in the hr schema, enter hr.hr5 for this parameter. If the schema is not specified, then the current user is the default. |
| destination_queue_name | VARCHAR2) | IN | The name of the queue into which the apply component enqueues the message. Specify the queue in the form [ schema_name .] queue_name . Only local queues can be specified. For example, to specify a queue in the hr schema named streams_queue , enter hr.streams_queue . If the schema is not specified, then the current user is the default. If NULL , then an existing name-value pair with the name APPLY$_ENQUEUE is removed. If no name-value pair exists with the name APPLY$_ENQUEUE for the rule, then no action is taken. If non- NULL and a name-value pair exists for the rule with the name APPLY$_ENQUEUE , then it is removed, and a new name-value pair with the value specified by this parameter is added. |

## Usage Notes

This procedure modifies the specified rule's action context to specify the queue. A rule action context is optional information associated with a rule that is interpreted by the client of the rules engine after the rule evaluates to TRUE for a message. In this case, the client of the rules engine is an apply component. The information in an action context is an object of type SYS.RE$NV_LIST , which consists of a list of name-value pairs. A queue destination specified by this procedure always consists of the following name-value pair in an action context: The name is APPLY$_ENQUEUE . The value is an ANYDATA instance containing the queue name specified as a VARCHAR2 . Syntax DBMS_APPLY_ADM.SET_ENQUEUE_DESTINATION( rule_name IN VARCHAR2, destination_queue_name IN VARCHAR2); Parameters Table 21-18 SET_ENQUEUE_DESTINATION Procedure Parameters Parameter Description rule_name The name of the rule, specified as [ schema_name .] rule_name . For example, to specify a rule named hr5 in the hr schema, enter hr.hr5 for this parameter. If the schema is not specified, then the current user is the default. destination_queue_name The name of the queue into which the apply component enqueues the message. Specify the queue in the form [ schema_name .] queue_name . Only local queues can be specified. For example, to specify a queue in the hr schema named streams_queue , enter hr.streams_queue . If the schema is not specified, then the current user is the default. If NULL , then an existing name-value pair with the name APPLY$_ENQUEUE is removed. If no name-value pair exists with the name APPLY$_ENQUEUE for the rule, then no action is taken. If non- NULL and a name-value pair exists for the rule with the name APPLY$_ENQUEUE , then it is removed, and a new name-value pair with the value specified by this parameter is added. Usage Notes The following usage notes apply to this procedure: The SET_ENQUEUE_DESTINATION Procedure and Apply Handlers Considerations for the SET_ENQUEUE_DESTINATION Procedure The SET_ENQUEUE_DESTINATION Procedure and XStream Outbound Servers The SET_ENQUEUE_DESTINATION Procedure and XStream Inbound Servers The SET_ENQUEUE_DESTINATION Procedure and Apply Handlers If an apply handler, such as a procedure DML handler, DDL handler, or message handler, processes a message that also is enqueued into a destination queue, then the apply handler processes the message before it is enqueued. Considerations for the SET_ENQUEUE_DESTINATION Procedure The following are considerations for using this procedure: This procedure does not verify that the specified queue exists. If the queue does not exist, then an error is raised when an apply component tries to enqueue a message into it. Oracle Replication capture processes, propagations, and messaging clients ignore the action context created by this procedure. The apply user of the apply component using the specified rule must have the necessary privileges to enqueue messages into the specified queue. If the queue is a secure queue, then the apply user must be a secure queue user of the queue. The specified rule must be in the positive rule set for an apply component. If the rule is in the negative rule set for an apply component, then the apply component does not enqueue the message into the destination queue. If the commit SCN for a message is less than or equal to the relevant instantiation SCN for the message, then the message is not enqueued into the destination queue, even if the message satisfies the apply component rule sets. The SET_ENQUEUE_DESTINATION Procedure and XStream Outbound Servers This procedure has no effect on XStream outbound servers. The SET_ENQUEUE_DESTINATION Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.