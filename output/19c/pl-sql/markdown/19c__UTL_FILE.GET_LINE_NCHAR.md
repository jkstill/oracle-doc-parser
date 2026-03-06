---
id: 19c__UTL_FILE.GET_LINE_NCHAR
name: UTL_FILE.GET_LINE_NCHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.GET_LINE_NCHAR

This procedure reads text from the open file identified by the file handle and places the text in the output buffer parameter. With this function, you can read a text file in Unicode instead of in the database character set.

## Syntax

```sql
UTL_FILE.GET_LINE_NCHAR (
   file        IN  FILE_TYPE,
   buffer      OUT NVARCHAR2,
   len         IN  PLS_INTEGER DEFAULT NULL);
```

## Usage Notes

The file must be opened in national character set mode, and must be encoded in the UTF8 character set. The expected buffer datatype is NVARCHAR2 . If a variable of another datatype, such as NCHAR , NCLOB , or VARCHAR2 is specified, PL/SQL will perform standard implicit conversion from NVARCHAR2 after the text is read. See also GET_LINE Procedure Syntax UTL_FILE.GET_LINE_NCHAR ( file IN FILE_TYPE, buffer OUT NVARCHAR2, len IN PLS_INTEGER DEFAULT NULL); Parameters Table 263-17 GET_LINE_NCHAR Procedure Parameters Parameters Description file Active file handle returned by an FOPEN_NCHAR call. The file must be open for reading (mode r ). If the file is opened by FOPEN instead of FOPEN_NCHAR , a CHARSETMISMATCH exception is raised. buffer Data buffer to receive the line read from the file len The number of bytes read from the file. Default is NULL . If NULL , Oracle supplies the value of max_linesize. Exceptions INVALID_FILEHANDLE INVALID_OPERATION NO_DATA_FOUND READ_ERROR