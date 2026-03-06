---
id: 19c__UTL_COMPRESS.LZ_COMPRESS_ADD
name: UTL_COMPRESS.LZ_COMPRESS_ADD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_COMPRESS_ADD

This procedure adds a piece of compressed data.

## Syntax

```sql
UTL_COMPRESS.LZ_COMPRESS_ADD (
   handle IN             BINARY_INTEGER, 
   dst    IN OUT NOCOPY  BLOB, 
   src    IN             RAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | BINARY_INTEGER | IN | The handle to a piecewise compress context. |
| dst | NOCOPY | IN OUT | The opened LOB from LZ_COMPRESS_OPEN to store compressed data. |
| src | RAW) | IN | The input data to be compressed. |

## Usage Notes

Syntax UTL_COMPRESS.LZ_COMPRESS_ADD ( handle IN BINARY_INTEGER, dst IN OUT NOCOPY BLOB, src IN RAW); Parameters Table 261-5 LZ_COMPRESS_ADD Procedure Parameters Parameter Description handle The handle to a piecewise compress context. dst The opened LOB from LZ_COMPRESS_OPEN to store compressed data. src The input data to be compressed. Exceptions invalid_handle - out of range invalid or unopened handle. invalid_argument - NULL handle, src, dst, or invalid dst .