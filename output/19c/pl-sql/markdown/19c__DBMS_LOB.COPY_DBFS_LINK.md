---
id: 19c__DBMS_LOB.COPY_DBFS_LINK
name: DBMS_LOB.COPY_DBFS_LINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.COPY_DBFS_LINK

This procedure copies the DBFS Link in the source LOB to the destination LOB.

## Syntax

```sql
DBMS_LOB.COPY_DBFS_LINK (
  lob_loc_dst    IN OUT BLOB,
  lob_loc_src    IN     BLOB,
  flags          IN     PLS_INTEGER DEFAULT DBFS_LINK_NOCACHE);

DBMS_LOB.COPY_DBFS_LINK (
  lob_loc_dst    IN OUT CLOB CHARACTER SET ANY_CS,
  lob_loc_src    IN     CLOB CHARACTER SET ANY_CS,
  flags          IN     PLS_INTEGER DEFAULT DBFS_LINK_NOCACHE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc_dst | BLOB | IN OUT | LOB to be made to reference the same storage data as lob_loc_src |
| lob_loc_src | BLOB | IN | LOB from which to copy the reference |
| flags | PLS_INTEGER | IN | Options to COPY_DBFS_LINK : DBFS_LINK_NOCACHE specifies to only copy the DBFS Link DBFS_LINK_CACHE specifies to copy the DBFS Link and read the data into the database LOB specified by lob_loc_dst so that the data is cached |

## Usage Notes

Syntax DBMS_LOB.COPY_DBFS_LINK ( lob_loc_dst IN OUT BLOB, lob_loc_src IN BLOB, flags IN PLS_INTEGER DEFAULT DBFS_LINK_NOCACHE); DBMS_LOB.COPY_DBFS_LINK ( lob_loc_dst IN OUT CLOB CHARACTER SET ANY_CS, lob_loc_src IN CLOB CHARACTER SET ANY_CS, flags IN PLS_INTEGER DEFAULT DBFS_LINK_NOCACHE); Parameters Table 99-24 COPY_DBFS_LINK Procedure Parameters Parameter Description lob_loc_dst LOB to be made to reference the same storage data as lob_loc_src lob_loc_src LOB from which to copy the reference flags Options to COPY_DBFS_LINK : DBFS_LINK_NOCACHE specifies to only copy the DBFS Link DBFS_LINK_CACHE specifies to copy the DBFS Link and read the data into the database LOB specified by lob_loc_dst so that the data is cached Exceptions Table 99-25 COPY_DBFS_LINK Procedure Exceptions Exception Description SECUREFILE_BADLOB Either lob_loc_src or lob_loc_dst is not a SECUREFILE INVALID_ARGVAL lob_loc_src LOB has not been archived ORA-01555 If the source LOB has been retrieved, never archived, or if the LOB has been migrated in and out (modified or not) since the locator was gotten.