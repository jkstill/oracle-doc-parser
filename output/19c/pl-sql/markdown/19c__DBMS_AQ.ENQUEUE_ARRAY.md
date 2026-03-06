---
id: 19c__DBMS_AQ.ENQUEUE_ARRAY
name: DBMS_AQ.ENQUEUE_ARRAY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.ENQUEUE_ARRAY

This function enqueues an array of payloads using a corresponding array of message properties. The output will be an array of message IDs of the enqueued messages.

## Syntax

```sql
DBMS_AQ.ENQUEUE_ARRAY (
   queue_name                IN   VARCHAR2,
   enqueue_options           IN   enqueue_options_t,
   array_size                IN   pls_integer,
   message_properties_array  IN   message_properties_array_t,
   payload_array             IN   "<COLLECTION_1>",
   msgid_array               OUT  msgid_array_t,
   error_array               OUT  error_array_t)
RETURN pls_integer;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | The queue name in which messages are enqueued (same as single-row enqueue). |
| enqueue_options | enqueue_options_t | IN | See ENQUEUE_OPTIONS_T Type . |
| array_size | pls_integer | IN | The number of elements to enqueue. For buffered messages, array_size should be 1 . |
| message_properties_array | message_properties_array_t | IN | A record containing an array corresponding to each message property. For each property, the user must allocate array_size elements. See MESSAGE_PROPERTIES_ARRAY_T Type . |
| payload_array | IN | IN | An array of payload data. "< COLLECTION_1 >" can be an associative array, VARRAY , or nested table in its PL/SQL representation. Users can enqueue RAW and ADT payloads. |
| msgid_array | msgid_array_t | OUT | An array of message IDs for the enqueued messages. If an error occurs for a particular message, then its corresponding message ID is null. See MSGID_ARRAY_T Type . |
| error_array | error_array_t) | OUT | Currently not implemented |

**Returns:** `pls_integer`

## Usage Notes

Syntax DBMS_AQ.ENQUEUE_ARRAY ( queue_name IN VARCHAR2, enqueue_options IN enqueue_options_t, array_size IN pls_integer, message_properties_array IN message_properties_array_t, payload_array IN "<COLLECTION_1>", msgid_array OUT msgid_array_t, error_array OUT error_array_t) RETURN pls_integer; Parameters Table 22-10 ENQUEUE_ARRAY Function Parameters Parameter Description queue_name The queue name in which messages are enqueued (same as single-row enqueue). enqueue_options See ENQUEUE_OPTIONS_T Type . array_size The number of elements to enqueue. For buffered messages, array_size should be 1 . message_properties_array A record containing an array corresponding to each message property. For each property, the user must allocate array_size elements. See MESSAGE_PROPERTIES_ARRAY_T Type . payload_array An array of payload data. "< COLLECTION_1 >" can be an associative array, VARRAY , or nested table in its PL/SQL representation. Users can enqueue RAW and ADT payloads. msgid_array An array of message IDs for the enqueued messages. If an error occurs for a particular message, then its corresponding message ID is null. See MSGID_ARRAY_T Type . error_array Currently not implemented Usage Notes ENQUEUE_ARRAY is not supported for buffered messages, but you can still use this procedure on individual buffered messages by setting array_size to one message.