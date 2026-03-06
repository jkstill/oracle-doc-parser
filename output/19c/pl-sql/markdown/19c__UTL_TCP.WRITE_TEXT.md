---
id: 19c__UTL_TCP.WRITE_TEXT
name: UTL_TCP.WRITE_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.WRITE_TEXT

This function transmits a text message to a service on an open connection.

## Syntax

```sql
UTL_TCP.WRITE_TEXT (
   c    IN OUT NOCOPY connection,
   data IN            VARCHAR2 CHARACTER SET ANY_CS,
   len  IN            PLS_INTEGER DEFAULT NULL) 
 RETURN num_chars PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to which to send data |
| data | VARCHAR2 | IN | Buffer containing the data to be sent |
| len | PLS_INTEGER | IN | The number of characters of data to transmit. When len is NULL , the whole length of data is written. The actual amount of data written may be less because of network condition. |

**Returns:** `num_chars`

## Usage Notes

Syntax UTL_TCP.WRITE_TEXT ( c IN OUT NOCOPY connection, data IN VARCHAR2 CHARACTER SET ANY_CS, len IN PLS_INTEGER DEFAULT NULL) RETURN num_chars PLS_INTEGER; Parameters Table 277-19 WRITE_TEXT Function Parameters Parameter Description c TCP connection to which to send data data Buffer containing the data to be sent len The number of characters of data to transmit. When len is NULL , the whole length of data is written. The actual amount of data written may be less because of network condition. Return Values The actual number of characters of data transmitted Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION. Text messages are converted to the on-the-wire character set, specified when the connection was opened, before they are transmitted on the wire.