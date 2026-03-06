---
id: 19c__UTL_FILE.FCLOSE
name: UTL_FILE.FCLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FCLOSE

This procedure closes an open file identified by a file handle.

## Syntax

```sql
UTL_FILE.FCLOSE (
   file IN OUT FILE_TYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file | FILE_TYPE) | IN OUT | Active file handle returned by an FOPEN or FOPEN_NCHAR call |

## Usage Notes

Syntax UTL_FILE.FCLOSE ( file IN OUT FILE_TYPE); Parameters Table 263-4 FCLOSE Procedure Parameters Parameter Description file Active file handle returned by an FOPEN or FOPEN_NCHAR call Usage Notes If there is buffered data yet to be written when FCLOSE runs, then you may receive a WRITE_ERROR exception when closing a file. Exceptions WRITE_ERROR INVALID_FILEHANDLE