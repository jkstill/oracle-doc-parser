---
id: 19c__UTL_FILE.IS_OPEN
name: UTL_FILE.IS_OPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.IS_OPEN

This function tests a file handle to see if it identifies an open file.

## Syntax

```sql
UTL_FILE.IS_OPEN (
   file  IN FILE_TYPE)
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file | FILE_TYPE) | IN | Active file handle returned by an FOPEN or FOPEN_NCHAR call |

**Returns:** `BOOLEAN`

## Usage Notes

IS_OPEN reports only whether a file handle represents a file that has been opened, but not yet closed. It does not guarantee that there will be no operating system errors when you attempt to use the file handle. Syntax UTL_FILE.IS_OPEN ( file IN FILE_TYPE) RETURN BOOLEAN; Parameters Table 263-19 IS_OPEN Function Parameters Parameter Description file Active file handle returned by an FOPEN or FOPEN_NCHAR call Return Values TRUE or FALSE Exceptions INVALID_FILEHANDLE