---
id: 19c__UTL_TCP.AVAILABLE
name: UTL_TCP.AVAILABLE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_TCP
tags: [utl_tcp]
source_file: UTL_TCP.html
---

# UTL_TCP.AVAILABLE

This function determines the number of bytes available for reading from a TCP/IP connection. It is the number of bytes that can be read immediately without blocking. Determines if data is ready to be read from the connection.

## Syntax

```sql
UTL_TCP.AVAILABLE (
   c        IN OUT NOCOPY connection, 
   timeout  IN PLS_INTEGER DEFAULT 0)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | NOCOPY | IN OUT | TCP connection to determine the amount of data that is available to be read |
| timeout | PLS_INTEGER | IN | Time in seconds to wait before giving up and reporting that no data is available. Zero (0) indicates not to wait at all. NULL indicates to wait forever. |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_TCP.AVAILABLE ( c IN OUT NOCOPY connection, timeout IN PLS_INTEGER DEFAULT 0) RETURN PLS_INTEGER; Parameters Table 277-4 AVAILABLE Function Parameters Parameter Description c TCP connection to determine the amount of data that is available to be read timeout Time in seconds to wait before giving up and reporting that no data is available. Zero (0) indicates not to wait at all. NULL indicates to wait forever. Return Values The number of bytes available for reading without blocking Usage Notes The connection must have already been opened through a call to OPEN_CONNECTION . Users may use this API to determine if data is available to be read before calling the read API so that the program are not blocked because data is not ready to be read from the input. The number of bytes available for reading returned by this function may be less than what is actually available. On some platforms, this function may only return 1, to indicate that some data is available. If you are concerned about the portability of your application, then assume that this function returns a positive value when data is available for reading, and 0 when no data is available. This function returns a positive value when all the data at a particular connection has been read and the next read result in the END_OF_INPUT exception. The following example illustrates using this function in a portable manner: DECLARE c utl_tcp.connection data VARCHAR2(256); len PLS_INTEGER; BEGIN c := utl_tcp.open_connection(...); LOOP IF (utl_tcp.available(c) > 0) THEN len := utl_tcp.read_text(c, data, 256); ELSE ---do some other things . . . . END IF END LOOP; END;