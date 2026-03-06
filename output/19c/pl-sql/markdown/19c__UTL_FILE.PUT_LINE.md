---
id: 19c__UTL_FILE.PUT_LINE
name: UTL_FILE.PUT_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUT_LINE

This procedure writes the text string stored in the buffer parameter to the open file identified by the file handle.

## Syntax

```sql
UTL_FILE.PUT_LINE (
   file      IN FILE_TYPE,
   buffer    IN VARCHAR2,
   autoflush IN BOOLEAN DEFAULT FALSE);
```

## Usage Notes

The file must be open for write operations. PUT_LINE terminates the line with the platform-specific line terminator character or characters. See also " PUT_LINE_NCHAR Procedure " . Syntax UTL_FILE.PUT_LINE ( file IN FILE_TYPE, buffer IN VARCHAR2, autoflush IN BOOLEAN DEFAULT FALSE); Parameters Table 263-22 PUT_LINE Procedure Parameters Parameters Description file Active file handle returned by an FOPEN call buffer Text buffer that contains the lines to be written to the file autoflush Flushes the buffer to disk after the WRITE Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR Usage Notes The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes. If file is opened for byte mode operations, then the INVALID OPERATION exception is raised.