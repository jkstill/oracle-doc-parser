---
id: 19c__UTL_TCP.READ_RAW
name: UTL_TCP.READ_RAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.READ_RAW

This function receives binary data from a service on an open connection.

## Syntax

```sql
UTL_TCP.READ_RAW (
   c     IN OUT NOCOPY connection,
   data  IN OUT NOCOPY RAW,
   len   IN            PLS_INTEGER DEFAULT 1,
   peek  IN            BOOLEAN     DEFAULT FALSE)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection from which to receive data |
| data (IN OUT COPY) |  |  | Data received |
| len | PLS_INTEGER | IN | Number of bytes of data to receive |
| peek | BOOLEAN | IN | Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_TCP.READ_RAW ( c IN OUT NOCOPY connection, data IN OUT NOCOPY RAW, len IN PLS_INTEGER DEFAULT 1, peek IN BOOLEAN DEFAULT FALSE) RETURN PLS_INTEGER; Parameters Table 277-14 READ_RAW Function Parameters Parameter Description c TCP connection from which to receive data data (IN OUT COPY) Data received len Number of bytes of data to receive peek Normally, you want to read the data and remove it from the input queue, that is, consume it. In some situations, you may just want to look ahead at the data, that is, peek at it, without removing it from the input queue, so that it is still available for reading (or even peeking) in the next call. To keep the data in the input queue, set this flag to TRUE and set up an input buffer before the connection is opened. The amount of data you can peek at (that is, read but keep in the input queue) must be less than the size of input buffer. Return Values The number of bytes of data received Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . This function does not return until the specified number of bytes have been read, or the end of input has been reached. If transfer time out is set when the connection is opened, then this function waits for each data packet to be ready to read until time out occurs. If it occurs, then this function stops reading and returns all the data read successfully. If no data is read successfully, then the transfer_timeout exception is raised. The exception can be handled and the read operation can be retried later.