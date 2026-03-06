---
id: 19c__UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE
name: UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE

This procedure closes and finishes the piecewise uncompress.

## Syntax

```sql
UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE(
   handle  IN   BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | BINARY_INTEGER) | IN | The handle to a piecewise uncompress context. |

## Usage Notes

Syntax UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE( handle IN BINARY_INTEGER); Parameters Table 261-11 LZ_UNCOMPRESS_CLOSE Procedure Parameters Parameter Description handle The handle to a piecewise uncompress context. Exceptions invalid_handle - out of range invalid or uninitialized handle. invalid_argument - NULL handle.