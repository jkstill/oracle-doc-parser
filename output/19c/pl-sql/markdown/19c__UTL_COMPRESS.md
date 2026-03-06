---
id: 19c__UTL_COMPRESS
name: UTL_COMPRESS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS

Certain operational notes apply to UTL_COMPRESS .

## Usage Notes

It is the caller's responsibility to free the temporary LOB returned by the LZ * functions with DBMS_LOB.FREETEMPORARY call. A BFILE passed into LZ_COMPRESS * or l Z_UNCOMPRESS * has to be opened by DBMS_LOB.FILEOPEN . Under special circumstances (especially if the input has already been compressed) the output produced by one of the UTL_COMPRESS subprograms may be the same size, or even slightly larger than, the input. The output of the UTL_COMPRESS compressed data is compatible with gzip (with -n option) /gunzip on a single file.