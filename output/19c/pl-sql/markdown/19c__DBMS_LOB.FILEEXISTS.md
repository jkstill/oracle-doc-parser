---
id: 19c__DBMS_LOB.FILEEXISTS
name: DBMS_LOB.FILEEXISTS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FILEEXISTS

This function finds out if a specified BFILE locator points to a file that actually exists on the server's file system.

## Syntax

```sql
DBMS_LOB.FILEEXISTS (
   file_loc     IN    BFILE)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | BFILE) | IN | Locator for the BFILE . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.FILEEXISTS ( file_loc IN BFILE) RETURN INTEGER; Pragmas pragma restrict_references(FILEEXISTS, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-36 FILEEXISTS Function Parameter Parameter Description file_loc Locator for the BFILE . Return Values Table 99-37 FILEEXISTS Function Return Values Return Description 0 Physical file does not exist. 1 Physical file exists. Exceptions Table 99-38 FILEEXISTS Function Exceptions Exception Description NOEXIST_DIRECTORY Directory does not exist. NOPRIV_DIRECTORY You do not have privileges for the directory. INVALID_DIRECTORY Directory has been invalidated after the file was opened. See Also: " FILEISOPEN Function " . Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure