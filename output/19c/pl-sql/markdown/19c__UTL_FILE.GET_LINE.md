---
id: 19c__UTL_FILE.GET_LINE
name: UTL_FILE.GET_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.GET_LINE

This procedure reads text from the open file identified by the file handle and places the text in the output buffer parameter. Text is read up to, but not including, the line terminator, or up to the end of the file, or up to the end of the len parameter. It cannot exceed the max_linesize specified in FOPEN .

## Syntax

```sql
UTL_FILE.GET_LINE (
   file        IN  FILE_TYPE,
   buffer      OUT VARCHAR2,
   len         IN  PLS_INTEGER DEFAULT NULL);
```

## Usage Notes

Syntax UTL_FILE.GET_LINE ( file IN FILE_TYPE, buffer OUT VARCHAR2, len IN PLS_INTEGER DEFAULT NULL); Parameters Table 263-16 GET_LINE Procedure Parameters Parameters Description file Active file handle returned by an FOPEN call. The file must be open for reading (mode r ); otherwise an INVALID_OPERATION exception is raised. buffer Data buffer to receive the line read from the file len The number of bytes read from the file. Default is NULL . If NULL , Oracle supplies the value of max_linesize . Exceptions INVALID_FILEHANDLE INVALID_OPERATION NO_DATA_FOUND READ_ERROR Usage Notes If the line does not fit in the buffer, a READ_ERROR exception is raised. If no text was read due to end of file, the NO_DATA_FOUND exception is raised. If the file is opened for byte mode operations, the INVALID_OPERATION exception is raised. Because the line terminator character is not read into the buffer, reading blank lines returns empty strings. The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN .If unspecified, Oracle supplies a default value of 1024. See also " GET_LINE_NCHAR Procedure " .