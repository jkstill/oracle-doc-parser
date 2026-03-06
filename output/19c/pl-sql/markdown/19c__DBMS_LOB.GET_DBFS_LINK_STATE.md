---
id: 19c__DBMS_LOB.GET_DBFS_LINK_STATE
name: DBMS_LOB.GET_DBFS_LINK_STATE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GET_DBFS_LINK_STATE

GET_DBFS_LINK_STATE retrieves the current link state of the specified SecureFile.

## Syntax

```sql
DBMS_LOB.GET_DBFS_LINK_STATE (
  lob_loc       IN BLOB,
  storage_path  OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE),
  state         OUT NUMBER,
  cached        OUT BOOLEAN);

DBMS_LOB.GET_DBFS_LINK_STATE (
  lob_loc       IN CLOB CHARACTER SET ANY_CS,
  storage_path  OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE),
  state         OUT NUMBER,
  cached        OUT BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN | LOB to be retrieved from the archive |
| storage_path | VARCHAR2(DBFS_LINK_PATH_MAX_SIZE) | OUT | Path where the LOB is stored in the DBFS HSM store |
| state | NUMBER | OUT | One of DBFS_LINK_NEVER , DBFS_LINK_NO or DBFS_LINK_YES |
| cached | BOOLEAN) | OUT | If the LOB is archived and the data was specified to be cashed on put |

## Usage Notes

Syntax DBMS_LOB.GET_DBFS_LINK_STATE ( lob_loc IN BLOB, storage_path OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE), state OUT NUMBER, cached OUT BOOLEAN); DBMS_LOB.GET_DBFS_LINK_STATE ( lob_loc IN CLOB CHARACTER SET ANY_CS, storage_path OUT VARCHAR2(DBFS_LINK_PATH_MAX_SIZE), state OUT NUMBER, cached OUT BOOLEAN); Parameters Table 99-56 GET_DBFS_LINK_STATE Procedure Parameters Parameter Description lob_loc LOB to be retrieved from the archive storage_path Path where the LOB is stored in the DBFS HSM store state One of DBFS_LINK_NEVER , DBFS_LINK_NO or DBFS_LINK_YES cached If the LOB is archived and the data was specified to be cashed on put Exceptions Table 99-57 GET_DBFS_LINK_STATE Procedure Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE Usage Notes If the LOB has never been archived, state is set to DBMS_LOB . DBFS_LINK_NEVER . If the LOB has been archived, state is set to DBMS_LOB . DBFS_LINK_YES . If the LOB has been previously retrieved from the archive, state is set to DBFS_LINK_NO . If the LOB was archived, but the data was left in the RDBMS, cached is set to TRUE . If the data was removed after the link was created, cached is set to FALSE , and NULL if state is DBMS_LOB . DBFS_LINK_NEVER .