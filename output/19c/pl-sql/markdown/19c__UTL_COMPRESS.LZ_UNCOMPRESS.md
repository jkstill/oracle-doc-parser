---
id: 19c__UTL_COMPRESS.LZ_UNCOMPRESS
name: UTL_COMPRESS.LZ_UNCOMPRESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_UNCOMPRESS

This procedure accepts as input a RAW , BLOB or BFILE compressed string, verifies it to be a valid compressed value, uncompresses it using Lempel-Ziv compression algorithm, and returns the uncompressed RAW or BLOB result.

## Syntax

```sql
UTL_COMPRESS.LZ_UNCOMPRESS(
   src  IN  RAW)
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| src | RAW) | IN | Compressed data. |
| dst |  |  | Destination for uncompressed data. |

**Returns:** `RAW`

## Usage Notes

Syntax This function returns uncompressed data as RAW : UTL_COMPRESS.LZ_UNCOMPRESS( src IN RAW) RETURN RAW; This function returns uncompressed data as a temporary BLOB : UTL_COMPRESS.LZ_UNCOMPRESS( src IN BLOB) RETURN BLOB; This procedure returns the uncompressed data into the existing BLOB ( dst ), which will be trimmed to the uncompressed data size: UTL_COMPRESS.LZ_UNCOMPRESS( src IN BLOB, dst IN OUT NOCOPY BLOB); This function returns a temporary BLOB for the uncompressed data: UTL_COMPRESS.LZ_UNCOMPRESS( src IN BFILE) RETURN BLOB; This procedure returns the uncompressed data into the existing BLOB ( dst ). The original dst data will be overwritten. UTL_COMPRESS.LZ_UNCOMPRESS( src IN BFILE, dst IN OUT NOCOPY BLOB); Parameters Table 261-8 LZ_UNCOMPRESS Function and Procedures Parameters Parameter Description src Compressed data. dst Destination for uncompressed data.