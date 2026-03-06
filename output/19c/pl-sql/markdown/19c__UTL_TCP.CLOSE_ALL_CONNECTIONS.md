---
id: 19c__UTL_TCP.CLOSE_ALL_CONNECTIONS
name: UTL_TCP.CLOSE_ALL_CONNECTIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.CLOSE_ALL_CONNECTIONS

This procedure closes all open TCP/IP connections.

## Syntax

```sql
UTL_TCP.CLOSE_ALL_CONNECTIONS;
```

## Usage Notes

Syntax UTL_TCP.CLOSE_ALL_CONNECTIONS; Usage Notes This call is provided to close all connections before a PL/SQL program ends to avoid dangling connections.