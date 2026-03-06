---
id: 19c__DBMS_PIPE.SEND_MESSAGE
name: DBMS_PIPE.SEND_MESSAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.SEND_MESSAGE

This function sends a message on the named pipe.

## Syntax

```sql
DBMS_PIPE.SEND_MESSAGE (
    pipename     IN VARCHAR2,
    timeout      IN INTEGER DEFAULT MAXWAIT,
    maxpipesize  IN INTEGER DEFAULT 8192)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pipename | VARCHAR2 | IN | Name of the pipe on which you want to place the message. If you are using an explicit pipe, then this is the name that you specified when you called CREATE_PIPE . Caution: Do not use pipe names beginning with ' ORA$ '. These names are reserved for use by procedures provided by Oracle. Pipename should not be longer than 128 bytes, and is case-insensitive. At this time, the name cannot contain Globalization Support characters. |
| timeout | INTEGER | IN | Time to wait while attempting to place a message on a pipe, in seconds. The default value is the constant MAXWAIT , which is defined as 86400000 (1000 days). |
| maxpipesize | INTEGER | IN | Maximum size allowed for the pipe, in bytes. The total size of all the messages on the pipe cannot exceed this amount. The message is blocked if it exceeds this maximum. The default is 8192 bytes. The maxpipesize for a pipe becomes a part of the characteristics of the pipe and persists for the life of the pipe. Callers of SEND_MESSAGE with larger values cause the maxpipesize to be increased. Callers with a smaller value simply use the existing, larger value. Specifying maxpipesize as part of the SEND_MESSAGE procedure eliminates the need for a separate call to open the pipe. If you created the pipe explicitly, then you can use the optional maxpipesize parameter to override the creation pipe size specifications. |

**Returns:** `INTEGER`

## Usage Notes

The message is contained in the local message buffer, which was filled with calls to PACK_MESSAGE . You can create a pipe explicitly using CREATE_PIPE , otherwise, it is created implicitly. Syntax DBMS_PIPE.SEND_MESSAGE ( pipename IN VARCHAR2, timeout IN INTEGER DEFAULT MAXWAIT, maxpipesize IN INTEGER DEFAULT 8192) RETURN INTEGER; Pragmas pragma restrict_references(send_message,WNDS,RNDS); Parameters Table 127-15 SEND_MESSAGE Function Parameters Parameter Description pipename Name of the pipe on which you want to place the message. If you are using an explicit pipe, then this is the name that you specified when you called CREATE_PIPE . Caution: Do not use pipe names beginning with ' ORA$ '. These names are reserved for use by procedures provided by Oracle. Pipename should not be longer than 128 bytes, and is case-insensitive. At this time, the name cannot contain Globalization Support characters. timeout Time to wait while attempting to place a message on a pipe, in seconds. The default value is the constant MAXWAIT , which is defined as 86400000 (1000 days). maxpipesize Maximum size allowed for the pipe, in bytes. The total size of all the messages on the pipe cannot exceed this amount. The message is blocked if it exceeds this maximum. The default is 8192 bytes. The maxpipesize for a pipe becomes a part of the characteristics of the pipe and persists for the life of the pipe. Callers of SEND_MESSAGE with larger values cause the maxpipesize to be increased. Callers with a smaller value simply use the existing, larger value. Specifying maxpipesize as part of the SEND_MESSAGE procedure eliminates the need for a separate call to open the pipe. If you created the pipe explicitly, then you can use the optional maxpipesize parameter to override the creation pipe size specifications. Return Values Table 127-16 SEND_MESSAGE Function Return Values Return Description 0 Success. If the pipe already exists and the user attempting to create it is authorized to use it, then Oracle returns 0, indicating success, and any data already in the pipe remains. If a user connected as SYSDBS / SYSOPER re-creates a pipe, then Oracle returns status 0, but the ownership of the pipe remains unchanged. 1 Timed out. This procedure can timeout either because it cannot get a lock on the pipe, or because the pipe remains too full to be used. If the pipe was implicitly-created and is empty, then it is removed. 3 An interrupt occurred. If the pipe was implicitly created and is empty, then it is removed. ORA-23322 Insufficient privileges. If a pipe with the same name exists and was created by a different user, then Oracle signals error ORA-23322 , indicating the naming conflict.