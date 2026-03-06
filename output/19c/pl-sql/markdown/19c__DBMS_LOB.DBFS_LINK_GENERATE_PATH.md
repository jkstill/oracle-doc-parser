---
id: 19c__DBMS_LOB.DBFS_LINK_GENERATE_PATH
name: DBMS_LOB.DBFS_LINK_GENERATE_PATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.DBFS_LINK_GENERATE_PATH

This subprogram returns a unique file path name for use in creating a DBFS Link.

## Syntax

```sql
DBMS_LOB.DBFS_LINK_GENERATE_PATH (
  lob_loc       IN BLOB,
  storage_dir   IN VARCHAR2) 
 RETURN VARCHAR2;
 
DBMS_LOB.DBFS_LINK_GENERATE_PATH (
  lob_loc       IN CLOB CHARACTER SET ANY_CS,
  storage_dir   IN VARCHAR2) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | LOB to be retrieved from DBFS |
| storage_dir | VARCHAR2) | IN | DBFS directory that will be the parent directory of the file |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_LOB.DBFS_LINK_GENERATE_PATH ( lob_loc IN BLOB, storage_dir IN VARCHAR2) RETURN VARCHAR2; DBMS_LOB.DBFS_LINK_GENERATE_PATH ( lob_loc IN CLOB CHARACTER SET ANY_CS, storage_dir IN VARCHAR2) RETURN VARCHAR2; Pragmas PRAGMA RESTRICT_REFERENCES(dbfs_link_generate_path, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-29 DBFS_LINK_GENERATE_PATH Function Parameters Parameter Description lob_loc LOB to be retrieved from DBFS storage_dir DBFS directory that will be the parent directory of the file Exceptions Table 99-30 DBFS_LINK_GENERATE_PATH Function Exceptions Exception Description SECUREFILE_WRONGTYPE lob_loc is not a SECUREFILE Usage Notes Returns a globally unique file pathname that can be used for archiving. This is guaranteed to be globally unique across all calls to this function for different LOBs and versions of that LOB. It is always the same for the same LOB and version.