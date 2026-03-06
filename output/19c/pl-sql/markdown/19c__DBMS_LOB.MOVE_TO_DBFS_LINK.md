---
id: 19c__DBMS_LOB.MOVE_TO_DBFS_LINK
name: DBMS_LOB.MOVE_TO_DBFS_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.MOVE_TO_DBFS_LINK

This procedure archives the specified LOB data (from the database) into the DBFS HSM Store.

## Syntax

```sql
DBMS_LOB.MOVE_TO_DBFS_LINK (
  lob_loc       IN OUT BLOB,
  storage_path  IN     VARCHAR2(dbfs_link_path_max_size),
  flags         IN     BINARY INTEGER DEFAULT DBFS_LINK_NOCACHE); 

DBMS_LOB.MOVE_TO_DBFS_LINK (
  lob_loc       IN OUT CLOB CHARACTER SET ANY_CS,
  storage_path  IN     VARCHAR2(dbfs_link_path_max_size),
  flags         IN     BINARY INTEGER DEFAULT DBFS_LINK_NOCACHE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB | IN OUT | LOB to be archived |
| storage_path | VARCHAR2(dbfs_link_path_max_size) | IN | Path where the LOB will be stored |
| flags | BINARY | IN | Either DBFS_LINK_CACHE or DBFS_LINK_NOCACHE . If DBFS_LINK_CACHE is specified, the LOB data continues to be stored in the RDBMS as well as being written to the DBFS store. DBFS_LINK_NOCACHE specifies that the LOB data should be deleted from the RDBMS once written to the DBFS. |

## Usage Notes

Syntax DBMS_LOB.MOVE_TO_DBFS_LINK ( lob_loc IN OUT BLOB, storage_path IN VARCHAR2(dbfs_link_path_max_size), flags IN BINARY INTEGER DEFAULT DBFS_LINK_NOCACHE); DBMS_LOB.MOVE_TO_DBFS_LINK ( lob_loc IN OUT CLOB CHARACTER SET ANY_CS, storage_path IN VARCHAR2(dbfs_link_path_max_size), flags IN BINARY INTEGER DEFAULT DBFS_LINK_NOCACHE); Parameters Table 99-83 MOVE_TO_DBFS_LINK Procedure Parameters Parameter Description lob_loc LOB to be archived storage_path Path where the LOB will be stored flags Either DBFS_LINK_CACHE or DBFS_LINK_NOCACHE . If DBFS_LINK_CACHE is specified, the LOB data continues to be stored in the RDBMS as well as being written to the DBFS store. DBFS_LINK_NOCACHE specifies that the LOB data should be deleted from the RDBMS once written to the DBFS. Exceptions Table 99-84 MOVE_TO_DBFS_LINK Procedure Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE Usage Notes If the LOB is already archived, the procedure silently returns as if the put was successful. In that case, if DBFS_LINK_NOCACHE is specified, or flags is defaulted, the LOB data is removed from the RDBMS. Calling this procedure multiple times on the same LOB with the same flags has no effect. Calling the procedure on a LOB that is already archived causes the LOB to be cached ( DBFS_LINK_CACHE ) or removed ( DBFS_LINK_NOCACHE ) according to the flag setting.