---
id: 19c__UTL_TCP.FLUSH
name: UTL_TCP.FLUSH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.FLUSH

This procedure transfers immediately to the server all data in the output buffer, if a buffer is used.

## Syntax

```sql
UTL_TCP.FLUSH (
   c IN OUT NOCOPY connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to which to send data |

## Usage Notes

Syntax UTL_TCP.FLUSH ( c IN OUT NOCOPY connection); Parameters Table 277-6 FLUSH Procedure Parameters Parameter Description c TCP connection to which to send data Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION .