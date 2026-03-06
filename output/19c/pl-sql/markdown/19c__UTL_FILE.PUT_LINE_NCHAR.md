---
id: 19c__UTL_FILE.PUT_LINE_NCHAR
name: UTL_FILE.PUT_LINE_NCHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUT_LINE_NCHAR

This procedure writes the text string stored in the buffer parameter to the open file identified by the file handle. With this function, you can write a text file in Unicode instead of in the database character set.

## Syntax

```sql
UTL_FILE.PUT_LINE_NCHAR (
   file    IN FILE_TYPE,
   buffer  IN NVARCHAR2);
```

## Usage Notes

This procedure is equivalent to the PUT_NCHAR Procedure , except that the line separator is appended to the written text. See also PUT_LINE Procedure . Syntax UTL_FILE.PUT_LINE_NCHAR ( file IN FILE_TYPE, buffer IN NVARCHAR2); Parameters Table 263-23 PUT_LINE_NCHAR Procedure Parameters Parameters Description file Active file handle returned by an FOPEN_NCHAR call. The file must be open for writing. buffer Text buffer that contains the lines to be written to the file Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR Usage Notes The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes. If file is opened for byte mode operations, then the INVALID OPERATION exception is raised.