---
id: 19c__DBMS_LOB.COPY_FROM_DBFS_LINK
name: DBMS_LOB.COPY_FROM_DBFS_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.COPY_FROM_DBFS_LINK

This procedure retrieves the archived SecureFiles LOB data from the DBFS HSM store and to the database.

## Syntax

```sql
DBMS_LOB.COPY_FROM_DBFS_LINK (
  lob_loc       IN OUT BLOB);

DBMS_LOB.COPY_FROM_DBFS_LINK (
  lob_loc       IN OUT CLOB CHARACTER SET ANY_CS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN OUT | LOB to be retrieved from the archive |

## Usage Notes

Syntax DBMS_LOB.COPY_FROM_DBFS_LINK ( lob_loc IN OUT BLOB); DBMS_LOB.COPY_FROM_DBFS_LINK ( lob_loc IN OUT CLOB CHARACTER SET ANY_CS); Parameters Table 99-26 COPY_FROM_DBFS_LINK Procedure Parameters Parameter Description lob_loc LOB to be retrieved from the archive Usage Note COPY_FROM_DBFS_LINK does not remove the underlying DBFS file. If the LOB is successfully retrieved, COPY_FROM_DBFS_LINK silently returns success. Exceptions Table 99-27 COPY_FROM_DBFS_LINK Procedure Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE ORA-01555 If the LOB has already been retrieved and has been modified since retrieval, if the LOB has been migrated in and out (modified or not) since the locator was retrieved