---
id: 19c__UTL_TCP.WRITE_LINE
name: UTL_TCP.WRITE_LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.WRITE_LINE

This function transmits a text line to a service on an open connection. The newline character sequence is appended to the message before it is transmitted.

## Syntax

```sql
UTL_TCP.WRITE_LINE (
   c    IN OUT NOCOPY connection,
   data IN            VARCHAR2 DEFAULT NULL CHARACTER SET ANY_CS) 
  RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to which to send data |
| data | VARCHAR2 | IN | Buffer containing the data to be sent |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_TCP.WRITE_LINE ( c IN OUT NOCOPY connection, data IN VARCHAR2 DEFAULT NULL CHARACTER SET ANY_CS) RETURN PLS_INTEGER; Parameters Table 277-17 WRITE_LINE Function Parameters Parameter Description c TCP connection to which to send data data Buffer containing the data to be sent Return Values The actual number of characters of data transmitted Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . Text messages are converted to the on-the-wire character set, specified when the connection was opened, before they are transmitted on the wire.