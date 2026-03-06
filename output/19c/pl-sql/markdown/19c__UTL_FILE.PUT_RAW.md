---
id: 19c__UTL_FILE.PUT_RAW
name: UTL_FILE.PUT_RAW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.PUT_RAW

This procedure accepts as input a RAW data value and writes the value to the output buffer.

## Syntax

```sql
UTL_FILE.PUT_RAW (
   file          IN    UTL_FILE.FILE_TYPE,
   buffer        IN    RAW, 
   autoflush     IN    BOOLEAN DEFAULT FALSE);
```

## Usage Notes

Syntax UTL_FILE.PUT_RAW ( file IN UTL_FILE.FILE_TYPE, buffer IN RAW, autoflush IN BOOLEAN DEFAULT FALSE); Parameters Table 263-27 PUT_RAW Procedure Parameters Parameters Description file File handle buffer The RAW data written to the buffer autoflush If TRUE , then performs a flush after writing the value to the output buffer; default is FALSE. Exceptions INVALID_FILEHANDLE INVALID_OPERATION WRITE_ERROR Usage Notes You can request an automatic flush of the buffer by setting the third argument to TRUE . The maximum size of the buffer parameter is 32767 bytes unless you specify a smaller size in FOPEN . If unspecified, Oracle supplies a default value of 1024. The sum of all sequential PUT calls cannot exceed 32767 without intermediate buffer flushes.