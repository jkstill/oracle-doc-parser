---
id: 19c__UTL_FILE.FGETATTR
name: UTL_FILE.FGETATTR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FGETATTR

This procedure reads and returns the attributes of a disk file.

## Syntax

```sql
UTL_FILE.FGETATTR(
   location     IN VARCHAR2, 
   filename     IN VARCHAR2, 
   fexists      OUT BOOLEAN, 
   file_length  OUT NUMBER, 
   block_size   OUT BINARY_INTEGER);
```

## Usage Notes

Syntax UTL_FILE.FGETATTR( location IN VARCHAR2, filename IN VARCHAR2, fexists OUT BOOLEAN, file_length OUT NUMBER, block_size OUT BINARY_INTEGER); Parameters Table 263-7 FGETATTR Procedure Parameters Parameters Description location Directory location of the source file, a DIRECTORY_NAME from the ALL_DIRECTORIES view (case sensitive) filename Name of the file to be examined fexists A BOOLEAN for whether or not the file exists file_length Length of the file in bytes. NULL if file does not exist. block_size File system block size in bytes. NULL if the file does not exist. Exceptions INVALID_PATH INVALID_FILENAME INVALID_OPERATION READ_ERROR ACCESS_DENIED