---
id: 19c__UTL_FILE.PUTF
name: UTL_FILE.PUTF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUTF

This procedure is a formatted PUT procedure.

## Syntax

```sql
UTL_FILE.PUTF (
   file    IN FILE_TYPE,
   format  IN VARCHAR2,
   [arg1   IN VARCHAR2  DEFAULT NULL,
   . . .  
   arg5    IN VARCHAR2  DEFAULT NULL]);
```

## Usage Notes

It works like a limited printf (). Syntax UTL_FILE.PUTF ( file IN FILE_TYPE, format IN VARCHAR2, [arg1 IN VARCHAR2 DEFAULT NULL, . . . arg5 IN VARCHAR2 DEFAULT NULL]); Parameters Table 263-25 PUTF Procedure Parameters Parameters Description file Active file handle returned by an FOPEN call format Format string that can contain text as well as the formatting characters \n and %s arg1..arg5 From one to five operational argument strings. Argument strings are substituted, in order, for the %s formatters in the format string. If there are more formatters in the format parameter string than there are arguments, then an empty string is substituted for each %s for which there is no argument. Usage Notes If file is opened for byte mode operations, then the INVALID OPERATION exception is raised. The format string can contain any text, but the character sequences %s and \n have special meaning. Character Sequence Meaning %s Substitute this sequence with the string value of the next argument in the argument list. \n Substitute with the appropriate platform-specific line terminator. Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR