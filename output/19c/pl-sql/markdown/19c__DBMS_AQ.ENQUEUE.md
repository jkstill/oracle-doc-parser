---
id: 19c__DBMS_AQ.ENQUEUE
name: DBMS_AQ.ENQUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.ENQUEUE

This procedure adds a message to the specified queue.

## Syntax

```sql
DBMS_AQ.ENQUEUE (
   queue_name          IN      VARCHAR2,
   enqueue_options     IN      enqueue_options_t,
   message_properties  IN      message_properties_t,
   payload             IN       "<ADT_1>",
   msgid               OUT     RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Specifies the name of the queue to which this message should be enqueued. The queue cannot be an exception queue. |
| enqueue_options | enqueue_options_t | IN | See ENQUEUE_OPTIONS_T Type . |
| message_properties | message_properties_t | IN | See MESSAGE_PROPERTIES_T Type . |
| payload | IN | IN | Not interpreted by Oracle Database Advanced Queuing. The payload must be specified according to the specification in the associated queue table. NULL is an acceptable parameter. For the definition of type_name refer to TYPE_NAME in DBMS_AQ Data Types . |
| msgid | RAW) | OUT | System generated identification of the message. This is a globally unique identifier that can be used to identify the message at dequeue time. |

## Usage Notes

Syntax DBMS_AQ.ENQUEUE ( queue_name IN VARCHAR2, enqueue_options IN enqueue_options_t, message_properties IN message_properties_t, payload IN "<ADT_1>", msgid OUT RAW); Parameters Table 22-9 ENQUEUE Procedure Parameters Parameter Description queue_name Specifies the name of the queue to which this message should be enqueued. The queue cannot be an exception queue. enqueue_options See ENQUEUE_OPTIONS_T Type . message_properties See MESSAGE_PROPERTIES_T Type . payload Not interpreted by Oracle Database Advanced Queuing. The payload must be specified according to the specification in the associated queue table. NULL is an acceptable parameter. For the definition of type_name refer to TYPE_NAME in DBMS_AQ Data Types . msgid System generated identification of the message. This is a globally unique identifier that can be used to identify the message at dequeue time. Usage Notes The sequence_deviation parameter in enqueue_options can be used to change the order of processing between two messages. The identity of the other message, if any, is specified by the enqueue_options parameter relative_msgid . The relationship is identified by the sequence_deviation parameter. Specifying sequence_deviation for a message introduces some restrictions for the delay and priority values that can be specified for this message. The delay of this message must be less than or equal to the delay of the message before which this message is to be enqueued. The priority of this message must be greater than or equal to the priority of the message before which this message is to be enqueued. Note: The sequence_deviation attribute has no effect in releases prior to Oracle Streams AQ 10g Release 1 (10.1) if message_grouping parameter of DBMS_AQADM subprograms is set to TRANSACTIONAL . The sequence deviation feature is deprecated in Oracle Streams AQ 10g Release 2 (10.2). If a message is enqueued to a multiconsumer queue with no recipient, and if the queue has no subscribers (or rule-based subscribers that match this message), then Oracle error ORA _ 24033 is raised. This is a warning that the message will be discarded because there are no recipients or subscribers to whom it can be delivered. Using Secure Queues For secure queues, you must specify the sender_id in the messages_properties parameter. See MESSAGE_PROPERTIES_T Type for more information about sender_id . When you use secure queues, the following are required: You must have created a valid Oracle Database Advanced Queuing agent using DBMS_AQADM.CREATE_AQ_AGENT . See CREATE_AQ_AGENT Procedure . You must map sender_id to a database user with enqueue privileges on the secure queue. Use DBMS_AQADM.ENABLE_DB_ACCESS to do this. See ENABLE_DB_ACCESS Procedure . Note: The sequence_deviation attribute has no effect in releases prior to Oracle Streams AQ 10g Release 1 (10.1) if message_grouping parameter of DBMS_AQADM subprograms is set to TRANSACTIONAL . The sequence deviation feature is deprecated in Oracle Streams AQ 10g Release 2 (10.2).