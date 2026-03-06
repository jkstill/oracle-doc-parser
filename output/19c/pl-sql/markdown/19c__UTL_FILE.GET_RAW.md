---
id: 19c__UTL_FILE.GET_RAW
name: UTL_FILE.GET_RAW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.GET_RAW

This procedure reads a RAW string value from a file and adjusts the file pointer ahead by the number of bytes read. UTL_FILE.GET_RAW ignores line terminators.

## Syntax

```sql
UTL_FILE.GET_RAW (
   file       IN            UTL_FILE.FILE_TYPE, 
   buffer     OUT NOCOPY    RAW, 
   len        IN            PLS_INTEGER DEFAULT NULL);
```

## Usage Notes

Syntax UTL_FILE.GET_RAW ( file IN UTL_FILE.FILE_TYPE, buffer OUT NOCOPY RAW, len IN PLS_INTEGER DEFAULT NULL); Parameters Table 263-18 GET_RAW Procedure Parameters Parameters Description file File handle buffer RAW data len The number of bytes read from the file. Default is NULL . If NULL , len is assumed to be the maximum length of RAW . Exceptions INVALID_FILEHANDLE INVALID_OPERATION LENGTH_MISMATCH NO_DATA_FOUND READ_ERROR Usage Notes The subprogram will raise No_Data_Found when it attempts to read past the end of the file. Your application should allow for this by catching the exception in its processing loop. PROCEDURE Sys.p (n IN VARCHAR2) IS h UTL_FILE.FILE_TYPE := UTL_FILE.FOPEN('D', n, 'r', 32767); Buf RAW(32767); Amnt CONSTANT PLS_INTEGER := 32767; BEGIN LOOP BEGIN Utl_File.Get_Raw(h, Buf, Amnt); -- Do something with this chunk EXCEPTION WHEN No_Data_Found THEN EXIT; END; END LOOP; UTL_FILE.FCLOSE (h); END;