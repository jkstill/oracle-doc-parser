---
id: 19c__UTL_TCP.READ_TEXT
name: UTL_TCP.READ_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.READ_TEXT

This function receives text data from a service on an open connection.

## Syntax

```sql
UTL_TCP.READ_TEXT (
   c    IN OUT NOCOPY connection,
   data IN OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS,
   len  IN            PLS_INTEGER DEFAULT 1,
   peek IN            BOOLEAN     DEFAULT FALSE) 
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |
| data | NOCOPY | IN OUT | Data received |
| len | PLS_INTEGER | IN | Number of characters of data to receive |
| peek | BOOLEAN | IN | Normally, users want to read the data and remove it from the input queue, that is, consume it. In some situations, users may just want to look ahead at the data without removing it from the input queue so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and an input buffer must be set up when the connection is opened. The amount of data that you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_TCP.READ_TEXT ( c IN OUT NOCOPY connection, data IN OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS, len IN PLS_INTEGER DEFAULT 1, peek IN BOOLEAN DEFAULT FALSE) RETURN PLS_INTEGER; Parameters Table 277-15 READ_TEXT Function Parameters Parameter Description c TCP connection from which to receive data data Data received len Number of characters of data to receive peek Normally, users want to read the data and remove it from the input queue, that is, consume it. In some situations, users may just want to look ahead at the data without removing it from the input queue so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and an input buffer must be set up when the connection is opened. The amount of data that you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. Return Values The number of characters of data received Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . This function does not return until the specified number of characters has been read, or the end of input has been reached. Text messages is converted from the on-the-wire character set, specified when the connection was opened, to the database character set before they are returned to the caller. Unless explicitly overridden, the size of a VARCHAR2 buffer is specified in terms of bytes, while the parameter len refers to the maximum number of characters to be read. When the database character set is multibyte, where a single character may consist of more than 1 byte, you should ensure that the buffer can hold the maximum of characters. In general, the size of the VARCHAR2 buffer should equal the number of characters to be read, multiplied by the maximum number of bytes of a character of the database character set. If transfer time out is set when the connection is opened, then this function waits for each data packet to be ready to read until time out occurs. If it occurs, then this function stops reading and returns all the data read successfully. If no data is read successfully, then the transfer_timeout exception is raised. The exception can be handled and the read operation can be retried later. If a partial multibyte character is found at the end of input, then this function stops reading and returns all the complete multibyte characters read successfully. If no complete character is read successfully, then the partial_multibyte_char exception is raised. The exception can be handled and the bytes of that partial multibyte character can be read as binary by the READ_RAW function. If a partial multibyte character is seen in the middle of the input because the remaining bytes of the character have not arrived and read time out occurs, then the transfer_timeout exception is raised instead. The exception can be handled and the read operation can be retried later.