---
id: 19c__UTL_TCP.CLOSE_CONNECTION
name: UTL_TCP.CLOSE_CONNECTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.CLOSE_CONNECTION

This procedure closes an open TCP/IP connection.

## Syntax

```sql
UTL_TCP.CLOSE_CONNECTION (
   c IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to close |

## Usage Notes

Syntax UTL_TCP.CLOSE_CONNECTION ( c IN OUT NOCOPY connection); Parameters Table 277-5 CLOSE_CONNECTION Procedure Parameters Parameter Description c TCP connection to close Usage Notes Connection must have been opened by a previous call to OPEN_CONNECTION . The fields remote_host, remote_port, local_host, local_port and charset of c are reset after the connection is closed. An open connection must be closed explicitly. An open connection remains open when the PL/SQL record variable that stores the connection goes out-of-scope in the PL/SQL program. Failing to close unwanted connections may result in unnecessary tying up of local and remote system resources.