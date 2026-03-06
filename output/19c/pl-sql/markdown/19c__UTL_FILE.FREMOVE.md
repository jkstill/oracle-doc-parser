---
id: 19c__UTL_FILE.FREMOVE
name: UTL_FILE.FREMOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FREMOVE

This procedure deletes a disk file, assuming that you have sufficient privileges.

## Syntax

```sql
UTL_FILE.FREMOVE (
   location IN VARCHAR2,
   filename IN VARCHAR2);
```

## Usage Notes

Syntax UTL_FILE.FREMOVE ( location IN VARCHAR2, filename IN VARCHAR2); Parameters Table 263-13 FREMOVE Procedure Parameters Parameters Description location Directory location of the file, a DIRECTORY_NAME from ALL_DIRECTORIES (case sensitive) filename Name of the file to be deleted Exceptions ACCESS_DENIED DELETE_FAILED INVALID_FILENAME INVALID_OPERATION INVALID_PATH Usage Notes The FREMOVE procedure does not verify privileges before deleting a file. The O/S verifies file and directory permissions. An exception is returned on failure.