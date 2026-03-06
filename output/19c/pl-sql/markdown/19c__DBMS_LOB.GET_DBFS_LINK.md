---
id: 19c__DBMS_LOB.GET_DBFS_LINK
name: DBMS_LOB.GET_DBFS_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GET_DBFS_LINK

This function returns the DBFS path name for the specified SecureFile LOB.

## Syntax

```sql
DBMS_LOB.GET_DBFS_LINK (
  lob_loc             IN     BLOB,
  storage_path        OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE),
  lob_length          OUT NUMBER);

DBMS_LOB.GET_DBFS_LINK (
  lob_loc             IN     CLOB CHARACTER SET ANY_CS,
  storage_path        OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE),
  lob_length          OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | LOB to be retrieved from DBFS |
| storage_path | VARCHAR2(DBFS_LINK_PATH_MAX_SIZE) | OUT | Path where the LOB is stored in DBFS |
| lob_length | NUMBER) | OUT | LOB length at the time of write to DBFS |

## Usage Notes

Syntax DBMS_LOB.GET_DBFS_LINK ( lob_loc IN BLOB, storage_path OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE), lob_length OUT NUMBER); DBMS_LOB.GET_DBFS_LINK ( lob_loc IN CLOB CHARACTER SET ANY_CS, storage_path OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE), lob_length OUT NUMBER); Parameters Table 99-54 GET_DBFS_LINK Function Parameters Parameter Description lob_loc LOB to be retrieved from DBFS storage_path Path where the LOB is stored in DBFS lob_length LOB length at the time of write to DBFS Return Values The Archive ID Exceptions Table 99-55 GET_DBFS_LINK Function Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE ORA-01555 The LOB has already been retrieved and has been modified since retrieval or the LOB has been migrated in and out (modified or not) since the locator was retrieved