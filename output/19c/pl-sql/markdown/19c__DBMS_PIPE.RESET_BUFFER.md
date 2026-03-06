---
id: 19c__DBMS_PIPE.RESET_BUFFER
name: DBMS_PIPE.RESET_BUFFER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PIPE
tags: [dbms_pipe]
source_file: DBMS_PIPE.html
---

# DBMS_PIPE.RESET_BUFFER

This procedure resets the PACK_MESSAGE and UNPACK_MESSAGE positioning indicators to 0.

## Syntax

```sql
DBMS_PIPE.RESET_BUFFER;
```

## Usage Notes

Because all pipes share a single buffer, you may find it useful to reset the buffer before using a new pipe. This ensures that the first time you attempt to send a message to your pipe, you do not inadvertently send an expired message remaining in the buffer. Syntax DBMS_PIPE.RESET_BUFFER; Pragmas pragma restrict_references(reset_buffer,WNDS,RNDS);