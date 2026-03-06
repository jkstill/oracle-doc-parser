---
id: 19c__UTL_COMPRESS.LZ_COMPRESS_OPEN
name: UTL_COMPRESS.LZ_COMPRESS_OPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_COMPRESS_OPEN

This function initializes a piecewise context that maintains the compress state and data.

## Syntax

```sql
UTL_COMPRESS.LZ_COMPRESS_OPEN (
   dst       IN OUT NOCOPY BLOB, 
   quality   IN            BINARY_INTEGER DEFAULT 6) 
 RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dst | NOCOPY | IN OUT | User supplied LOB to store compressed data. |
| quality | BINARY_INTEGER | IN | Speed versus efficiency of resulting compressed output. Valid values are the range 1..9, with a default value of 6. 1=fastest compression, 9=slowest compression and best compressed file size. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax UTL_COMPRESS.LZ_COMPRESS_OPEN ( dst IN OUT NOCOPY BLOB, quality IN BINARY_INTEGER DEFAULT 6) RETURN BINARY_INTEGER; Parameters Table 261-7 LZ_COMPRESS_OPEN Function Parameters Parameter Description dst User supplied LOB to store compressed data. quality Speed versus efficiency of resulting compressed output. Valid values are the range 1..9, with a default value of 6. 1=fastest compression, 9=slowest compression and best compressed file size. Return Values A handle to an initialized piecewise compress context. Exceptions invalid_handle - invalid handle, too many open handles. invalid_argument - NULL dst or invalid quality specified. Usage Notes Close the opened handle with LZ_COMPRESS_CLOSE once the piecewise compress is completed in the event of an exception in the middle of process because lack of doing so will cause these handles to leak.