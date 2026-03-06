---
id: 19c__DBMS_LOB.FILECLOSE
name: DBMS_LOB.FILECLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FILECLOSE

This procedure closes a BFILE that has already been opened through the input locator.

## Syntax

```sql
DBMS_LOB.FILECLOSE (
    file_loc IN OUT NOCOPY BFILE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | NOCOPY | IN OUT | Locator for the BFILE to be closed. |

## Usage Notes

Note: The database has only read-only access to BFILEs . This means that BFILEs cannot be written through the database. Note: The database has only read-only access to BFILEs . This means that BFILEs cannot be written through the database. Syntax DBMS_LOB.FILECLOSE ( file_loc IN OUT NOCOPY BFILE); Parameters Table 99-33 FILECLOSE Procedure Parameters Parameter Description file_loc Locator for the BFILE to be closed. Exceptions Table 99-34 FILECLOSE Procedure Exceptions Exception Description VALUE_ERROR NULL input value for file_loc . UNOPENED_FILE File was not opened with the input locator. NOEXIST_DIRECTORY Directory does not exist. NOPRIV_DIRECTORY You do not have privileges for the directory. INVALID_DIRECTORY Directory has been invalidated after the file was opened. INVALID_OPERATION File does not exist, or you do not have access privileges on the file. See Also: " FILEOPEN Procedure " " FILECLOSEALL Procedure " Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure