---
id: 19c__UTL_FILE
name: UTL_FILE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE

The UTL_FILE package defines a RECORD type.

## Syntax

```sql
TYPE file_type IS RECORD (
   id          BINARY_INTEGER, 
   datatype    BINARY_INTEGER,
   byte_mode   BOOLEAN);
```

## Usage Notes

Record Types FILETYPE Record Type TYPE file_type IS RECORD ( id BINARY_INTEGER, datatype BINARY_INTEGER, byte_mode BOOLEAN); Fields Table 263-2 FILE_TYPE Fields Field Description id A numeric value indicating the internal file handle number datatype Indicates whether the file is a CHAR file, Nchar file or other (binary) byte_mode Indicates whether the file was open as a binary file, or as a text file Caution: Oracle does not guarantee the persistence of FILE_TYPE values between database sessions or within a single session. Attempts to clone file handles or use dummy file handles may have inderterminate outcomes. Caution: Oracle does not guarantee the persistence of FILE_TYPE values between database sessions or within a single session. Attempts to clone file handles or use dummy file handles may have inderterminate outcomes.