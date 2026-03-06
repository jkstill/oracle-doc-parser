---
id: 19c__DBMS_AQ.DEQUEUE_ARRAY
name: DBMS_AQ.DEQUEUE_ARRAY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.DEQUEUE_ARRAY

This function dequeues an array of messages and returns them in the form of an array of payloads, an array of message properties and an array of message IDs. This function returns the number of messages successfully dequeued.

## Syntax

```sql
DBMS_AQ.DEQUEUE_ARRAY (
   queue_name                IN   VARCHAR2,
   dequeue_options           IN   dequeue_options_t,
   array_size                IN   pls_integer,
   message_properties_array  OUT  message_properties_array_t,
   payload_array             OUT  "<COLLECTION_1>",
   msgid_array               OUT  msgid_array_t,
   error_array               OUT  error_array_t)
RETURN pls_integer;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | The queue name from which messages are dequeued (same as single-row dequeue). |
| dequeue_options | dequeue_options_t | IN | The set of options which will be applied to all messages in the array (same as single-row dequeue). |
| array_size | pls_integer | IN | The number of elements to dequeue. For buffered messages, array_size should be 1 . |
| message_properties_array | message_properties_array_t | OUT | A record containing an array corresponding to each message property. Each payload element has a corresponding set of message properties. See MESSAGE_PROPERTIES_ARRAY_T Type . |
| payload_array | OUT | IN | An array of dequeued payload data. "<COLLECTION_1>" can be an associative array, varray or nested table in its PL/SQL representation. Users can dequeue RAW and ADT payloads. |
| msgid_array | msgid_array_t | OUT | An array of message IDs of the dequeued messages. See MSGID_ARRAY_T Type . |
| error_array | error_array_t) | OUT | Currently not implemented |

**Returns:** `pls_integer`

## Usage Notes

Syntax DBMS_AQ.DEQUEUE_ARRAY ( queue_name IN VARCHAR2, dequeue_options IN dequeue_options_t, array_size IN pls_integer, message_properties_array OUT message_properties_array_t, payload_array OUT "<COLLECTION_1>", msgid_array OUT msgid_array_t, error_array OUT error_array_t) RETURN pls_integer; Parameters Table 22-8 DEQUEUE_ARRAY Function Parameters Parameter Description queue_name The queue name from which messages are dequeued (same as single-row dequeue). dequeue_options The set of options which will be applied to all messages in the array (same as single-row dequeue). array_size The number of elements to dequeue. For buffered messages, array_size should be 1 . message_properties_array A record containing an array corresponding to each message property. Each payload element has a corresponding set of message properties. See MESSAGE_PROPERTIES_ARRAY_T Type . payload_array An array of dequeued payload data. "<COLLECTION_1>" can be an associative array, varray or nested table in its PL/SQL representation. Users can dequeue RAW and ADT payloads. msgid_array An array of message IDs of the dequeued messages. See MSGID_ARRAY_T Type . error_array Currently not implemented Usage Notes A nonzero wait time, as specified in dequeue_options , is recognized only when there are no messages in the queue. If the queue contains messages that are eligible for dequeue, then the DEQUEUE_ARRAY function will dequeue up to array_size messages and return immediately. Dequeue by message_id is not supported. See DEQUEUE Procedure for more information on the navigation parameter. Existing NAVIGATION modes are supported. In addition, two new NAVIGATION modes are supported for queues enabled for message grouping: FIRST_MESSAGE_MULTI_GROUP NEXT_MESSAGE_MULTI_GROUP See Also: ENQUEUE_OPTIONS_T Type For transaction grouped queues and ONE_GROUP navigation, messages are dequeued from a single transaction group only, subject to the array_size limit. In MULTI_GROUP navigation, messages are dequeued across multiple transaction groups, still subject to the array_size limit. ORA-25235 is returned to indicate the end of a transaction group. DEQUEUE_ARRAY is not supported for buffered messages, but you can still use this procedure on individual buffered messages by setting array_size to one message. See Also: ENQUEUE_OPTIONS_T Type