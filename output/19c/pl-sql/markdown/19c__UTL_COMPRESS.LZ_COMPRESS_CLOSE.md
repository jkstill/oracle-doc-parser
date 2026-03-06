---
id: 19c__UTL_COMPRESS.LZ_COMPRESS_CLOSE
name: UTL_COMPRESS.LZ_COMPRESS_CLOSE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_COMPRESS_CLOSE

This procedure closes and finishes piecewise compress operation.

## Syntax

```sql
UTL_COMPRESS.LZ_COMPRESS_CLOSE (
   handle IN             BINARY_INTEGER, 
   dst    IN OUT NOCOPY  BLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | BINARY_INTEGER | IN | The handle to a piecewise compress context. |
| dst | NOCOPY | IN OUT | The opened LOB from LZ_COMPRESS_OPEN to store compressed data. |

## Usage Notes

Syntax UTL_COMPRESS.LZ_COMPRESS_CLOSE ( handle IN BINARY_INTEGER, dst IN OUT NOCOPY BLOB); Parameters Table 261-6 LZ_COMPRESS_CLOSE Procedure Parameters Parameter Description handle The handle to a piecewise compress context. dst The opened LOB from LZ_COMPRESS_OPEN to store compressed data. Exceptions invalid_handle - out of range invalid or uninitialized handle. invalid_argument - NULL handle, dst , or invalid dst .