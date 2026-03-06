---
id: 19c__DBMS_PIPE.REMOVE_PIPE
name: DBMS_PIPE.REMOVE_PIPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.REMOVE_PIPE

This function removes explicitly-created pipes.

## Syntax

```sql
DBMS_PIPE.REMOVE_PIPE (
   pipename  IN  VARCHAR2)
RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pipename | VARCHAR2) | IN | Name of pipe that you want to remove. |

**Returns:** `INTEGER`

## Usage Notes

Pipes created implicitly by SEND_MESSAGE are automatically removed when empty. However, pipes created explicitly by CREATE_PIPE are removed only by calling REMOVE_PIPE , or by shutting down the instance. All unconsumed records in the pipe are removed before the pipe is deleted. This is similar to calling PURGE on an implicitly-created pipe. Syntax DBMS_PIPE.REMOVE_PIPE ( pipename IN VARCHAR2) RETURN INTEGER; Pragmas pragma restrict_references(remove_pipe,WNDS,RNDS); Parameters Table 127-12 REMOVE_PIPE Function Parameters Parameter Description pipename Name of pipe that you want to remove. Return Values Table 127-13 REMOVE_PIPE Function Return Values Return Description 0 Success If the pipe does not exist, or if the pipe already exists and the user attempting to remove it is authorized to do so, then Oracle returns 0, indicating success, and any data remaining in the pipe is removed. ORA-23322 Insufficient privileges. If the pipe exists, but the user is not authorized to access the pipe, then Oracle signals error ORA-23322 , indicating insufficient privileges.