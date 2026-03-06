---
id: 19c__DBMS_PIPE.CREATE_PIPE
name: DBMS_PIPE.CREATE_PIPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.CREATE_PIPE

This function explicitly creates a public or private pipe. If the private flag is TRUE , then the pipe creator is assigned as the owner of the private pipe.

## Syntax

```sql
DBMS_PIPE.CREATE_PIPE (
   pipename     IN VARCHAR2,
   maxpipesize  IN INTEGER DEFAULT 8192,
   private      IN BOOLEAN DEFAULT TRUE)
RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pipename | VARCHAR2 | IN | Name of the pipe you are creating. You must use this name when you call SEND_MESSAGE and RECEIVE_MESSAGE . This name must be unique across the instance. Caution: Do not use pipe names beginning with ORA$ . These are reserved for use by procedures provided by Oracle. Pipename should not be longer than 128 bytes, and is case insensitive. At this time, the name cannot contain Globalization Support characters. |
| maxpipesize | INTEGER | IN | The maximum size allowed for the pipe, in bytes. The total size of all of the messages on the pipe cannot exceed this amount. The message is blocked if it exceeds this maximum. The default maxpipesize is 8192 bytes. The maxpipesize for a pipe becomes a part of the characteristics of the pipe and persists for the life of the pipe. Callers of SEND_MESSAGE with larger values cause the maxpipesize to be increased. Callers with a smaller value use the existing, larger value. |
| private | BOOLEAN | IN | Uses the default, TRUE , to create a private pipe. Public pipes can be implicitly created when you call SEND_MESSAGE . |

**Returns:** `INTEGER`

## Usage Notes

Explicitly-created pipes can only be removed by calling REMOVE_PIPE , or by shutting down the instance. Syntax DBMS_PIPE.CREATE_PIPE ( pipename IN VARCHAR2, maxpipesize IN INTEGER DEFAULT 8192, private IN BOOLEAN DEFAULT TRUE) RETURN INTEGER; Pragmas pragma restrict_references(create_pipe,WNDS,RNDS); Parameters Table 127-3 CREATE_PIPE Function Parameters Parameter Description pipename Name of the pipe you are creating. You must use this name when you call SEND_MESSAGE and RECEIVE_MESSAGE . This name must be unique across the instance. Caution: Do not use pipe names beginning with ORA$ . These are reserved for use by procedures provided by Oracle. Pipename should not be longer than 128 bytes, and is case insensitive. At this time, the name cannot contain Globalization Support characters. maxpipesize The maximum size allowed for the pipe, in bytes. The total size of all of the messages on the pipe cannot exceed this amount. The message is blocked if it exceeds this maximum. The default maxpipesize is 8192 bytes. The maxpipesize for a pipe becomes a part of the characteristics of the pipe and persists for the life of the pipe. Callers of SEND_MESSAGE with larger values cause the maxpipesize to be increased. Callers with a smaller value use the existing, larger value. private Uses the default, TRUE , to create a private pipe. Public pipes can be implicitly created when you call SEND_MESSAGE . Return Values Table 127-4 CREATE_PIPE Function Return Values Return Description 0 Successful. If the pipe already exists and the user attempting to create it is authorized to use it, then Oracle returns 0, indicating success, and any data already in the pipe remains. If a user connected as SYSDBA / SYSOPER re-creates a pipe, then Oracle returns status 0, but the ownership of the pipe remains unchanged. ORA-23322 Failure due to naming conflict. If a pipe with the same name exists and was created by a different user, then Oracle signals error ORA-23322 , indicating the naming conflict.