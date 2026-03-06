---
id: 19c__DBMS_PIPE.PACK_MESSAGE
name: DBMS_PIPE.PACK_MESSAGE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.PACK_MESSAGE

This procedure builds your message in the local message buffer.

## Syntax

```sql
DBMS_PIPE.PACK_MESSAGE (
   item  IN  VARCHAR2);

DBMS_PIPE.PACK_MESSAGE (
   item  IN  NCHAR);

DBMS_PIPE.PACK_MESSAGE (
   item  IN  NUMBER);

DBMS_PIPE.PACK_MESSAGE (
   item  IN  DATE);

DBMS_PIPE.PACK_MESSAGE_RAW (
   item  IN  RAW);

DBMS_PIPE.PACK_MESSAGE_ROWID (
   item  IN  ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| item | VARCHAR2) | IN | Item to pack into the local message buffer. |

## Usage Notes

To send a message, first make one or more calls to PACK_MESSAGE . Then, call SEND_MESSAGE to send the message in the local buffer on the named pipe. The procedure is overloaded to accept items of type VARCHAR2 , NCHAR , NUMBER , DATE ., RAW and ROWID items. In addition to the data bytes, each item in the buffer requires one byte to indicate its type, and two bytes to store its length. One additional byte is needed to terminate the message.The overhead for all types other than VARCHAR is 4 bytes. Syntax DBMS_PIPE.PACK_MESSAGE ( item IN VARCHAR2); DBMS_PIPE.PACK_MESSAGE ( item IN NCHAR); DBMS_PIPE.PACK_MESSAGE ( item IN NUMBER); DBMS_PIPE.PACK_MESSAGE ( item IN DATE); DBMS_PIPE.PACK_MESSAGE_RAW ( item IN RAW); DBMS_PIPE.PACK_MESSAGE_ROWID ( item IN ROWID); Pragmas pragma restrict_references(pack_message,WNDS,RNDS); pragma restrict_references(pack_message_raw,WNDS,RNDS); pragma restrict_references(pack_message_rowid,WNDS,RNDS); Parameters Table 127-7 PACK_MESSAGE Procedure Parameters Parameter Description item Item to pack into the local message buffer. Usage Notes In Oracle database version 8.x, the char-set-id (2 bytes) and the char-set-form (1 byte) are stored with each data item. Therefore, the overhead when using Oracle database version 8.x is 7 bytes. When you call SEND_MESSAGE to send this message, you must indicate the name of the pipe on which you want to send the message. If this pipe already exists, then you must have sufficient privileges to access this pipe. If the pipe does not already exist, then it is created automatically.