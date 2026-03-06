---
id: 19c__UTL_TCP.WRITE_RAW
name: UTL_TCP.WRITE_RAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.WRITE_RAW

This function transmits a binary message to a service on an open connection. The function does not return until the specified number of bytes have been written.

## Syntax

```sql
UTL_TCP.WRITE_RAW (
   c    IN OUT NOCOPY connection,
   data IN            RAW,
   len  IN            PLS_INTEGER DEFAULT NULL) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to which to send data |
| data | RAW | IN | Buffer containing the data to be sent |
| len | PLS_INTEGER | IN | The number of bytes of data to transmit. When len is NULL , the whole length of data is written. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_TCP.WRITE_RAW ( c IN OUT NOCOPY connection, data IN RAW, len IN PLS_INTEGER DEFAULT NULL) RETURN PLS_INTEGER; Parameters Table 277-18 WRITE_RAW Function Parameters Parameter Description c TCP connection to which to send data data Buffer containing the data to be sent len The number of bytes of data to transmit. When len is NULL , the whole length of data is written. Return Values The number of bytes of data transmitted Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION.