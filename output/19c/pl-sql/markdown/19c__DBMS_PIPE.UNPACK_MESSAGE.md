---
id: 19c__DBMS_PIPE.UNPACK_MESSAGE
name: DBMS_PIPE.UNPACK_MESSAGE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.UNPACK_MESSAGE

This procedure retrieves items from the buffer.

## Syntax

```sql
DBMS_PIPE.UNPACK_MESSAGE (
   item  OUT VARCHAR2);

DBMS_PIPE.UNPACK_MESSAGE (
   item  OUT NCHAR);

DBMS_PIPE.UNPACK_MESSAGE (
   item  OUT NUMBER);

DBMS_PIPE.UNPACK_MESSAGE (
   item  OUT DATE);

DBMS_PIPE.UNPACK_MESSAGE_RAW (
   item  OUT RAW);

DBMS_PIPE.UNPACK_MESSAGE_ROWID (
   item  OUT ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| item | VARCHAR2) | OUT | Argument to receive the next unpacked item from the local message buffer. |

## Usage Notes

After you have called RECEIVE_MESSAGE to place pipe information in a local buffer, call UNPACK_MESSAGE . Note: The UNPACK_MESSAGE procedure is overloaded to return items of type VARCHAR2 , NCHAR , NUMBER , or DATE . There are two additional procedures to unpack RAW and ROWID items. Note: The UNPACK_MESSAGE procedure is overloaded to return items of type VARCHAR2 , NCHAR , NUMBER , or DATE . There are two additional procedures to unpack RAW and ROWID items. Syntax DBMS_PIPE.UNPACK_MESSAGE ( item OUT VARCHAR2); DBMS_PIPE.UNPACK_MESSAGE ( item OUT NCHAR); DBMS_PIPE.UNPACK_MESSAGE ( item OUT NUMBER); DBMS_PIPE.UNPACK_MESSAGE ( item OUT DATE); DBMS_PIPE.UNPACK_MESSAGE_RAW ( item OUT RAW); DBMS_PIPE.UNPACK_MESSAGE_ROWID ( item OUT ROWID); Pragmas pragma restrict_references(unpack_message,WNDS,RNDS); pragma restrict_references(unpack_message_raw,WNDS,RNDS); pragma restrict_references(unpack_message_rowid,WNDS,RNDS); Parameters Table 127-18 UNPACK_MESSAGE Procedure Parameters Parameter Description item Argument to receive the next unpacked item from the local message buffer.