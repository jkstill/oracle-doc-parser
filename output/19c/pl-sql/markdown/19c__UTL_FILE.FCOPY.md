---
id: 19c__UTL_FILE.FCOPY
name: UTL_FILE.FCOPY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FCOPY

This procedure copies a contiguous portion of a file to a newly created file.

## Syntax

```sql
UTL_FILE.FCOPY (
   src_location    IN VARCHAR2,
   src_filename    IN VARCHAR2,
   dest_location   IN VARCHAR2,
   dest_filename   IN VARCHAR2,
   start_line      IN BINARY_INTEGER DEFAULT 1,
   end_line        IN BINARY_INTEGER DEFAULT NULL);
```

## Usage Notes

By default, the whole file is copied if the start_line and end_line parameters are omitted. The source file is opened in read mode. The destination file is opened in write mode. A starting and ending line number can optionally be specified to select a portion from the center of the source file for copying. Syntax UTL_FILE.FCOPY ( src_location IN VARCHAR2, src_filename IN VARCHAR2, dest_location IN VARCHAR2, dest_filename IN VARCHAR2, start_line IN BINARY_INTEGER DEFAULT 1, end_line IN BINARY_INTEGER DEFAULT NULL); Parameters Table 263-5 FCOPY Procedure Parameters Parameters Description src_location Directory location of the source file, a DIRECTORY_NAME from the ALL_DIRECTORIES view (case sensitive) src_filename Source file to be copied dest_location Destination directory where the destination file is created dest_filename Destination file created from the source file start_line Line number at which to begin copying. The default is 1 for the first line end_line Line number at which to stop copying. The default is NULL, signifying end of file Exceptions INVALID_FILENAME INVALID_PATH INVALID_OPERATION INVALID_OFFSET READ_ERROR WRITE_ERROR