---
id: 19c__UTL_TCP.GET_LINE
name: UTL_TCP.GET_LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.GET_LINE

This function returns the line of data read.

## Syntax

```sql
UTL_TCP.GET_LINE (
   c           IN OUT NOCOPY connection,
   remove_crlf IN            BOOLEAN DEFAULT FALSE,
   peek        IN            BOOLEAN DEFAULT FALSE) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |
| remove_crlf | BOOLEAN | IN | If TRUE , then one ore more trailing CRLF characters are removed from the received message. |
| peek | BOOLEAN | IN | Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_TCP.GET_LINE ( c IN OUT NOCOPY connection, remove_crlf IN BOOLEAN DEFAULT FALSE, peek IN BOOLEAN DEFAULT FALSE) RETURN VARCHAR2; Parameters Table 277-7 GET_LINE Function Parameters Parameter Description c TCP connection from which to receive data remove_crlf If TRUE , then one ore more trailing CRLF characters are removed from the received message. peek Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. Return Values The text line read Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . See READ_LINE for the read time out, character set conversion, buffer size, and multibyte character issues.