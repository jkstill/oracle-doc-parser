---
id: 19c__UTL_TCP.GET_RAW
name: UTL_TCP.GET_RAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.GET_RAW

This function returns the data read instead of the amount of data read.

## Syntax

```sql
UTL_TCP.GET_RAW (
   c     IN OUT NOCOPY connection,
   len   IN            PLS_INTEGER DEFAULT 1,
   peek  IN            BOOLEAN     DEFAULT FALSE) 
 RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |
| len | PLS_INTEGER | IN | The number of bytes (or characters for VARCHAR2 ) of data to receive. Default is 1. |
| peek | BOOLEAN | IN | Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. |
| remove_crlf |  |  | If TRUE , then one ore more trailing CRLF characters are removed from the received message. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_TCP.GET_RAW ( c IN OUT NOCOPY connection, len IN PLS_INTEGER DEFAULT 1, peek IN BOOLEAN DEFAULT FALSE) RETURN RAW; Parameters Table 277-9 GET_RAW Function Parameters Parameter Description c TCP connection from which to receive data len The number of bytes (or characters for VARCHAR2 ) of data to receive. Default is 1. peek Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. remove_crlf If TRUE , then one ore more trailing CRLF characters are removed from the received message. Return Values The binary data read Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . For all the get_* APIs described in this section, see the corresponding READ_* API for the read time out issue. For GET_TEXT and GET_LINE , see the corresponding READ_* API for character set conversion, buffer size, and multibyte character issues.