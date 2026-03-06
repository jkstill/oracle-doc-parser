---
id: 19c__UTL_FILE.FGETPOS
name: UTL_FILE.FGETPOS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FGETPOS

This function returns the current relative offset position within a file, in bytes.

## Syntax

```sql
UTL_FILE.FGETPOS (
   file IN FILE_TYPE)
 RETURN PLS_INTEGER;
```

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_FILE.FGETPOS ( file IN FILE_TYPE) RETURN PLS_INTEGER; Parameters Table 263-8 FGETPOS Parameters Parameters Description file Directory location of the source file Return Values FGETPOS returns the relative offset position for an open file, in bytes. It raises an exception if the file is not open. It returns 0 for the beginning of the file. Exceptions INVALID_FILEHANDLE INVALID_OPERATION READ_ERROR Usage Notes If file is opened for byte mode operations, then the INVALID OPERATION exception is raised.