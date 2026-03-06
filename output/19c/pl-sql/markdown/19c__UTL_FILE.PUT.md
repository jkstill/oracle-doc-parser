---
id: 19c__UTL_FILE.PUT
name: UTL_FILE.PUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUT

PUT writes the text string stored in the buffer parameter to the open file identified by the file handle.

## Syntax

```sql
UTL_FILE.PUT (
   file      IN FILE_TYPE,
   buffer    IN VARCHAR2);
```

## Usage Notes

The file must be open for write operations. No line terminator is appended by PUT ; use NEW_LINE to terminate the line or use PUT_LINE to write a complete line with a line terminator. See also " PUT_NCHAR Procedure " . Syntax UTL_FILE.PUT ( file IN FILE_TYPE, buffer IN VARCHAR2); Parameters Table 263-21 PUT Procedure Parameters Parameters Description file Active file handle returned by an FOPEN_NCHAR call. The file must be open for writing. buffer Buffer that contains the text to be written to the file. User must have opened the file using mode w or mode a ; otherwise, an INVALID_OPERATION exception is raised. Usage Notes The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes. Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR