---
id: 19c__UTL_COMPRESS.ISOPEN
name: UTL_COMPRESS.ISOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_COMPRESS
tags: [utl_compress]
source_file: UTL_COMPRESS.html
---

# UTL_COMPRESS.ISOPEN

This function checks to see if the handle to a piecewise (un)compress context is open or closed.

## Syntax

```sql
UTL_COMPRESS.ISOPEN(
   handle in binary_integer) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | binary_integer) | in | The handle to a piecewise uncompress context. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax UTL_COMPRESS.ISOPEN( handle in binary_integer) RETURN BOOLEAN; Parameters Table 261-3 ISOPEN Function Parameters Parameter Description handle The handle to a piecewise uncompress context. Return Values TRUE if the given piecewise handle is opened, otherwise FALSE . Examples IF (UTL_COMPRESS.ISOPEN(myhandle) = TRUE) then UTL_COMPRESS.LZ_COMPRESS_CLOSE(myhandle, lob_1); END IF; Alternatively: IF (UTL_COMPRESS.ISOPEN(myhandle) = TRUE) THEN UTL_COMPRESS.LZ_UNCOMPRESS_CLOSE(myhandle); END IF;