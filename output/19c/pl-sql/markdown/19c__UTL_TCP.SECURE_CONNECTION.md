---
id: 19c__UTL_TCP.SECURE_CONNECTION
name: UTL_TCP.SECURE_CONNECTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.SECURE_CONNECTION

This procedure secures a TCP/IP connection using SSL/TLS.

## Syntax

```sql
UTL_TCP.SECURE_CONNECTION (
   c    IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |

## Usage Notes

SSL/TLS requires an Oracle wallet which must be specified when the connection was opened by the OPEN_CONNECTION Function . Syntax UTL_TCP.SECURE_CONNECTION ( c IN OUT NOCOPY connection); Parameters Table 277-16 SECURE_CONNECTION Procedure Parameters Parameter Description c TCP connection from which to receive data