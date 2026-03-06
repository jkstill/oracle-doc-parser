---
id: 19c__UTL_TCP.READ_LINE
name: UTL_TCP.READ_LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.READ_LINE

This function receives a text line from a service on an open connection.

## Syntax

```sql
UTL_TCP.READ_LINE (
   c           IN OUT NOCOPY connection,
   data        IN OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS,
   peek        IN            BOOLEAN DEFAULT FALSE) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |
| data | NOCOPY | IN OUT | Data received. |
| remove_crlf |  |  | If TRUE , then one ore more trailing CRLF characters are removed from the received message. |
| peek | BOOLEAN | IN | Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. |

**Returns:** `PLS_INTEGER`

## Usage Notes

A line is terminated by a line-feed, a carriage-return or a carriage-return followed by a line-feed. Syntax UTL_TCP.READ_LINE ( c IN OUT NOCOPY connection, data IN OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS, peek IN BOOLEAN DEFAULT FALSE) RETURN PLS_INTEGER; Parameters Table 277-13 READ_LINE Function Parameters Parameter Description c TCP connection from which to receive data data Data received. remove_crlf If TRUE , then one ore more trailing CRLF characters are removed from the received message. peek Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. Return Values The number of characters of data received Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION. This function does not return until the end-of-line have been reached, or the end of input has been reached. Text messages is converted from the on-the-wire character set, specified when the connection was opened, to the database character set before they are returned to the caller. If transfer time out is set when the connection is opened, then this function waits for each data packet to be ready to read until time out occurs. If it occurs, then this function stops reading and returns all the data read successfully. If no data is read successfully, then the transfer_timeout exception is raised. The exception can be handled and the read operation can be retried later. If a partial multibyte character is found at the end of input, then this function stops reading and returns all the complete multibyte characters read successfully. If no complete character is read successfully, then the partial_multibyte_char exception is raised. The exception can be handled and the bytes of that partial multibyte character can be read as binary by the READ_RAW function. If a partial multibyte character is seen in the middle of the input because the remaining bytes of the character have not arrived and read time out occurs, then the transfer_timeout exception is raised instead. The exception can be handled and the read operation can be retried later.