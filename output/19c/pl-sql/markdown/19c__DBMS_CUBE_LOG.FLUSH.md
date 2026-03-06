---
id: 19c__DBMS_CUBE_LOG.FLUSH
name: DBMS_CUBE_LOG.FLUSH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.FLUSH

This procedure forces all buffered messages to be written to the logs.

## Syntax

```sql
DBMS_CUBE_LOG.FLUSH ( );
```

## Usage Notes

The buffers are flushed automatically throughout a session, but manually flushing them before viewing the logs assures that you can view all of the messages. Syntax DBMS_CUBE_LOG.FLUSH ( ); Example The following example flushes the buffers for all of the logs: EXECUTE dbms_cube_log.flush;