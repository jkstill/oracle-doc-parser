---
id: 19c__DBMS_LOB.FILEOPEN
name: DBMS_LOB.FILEOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FILEOPEN

This procedure opens a BFILE for read-only access. BFILE data may not be written through the database.

## Syntax

```sql
DBMS_LOB.FILEOPEN (
   file_loc   IN OUT NOCOPY  BFILE, 
   open_mode  IN             BINARY_INTEGER := file_readonly);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | NOCOPY | IN OUT | Locator for the BFILE . |
| open_mode | BINARY_INTEGER | IN | File access is read-only. |

## Usage Notes

Syntax DBMS_LOB.FILEOPEN ( file_loc IN OUT NOCOPY BFILE, open_mode IN BINARY_INTEGER := file_readonly); Parameters Table 99-43 FILEOPEN Procedure Parameters Parameter Description file_loc Locator for the BFILE . open_mode File access is read-only. Exceptions Table 99-44 FILEOPEN Procedure Exceptions Exception Description VALUE_ERROR file_loc or open_mode is NULL . INVALID_ARGVAL open_mode is not equal to FILE_READONLY . OPEN_TOOMANY Number of open files in the session exceeds session_max_open_files . NOEXIST_DIRECTORY Directory associated with file_loc does not exist. INVALID_DIRECTORY Directory has been invalidated after the file was opened. INVALID_OPERATION File does not exist, or you do not have access privileges on the file. See Also: " FILECLOSE Procedure " " FILECLOSEALL Procedure " Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: " FILECLOSE Procedure " " FILECLOSEALL Procedure " Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure