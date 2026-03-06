---
id: 19c__UTL_FILE.FFLUSH
name: UTL_FILE.FFLUSH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FFLUSH

FFLUSH physically writes pending data to the file identified by the file handle. Normally, data being written to a file is buffered. The FFLUSH procedure forces the buffered data to be written to the file. The data must be terminated with a newline character.

## Syntax

```sql
UTL_FILE.FFLUSH (
   file  IN FILE_TYPE);
```

## Usage Notes

Flushing is useful when the file must be read while still open. For example, debugging messages can be flushed to the file so that they can be read immediately. Syntax UTL_FILE.FFLUSH ( file IN FILE_TYPE); Parameters Table 263-6 FFLUSH Procedure Parameters Parameters Description file Active file handle returned by an FOPEN or FOPEN_NCHAR call Exceptions INVALID_FILENAME INVALID_MAXLINESIZE INVALID_OPERATION WRITE_ERROR