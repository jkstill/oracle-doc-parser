---
id: 19c__DBMS_LOB.FILEGETNAME
name: DBMS_LOB.FILEGETNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FILEGETNAME

This procedure determines the directory object and filename, given a BFILE locator.

## Syntax

```sql
DBMS_LOB.FILEGETNAME (
   file_loc   IN    BFILE, 
   dir_alias  OUT   VARCHAR2,
   filename   OUT   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | BFILE | IN | Locator for the BFILE |
| dir_alias | VARCHAR2 | OUT | Directory object name |
| filename | VARCHAR2) | OUT | Name of the BFILE |

## Usage Notes

This function only indicates the directory object name and filename assigned to the locator, not if the physical file or directory actually exists. The maximum constraint values for the dir_alias buffer is 30, and for the entire path name, it is 2000. Syntax DBMS_LOB.FILEGETNAME ( file_loc IN BFILE, dir_alias OUT VARCHAR2, filename OUT VARCHAR2); Parameters Table 99-39 FILEGETNAME Procedure Parameters Parameter Description file_loc Locator for the BFILE dir_alias Directory object name filename Name of the BFILE Exceptions Table 99-40 FILEGETNAME Procedure Exceptions Exception Description VALUE_ERROR Any of the input parameters are NULL or INVALID . INVALID_ARGVAL dir_alias or filename are NULL . See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure