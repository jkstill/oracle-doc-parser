---
id: 19c__DBMS_AQ.DEQUEUE
name: DBMS_AQ.DEQUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.DEQUEUE

This procedure dequeues a message from the specified queue.

## Syntax

```sql
DBMS_AQ.DEQUEUE (
   queue_name          IN      VARCHAR2,
   dequeue_options     IN      dequeue_options_t,
   message_properties  OUT     message_properties_t,
   payload             OUT     "<ADT_1>"
   msgid               OUT     RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Specifies the name of the queue. |
| dequeue_options | dequeue_options_t | IN | See DEQUEUE_OPTIONS_T Type . |
| message_properties | message_properties_t | OUT | See MESSAGE_PROPERTIES_T Type . |
| payload | OUT | IN | Not interpreted by Oracle Database Advanced Queuing. The payload must be specified according to the specification in the associated queue table. For the definition of type_name refer to TYPE_NAME in DBMS_AQ Data Types . |
| msgid | RAW) | OUT | System generated identification of the message. |

## Usage Notes

Syntax DBMS_AQ.DEQUEUE ( queue_name IN VARCHAR2, dequeue_options IN dequeue_options_t, message_properties OUT message_properties_t, payload OUT "<ADT_1>" msgid OUT RAW); Parameters Table 22-7 DEQUEUE Procedure Parameters Parameter Description queue_name Specifies the name of the queue. dequeue_options See DEQUEUE_OPTIONS_T Type . message_properties See MESSAGE_PROPERTIES_T Type . payload Not interpreted by Oracle Database Advanced Queuing. The payload must be specified according to the specification in the associated queue table. For the definition of type_name refer to TYPE_NAME in DBMS_AQ Data Types . msgid System generated identification of the message. Usage Notes The search criteria for messages to be dequeued is determined by the following parameters in dequeue_options : consumer_name msgid Msgid uniquely identifies the message to be dequeued. Only messages in the READY state are dequeued unless msgid is specified. correlation Correlation identifiers are application-defined identifiers that are not interpreted by Oracle Database Advanced Queuing. deq_condition Dequeue condition is an expression based on the message properties, the message data properties and PL/SQL functions. A deq_condition is specified as a Boolean expression using syntax similar to the WHERE clause of a SQL query. This Boolean expression can include conditions on message properties, user data properties (object payloads only), and PL/SQL or SQL functions (as specified in the where clause of a SQL query). Message properties include priority, corrid and other columns in the queue table. To specify dequeue conditions on a message payload (object payload), use attributes of the object type in clauses. You must prefix each attribute with tab.user_data as a qualifier to indicate the specific column of the queue table that stores the payload. Example: tab.user_data.orderstatus='EXPRESS' The dequeue order is determined by the values specified at the time the queue table is created unless overridden by the msgid and correlation ID in dequeue_options . The database-consistent read mechanism is applicable for queue operations. For example, a BROWSE call may not see a message that is enqueued after the beginning of the browsing transaction. The default NAVIGATION parameter during dequeue is NEXT_MESSAGE . This means that subsequent dequeues will retrieve the messages from the queue based on the snapshot obtained in the first dequeue. In particular, a message that is enqueued after the first dequeue command will be processed only after processing all the remaining messages in the queue. This is usually sufficient when all the messages have already been enqueued into the queue, or when the queue does not have a priority-based ordering. However, applications must use the FIRST_MESSAGE navigation option when the first message in the queue needs to be processed by every dequeue command. This usually becomes necessary when a higher priority message arrives in the queue while messages already-enqueued are being processed. Note: It may be more efficient to use the FIRST_MESSAGE navigation option when messages are concurrently enqueued. If the FIRST_MESSAGE option is not specified, Oracle Database Advanced Queuing continually generates the snapshot as of the first dequeue command, leading to poor performance. If the FIRST_MESSAGE option is specified, then Oracle Database Advanced Queuing uses a new snapshot for every dequeue command. Messages enqueued in the same transaction into a queue that has been enabled for message grouping will form a group. If only one message is enqueued in the transaction, then this will effectively form a group of one message. There is no upper limit to the number of messages that can be grouped in a single transaction. In queues that have not been enabled for message grouping, a dequeue in LOCKED or REMOVE mode locks only a single message. By contrast, a dequeue operation that seeks to dequeue a message that is part of a group will lock the entire group. This is useful when all the messages in a group need to be processed as an atomic unit. When all the messages in a group have been dequeued, the dequeue returns an error indicating that all messages in the group have been processed. The application can then use the NEXT_TRANSACTION to start dequeuing messages from the next available group. In the event that no groups are available, the dequeue will time out after the specified WAIT period. Using Secure Queues For secure queues, you must specify consumer_name in the dequeue_options parameter. See DEQUEUE_OPTIONS_T Type for more information about consumer_name . When you use secure queues, the following are required: You must have created a valid Oracle Database Advanced Queuing agent using DBMS_AQADM.CREATE_AQ_AGENT . See CREATE_AQ_AGENT Procedure . You must map the Oracle Database Advanced Queuing agent to a database user with dequeue privileges on the secure queue. Use DBMS_AQADM.ENABLE_DB_ACCESS to do this. See ENABLE_DB_ACCESS Procedure . Note: It may be more efficient to use the FIRST_MESSAGE navigation option when messages are concurrently enqueued. If the FIRST_MESSAGE option is not specified, Oracle Database Advanced Queuing continually generates the snapshot as of the first dequeue command, leading to poor performance. If the FIRST_MESSAGE option is specified, then Oracle Database Advanced Queuing uses a new snapshot for every dequeue command.