---
id: 19c__DBMS_AQADM.VERIFY_QUEUE_TYPES
name: DBMS_AQADM.VERIFY_QUEUE_TYPES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.VERIFY_QUEUE_TYPES

This procedure verifies that the source and destination queues have identical types.

## Syntax

```sql
DBMS_AQADM.VERIFY_QUEUE_TYPES (
   src_queue_name    IN    VARCHAR2,
   dest_queue_name   IN    VARCHAR2,
   destination       IN    VARCHAR2 DEFAULT NULL,
   rc                OUT   BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| src_queue_name | VARCHAR2 | IN | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| dest_queue_name | VARCHAR2 | IN | Name of the destination queue where messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| destination | VARCHAR2 | IN | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. |
| rc | BINARY_INTEGER) | OUT | Return code for the result of the procedure. If there is no error, and if the source and destination queue types match, then the result is 1. If they do not match, then the result is 0. If an Oracle error is encountered, then it is returned in rc . |

## Usage Notes

The result of the verification is stored in the table sys . aq$_message_types , overwriting all previous output of this command. Syntax DBMS_AQADM.VERIFY_QUEUE_TYPES ( src_queue_name IN VARCHAR2, dest_queue_name IN VARCHAR2, destination IN VARCHAR2 DEFAULT NULL, rc OUT BINARY_INTEGER); Parameters Table 23-62 VERIFY_QUEUE_TYPES Procedure Parameters Parameter Description src_queue_name Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. dest_queue_name Name of the destination queue where messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. destination Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. rc Return code for the result of the procedure. If there is no error, and if the source and destination queue types match, then the result is 1. If they do not match, then the result is 0. If an Oracle error is encountered, then it is returned in rc . Note: SYS.AQ$_MESSAGE_TYPES can have multiple entries for the same source queue, destination queue, and database link, but with different transformations. VERIFY_QUEUE_TYPES check happens once per AQ propagation schedule and not for every propagated message send. In case the payload of the queue is modified then the existing propagation schedule between source and destination queue needs to be dropped and recreated. Note: SYS.AQ$_MESSAGE_TYPES can have multiple entries for the same source queue, destination queue, and database link, but with different transformations. VERIFY_QUEUE_TYPES check happens once per AQ propagation schedule and not for every propagated message send. In case the payload of the queue is modified then the existing propagation schedule between source and destination queue needs to be dropped and recreated.