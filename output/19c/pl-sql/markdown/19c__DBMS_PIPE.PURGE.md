---
id: 19c__DBMS_PIPE.PURGE
name: DBMS_PIPE.PURGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.PURGE

This procedure empties the contents of the named pipe.

## Syntax

```sql
DBMS_PIPE.PURGE (
   pipename  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pipename | VARCHAR2) | IN | Name of pipe from which to remove all messages. The local buffer may be overwritten with messages as they are discarded. Pipename should not be longer than 128 bytes, and is case-insensitive. |

## Usage Notes

An empty implicitly-created pipe is aged out of the shared global area according to the least-recently-used algorithm. Thus, calling PURGE lets you free the memory associated with an implicitly-created pipe. Syntax DBMS_PIPE.PURGE ( pipename IN VARCHAR2); Pragmas pragma restrict_references(purge,WNDS,RNDS); Parameters Table 127-8 PURGE Procedure Parameters Parameter Description pipename Name of pipe from which to remove all messages. The local buffer may be overwritten with messages as they are discarded. Pipename should not be longer than 128 bytes, and is case-insensitive. Usage Notes Because PURGE calls RECEIVE_MESSAGE , the local buffer might be overwritten with messages as they are purged from the pipe. Also, you can receive an ORA-23322 (insufficient privileges) error if you attempt to purge a pipe with which you have insufficient access rights.