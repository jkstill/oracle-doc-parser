---
id: 19c__UTL_FILE.PUTF_NCHAR
name: UTL_FILE.PUTF_NCHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUTF_NCHAR

This procedure is a formatted version of a PUT_NCHAR Procedure.

## Syntax

```sql
UTL_FILE.PUTF_NCHAR (
   file    IN FILE_TYPE,
   format  IN NVARCHAR2,
   [arg1   IN NVARCHAR2  DEFAULT NULL,
   . . .  
   arg5    IN NVARCHAR2  DEFAULT NULL]);
```

## Usage Notes

Using PUTF_NCHAR , you can write a text file in Unicode instead of in the database character set. It accepts a format string with formatting elements \n and %s , and up to five arguments to be substituted for consecutive instances of %s in the format string. The expected datatype of the format string and the arguments is NVARCHAR2 . If variables of another datatype are specified, PL/SQL will perform implicit conversion to NVARCHAR2 before formatting the text. Formatted text is written in the UTF8 character set to the file identified by the file handle. The file must be opened in the national character set mode. Syntax UTL_FILE.PUTF_NCHAR ( file IN FILE_TYPE, format IN NVARCHAR2, [arg1 IN NVARCHAR2 DEFAULT NULL, . . . arg5 IN NVARCHAR2 DEFAULT NULL]); Parameters Table 263-26 PUTF_NCHAR Procedure Parameters Parameters Description file Active file handle returned by an FOPEN_NCHAR call. The file must be open for reading (mode r ). If the file is opened by FOPEN instead of FOPEN_NCHAR , a CHARSETMISMATCH exception is raised. format Format string that can contain text as well as the formatting characters \n and %s arg1..arg5 From one to five operational argument strings. Argument strings are substituted, in order, for the %s formatters in the format string. If there are more formatters in the format parameter string than there are arguments, then an empty string is substituted for each %s for which there is no argument. Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR Usage Notes The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes. If file is opened for byte mode operations, then the INVALID OPERATION exception is raised.