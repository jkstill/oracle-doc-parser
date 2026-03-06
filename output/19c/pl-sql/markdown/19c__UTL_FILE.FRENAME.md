---
id: 19c__UTL_FILE.FRENAME
name: UTL_FILE.FRENAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FRENAME

This procedure renames an existing file to a new name, similar to the UNIX mv function.

## Syntax

```sql
UTL_FILE.FRENAME (
   src_location     IN   VARCHAR2,
   src_filename     IN   VARCHAR2, 
   dest_location    IN   VARCHAR2,
   dest_filename    IN   VARCHAR2,
   overwrite        IN   BOOLEAN DEFAULT FALSE);
```

## Usage Notes

Syntax UTL_FILE.FRENAME ( src_location IN VARCHAR2, src_filename IN VARCHAR2, dest_location IN VARCHAR2, dest_filename IN VARCHAR2, overwrite IN BOOLEAN DEFAULT FALSE); Parameters Table 263-14 FRENAME Procedure Parameters Parameters Description src_location Directory location of the source file, a DIRECTORY_NAME from the ALL_DIRECTORIES view (case sensitive) src_filename Source file to be renamed dest_location Destination directory of the destination file, a DIRECTORY_NAME from the ALL_DIRECTORIES view (case sensitive) dest_filename New name of the file overwrite Default is FALSE . Permission on both the source and destination directories must be granted. You can use the overwrite parameter to specify whether or not to overwrite a file if one exists in the destination directory. The default is FALSE for no overwrite. Exceptions ACCESS_DENIED INVALID_FILENAME INVALID_PATH RENAME_FAILED