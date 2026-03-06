---
id: 19c__DBMS_APPLY_ADM.GET_ERROR_MESSAGE
name: DBMS_APPLY_ADM.GET_ERROR_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.GET_ERROR_MESSAGE

This function returns the message payload from the error queue for the specified message number and transaction identifier. The message can be a logical change record (LCR) or a non-LCR message.

## Syntax

```sql
DBMS_APPLY_ADM.GET_ERROR_MESSAGE(
   message_number          IN   NUMBER, 
   local_transaction_id    IN   VARCHAR2,
   destination_queue_name  OUT  VARCHAR2, 
   execute                 OUT  BOOLEAN)
RETURN ANYDATA;

DBMS_APPLY_ADM.GET_ERROR_MESSAGE(
   message_number          IN   NUMBER, 
   local_transaction_id    IN   VARCHAR2)
RETURN ANYDATA;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| message_number | NUMBER | IN | The identification number of the message. This number identifies the position of the message in the transaction. Query the DBA_APPLY_ERROR data dictionary view to view the message number of each apply error. |
| local_transaction_id | VARCHAR2 | IN | Identifier of the error transaction for which to return a message |
| destination_queue_name | VARCHAR2 | OUT | Contains the name of the queue into which the message should be enqueued. If the message should not be enqueued into a queue, then this parameter contains NULL . |
| execute | BOOLEAN) | OUT | Contains TRUE if the message should be executed Contains FALSE if the message should not be executed |

**Returns:** `ANYDATA`

## Usage Notes

This function is overloaded. One version of this function contains two OUT parameters. These OUT parameters contain the destination queue into which the message should be enqueued, if one exists, and whether the message should be executed. The destination queue is specified using the SET_ENQUEUE_DESTINATION procedure, and the execution directive is specified using the SET_EXECUTE procedure. See Also: SET_ENQUEUE_DESTINATION Procedure SET_EXECUTE Procedure See Also: SET_ENQUEUE_DESTINATION Procedure SET_EXECUTE Procedure Syntax DBMS_APPLY_ADM.GET_ERROR_MESSAGE( message_number IN NUMBER, local_transaction_id IN VARCHAR2, destination_queue_name OUT VARCHAR2, execute OUT BOOLEAN) RETURN ANYDATA; DBMS_APPLY_ADM.GET_ERROR_MESSAGE( message_number IN NUMBER, local_transaction_id IN VARCHAR2) RETURN ANYDATA; Parameters Table 21-13 GET_ERROR_MESSAGE Function Parameters Parameter Description message_number The identification number of the message. This number identifies the position of the message in the transaction. Query the DBA_APPLY_ERROR data dictionary view to view the message number of each apply error. local_transaction_id Identifier of the error transaction for which to return a message destination_queue_name Contains the name of the queue into which the message should be enqueued. If the message should not be enqueued into a queue, then this parameter contains NULL . execute Contains TRUE if the message should be executed Contains FALSE if the message should not be executed Usage Notes The following usage notes apply to this procedure: The GET_ERROR_MESSAGE Procedure and XStream Outbound Servers The GET_ERROR_MESSAGE Procedure and XStream Inbound Servers The GET_ERROR_MESSAGE Procedure and XStream Outbound Servers Outbound servers do not enqueue error transactions into an error queue. This procedure cannot be used with XStream outbound servers. The GET_ERROR_MESSAGE Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.