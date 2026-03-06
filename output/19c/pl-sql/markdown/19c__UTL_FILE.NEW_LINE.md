---
id: 19c__UTL_FILE.NEW_LINE
name: UTL_FILE.NEW_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.NEW_LINE

This procedure writes one or more line terminators to the file identified by the input file handle.

## Syntax

```sql
UTL_FILE.NEW_LINE (
   file     IN FILE_TYPE,
   lines    IN BINARY_INTEGER := 1);
```

## Usage Notes

This procedure is separate from PUT because the line terminator is a platform-specific character or sequence of characters. Syntax UTL_FILE.NEW_LINE ( file IN FILE_TYPE, lines IN BINARY_INTEGER := 1); Parameters Table 263-20 NEW_LINE Procedure Parameters Parameters Description file Active file handle returned by an FOPEN or FOPEN_NCHAR call lines Number of line terminators to be written to the file Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR