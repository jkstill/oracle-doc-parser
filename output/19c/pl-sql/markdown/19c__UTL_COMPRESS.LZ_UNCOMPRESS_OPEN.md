---
id: 19c__UTL_COMPRESS.LZ_UNCOMPRESS_OPEN
name: UTL_COMPRESS.LZ_UNCOMPRESS_OPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_UNCOMPRESS_OPEN

This function initializes a piecewise context that maintains the uncompress state and data.

## Syntax

```sql
UTL_COMPRESS.LZ_UNCOMPRESS_OPEN(
   src  IN  BLOB)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| src | BLOB) | IN | The input data to be uncompressed. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax UTL_COMPRESS.LZ_UNCOMPRESS_OPEN( src IN BLOB) RETURN BINARY_INTEGER; Parameters Table 261-10 LZ_UNCOMPRESS_OPEN Function Parameters Parameter Description src The input data to be uncompressed. Return Values A handle to an initialized piecewise compress context. Exceptions invalid_handle - invalid handle, too many open handles. invalid_argument - NULL src . Usage Notes Close the opened handle with LZ_UNCOMPRESS_CLOSE once the piecewise uncompress is completed in the event of an exception in the middle of process because lack of doing so will cause these handles to leak.