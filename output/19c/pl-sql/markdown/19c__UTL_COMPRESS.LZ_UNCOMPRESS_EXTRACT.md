---
id: 19c__UTL_COMPRESS.LZ_UNCOMPRESS_EXTRACT
name: UTL_COMPRESS.LZ_UNCOMPRESS_EXTRACT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_UNCOMPRESS_EXTRACT

This procedure extracts a piece of uncompressed data.

## Syntax

```sql
UTL_COMPRESS.LZ_UNCOMPRESS_EXTRACT(
   handle  IN          BINARY_INTEGER, 
   dst     OUT NOCOPY  RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | BINARY_INTEGER | IN | The handle to a piecewise uncompress context. |
| dst | NOCOPY | OUT | The uncompressed data. |

## Usage Notes

Syntax UTL_COMPRESS.LZ_UNCOMPRESS_EXTRACT( handle IN BINARY_INTEGER, dst OUT NOCOPY RAW); Parameters Table 261-9 LZ_UNCOMPRESS_EXTRACT Function Parameters Parameter Description handle The handle to a piecewise uncompress context. dst The uncompressed data. Exceptions no_data_found - finished uncompress. invalid_handle - out of range invalid or uninitialized handle. invalid_argument - NULL handle.