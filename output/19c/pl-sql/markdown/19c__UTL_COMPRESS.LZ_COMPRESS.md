---
id: 19c__UTL_COMPRESS.LZ_COMPRESS
name: UTL_COMPRESS.LZ_COMPRESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.LZ_COMPRESS

These functions and procedures compress data using Lempel-Ziv compression algorithm.

## Syntax

```sql
UTL_COMPRESS.LZ_COMPRESS (
   src       IN           RAW,
   quality   IN           BINARY_INTEGER DEFAULT 6) 
 RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| src | RAW | IN | Data ( RAW , BLOB or BFILE ) to be compressed. |
| dst |  |  | Destination for compressed data |
| quality | BINARY_INTEGER | IN | An integer in the range 1 to 9, 1=fast compression, 9=best compression, default=6 |

**Returns:** `RAW`

## Usage Notes

Syntax This function accept a RAW as input, compress it and return the compressed RAW result and metadata: UTL_COMPRESS.LZ_COMPRESS ( src IN RAW, quality IN BINARY_INTEGER DEFAULT 6) RETURN RAW; This function accept a BLOB as input, compress it and returns a temporary BLOB for the compressed data: UTL_COMPRESS.LZ_COMPRESS ( src IN BLOB, quality IN BINARY_INTEGER DEFAULT 6) RETURN BLOB; This procedure returns the compressed data into the existing BLOB(dst) which is trimmed to the compressed data size: UTL_COMPRESS.LZ_COMPRESS ( src IN BLOB, dst IN OUT NOCOPY BLOB, quality IN BINARY_INTEGER DEFAULT 6); This function returns a temporary BLOB for the compressed data: UTL_COMPRESS.LZ_COMPRESS ( src IN BFILE, quality IN BINARY_INTEGER DEFAULT 6) RETURN BLOB; This procedure will return the compressed data into the existing BLOB(dst) which is trimmed to the compressed data size: UTL_COMPRESS.LZ_COMPRESS ( src IN BFILE, dst IN OUT NOCOPY BLOB, quality IN BINARY_INTEGER DEFAULT 6); Parameters Table 261-4 LZ_COMPRESS Function and Procedures Parameters Parameter Description src Data ( RAW , BLOB or BFILE ) to be compressed. dst Destination for compressed data quality An integer in the range 1 to 9, 1=fast compression, 9=best compression, default=6 Usage Notes quality is an optional compression tuning value. It allows the UTL_COMPRESS user to choose between speed and compression quality, meaning the percentage of reduction in size. A faster compression speed will result in less compression of the data. A slower compression speed will result in more compression of the data. Valid values are [1..9], with 1=fastest and 9=slowest. The default 'quality' value is 6.