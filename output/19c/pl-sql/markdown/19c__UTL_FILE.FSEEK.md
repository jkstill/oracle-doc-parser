---
id: 19c__UTL_FILE.FSEEK
name: UTL_FILE.FSEEK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FSEEK

This procedure adjusts the file pointer forward or backward within the file by the number of bytes specified.

## Syntax

```sql
UTL_FILE.FSEEK (
   file             IN OUT  UTL_FILE.FILE_TYPE,
   absolute_offset  IN      PL_INTEGER DEFAULT NULL,
   relative_offset  IN      PLS_INTEGER DEFAULT NULL);
```

## Usage Notes

Syntax UTL_FILE.FSEEK ( file IN OUT UTL_FILE.FILE_TYPE, absolute_offset IN PL_INTEGER DEFAULT NULL, relative_offset IN PLS_INTEGER DEFAULT NULL); Parameters Table 263-15 FSEEK Procedure Parameters Parameters Description file File handle absolute_offset Absolute location to which to seek; default = NULL relative_offset Number of bytes to seek forward or backward; positive = forward, negative integer = backward, zero = current position, default = NULL Exceptions INVALID_FILEHANDLE INVALID_OFFSET INVALID_OPERATION READ_ERROR Usage Notes Using FSEEK , you can read previous lines in the file without first closing and reopening the file. You must know the number of bytes by which you want to navigate. If relative_offset , the procedure seeks forward. If relative_offset > 0, or backward, if relative_offset < 0, the procedure seeks through the file by the number of relative_offset bytes specified. If the beginning of the file is reached before the number of bytes specified, then the file pointer is placed at the beginning of the file. If the end of the file is reached before the number of bytes specified, then an INVALID_OFFSET error is raised. If absolute_offset , the procedure seeks to an absolute location specified in bytes. If file is opened for byte mode operations, then the INVALID OPERATION exception is raised.