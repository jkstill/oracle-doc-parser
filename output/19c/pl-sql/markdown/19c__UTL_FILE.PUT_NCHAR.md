---
id: 19c__UTL_FILE.PUT_NCHAR
name: UTL_FILE.PUT_NCHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUT_NCHAR

This procedure writes the text string stored in the buffer parameter to the open file identified by the file handle.

## Syntax

```sql
UTL_FILE.PUT_NCHAR (
   file      IN FILE_TYPE,
   buffer    IN NVARCHAR2);
```

## Usage Notes

With this function, you can write a text file in Unicode instead of in the database character set. The file must be opened in the national character set mode. The text string will be written in the UTF8 character set. The expected buffer datatype is NVARCHAR2 . If a variable of another datatype is specified, PL/SQL will perform implicit conversion to NVARCHAR2 before writing the text. Syntax UTL_FILE.PUT_NCHAR ( file IN FILE_TYPE, buffer IN NVARCHAR2); Parameters Table 263-24 PUT_NCHAR Procedure Parameters Parameters Description file Active file handle returned by an FOPEN_NCHAR call. If the file is opened by FOPEN instead of FOPEN_NCHAR , a CHARSETMISMATCH exception is raised. buffer Buffer that contains the text to be written to the file. User must have opened the file using mode w or mode a ; otherwise, an INVALID_OPERATION exception is raised. Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR Usage Notes The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes.