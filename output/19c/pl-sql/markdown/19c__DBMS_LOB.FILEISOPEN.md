---
id: 19c__DBMS_LOB.FILEISOPEN
name: DBMS_LOB.FILEISOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.FILEISOPEN

This function finds out whether a BFILE was opened with the specified FILE locator.

## Syntax

```sql
DBMS_LOB.FILEISOPEN (
   file_loc   IN    BFILE)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| file_loc | BFILE) | IN | Locator for the BFILE . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.FILEISOPEN ( file_loc IN BFILE) RETURN INTEGER; Pragmas PRAGMA RESTRICT_REFERENCES(fileisopen, WNDS, RNDS, WNPS, RNPS ); Parameters Table 99-41 FILEISOPEN Function Parameter Parameter Description file_loc Locator for the BFILE . Return Values INTEGER : 0 = file is not open, 1 = file is open Usage Notes If the input FILE locator was never passed to the FILEOPEN procedure, then the file is considered not to be opened by this locator. However, a different locator may have this file open. In other words, openness is associated with a specific locator.