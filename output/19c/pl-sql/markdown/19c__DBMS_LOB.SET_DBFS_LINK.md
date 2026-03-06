---
id: 19c__DBMS_LOB.SET_DBFS_LINK
name: DBMS_LOB.SET_DBFS_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.SET_DBFS_LINK

This function links the specified SecureFile to the specified path name. It does not copy the data to the path.

## Syntax

```sql
DBMS_LOB.SET_DBFS_LINK (
  lob_loc        IN OUT BLOB,
  archive_id     IN     RAW(1024));

DBMS_LOB.SET_DBFS_LINK(
  lob_loc_dst    IN OUT CLOB CHARACTER SET ANY_CS,
  archive_id     IN     RAW(1024));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN OUT | LOB for which to store the reference value |
| archive_id | RAW(1024)) | IN | Archive ID as returned by calling either of the GET_DBFS_LINK Functions Functions |

## Usage Notes

Syntax DBMS_LOB.SET_DBFS_LINK ( lob_loc IN OUT BLOB, archive_id IN RAW(1024)); DBMS_LOB.SET_DBFS_LINK( lob_loc_dst IN OUT CLOB CHARACTER SET ANY_CS, archive_id IN RAW(1024)); Parameters Table 99-89 SET_DBFS_LINK Procedure Parameters Parameter Description lob_loc LOB for which to store the reference value archive_id Archive ID as returned by calling either of the GET_DBFS_LINK Functions Functions Exceptions Table 99-90 SET_DBFS_LINK Procedure Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE