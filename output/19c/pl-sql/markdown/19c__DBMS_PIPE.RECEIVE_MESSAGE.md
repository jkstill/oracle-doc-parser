---
id: 19c__DBMS_PIPE.RECEIVE_MESSAGE
name: DBMS_PIPE.RECEIVE_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.RECEIVE_MESSAGE

This function copies the message into the local message buffer.

## Syntax

```sql
DBMS_PIPE.RECEIVE_MESSAGE (
   pipename     IN VARCHAR2,
   timeout      IN INTEGER      DEFAULT maxwait)
RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pipename | VARCHAR2 | IN | Name of the pipe on which you want to receive a message. Names beginning with ORA$ are reserved for use by Oracle |
| timeout | INTEGER | IN | Time to wait for a message, in seconds. The default value is the constant MAXWAIT , which is defined as 86400000 (1000 days). A timeout of 0 lets you read without blocking. |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_PIPE.RECEIVE_MESSAGE ( pipename IN VARCHAR2, timeout IN INTEGER DEFAULT maxwait) RETURN INTEGER; Pragmas pragma restrict_references(receive_message,WNDS,RNDS); Parameters Table 127-9 RECEIVE_MESSAGE Function Parameters Parameter Description pipename Name of the pipe on which you want to receive a message. Names beginning with ORA$ are reserved for use by Oracle timeout Time to wait for a message, in seconds. The default value is the constant MAXWAIT , which is defined as 86400000 (1000 days). A timeout of 0 lets you read without blocking. Return Values Table 127-10 RECEIVE_MESSAGE Function Return Values Return Description 0 Success 1 Timed out. If the pipe was implicitly-created and is empty, then it is removed. 2 Record in the pipe is too large for the buffer. (This should not happen.) 3 An interrupt occurred. ORA-23322 User has insufficient privileges to read from the pipe. Usage Notes To receive a message from a pipe, first call RECEIVE_MESSAGE . When you receive a message, it is removed from the pipe; hence, a message can only be received once. For implicitly-created pipes, the pipe is removed after the last record is removed from the pipe. If the pipe that you specify when you call RECEIVE_MESSAGE does not already exist, then Oracle implicitly creates the pipe and waits to receive the message. If the message does not arrive within a designated timeout interval, then the call returns and the pipe is removed. After receiving the message, you must make one or more calls to UNPACK_MESSAGE to access the individual items in the message. The UNPACK_MESSAGE procedure is overloaded to unpack items of type DATE , NUMBER , VARCHAR2 , and there are two additional procedures to unpack RAW and ROWID items. If you do not know the type of data that you are attempting to unpack, then call NEXT_ITEM_TYPE to determine the type of the next item in the buffer.