---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS
name: DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS

This procedure rebuilds the appropriate bitmaps. If no bitmap block is specified, then it rebuilds all bitmaps for the given tablespace.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS (
   tablespace_name         IN    VARCHAR2,
   bitmap_relative_file    IN    POSITIVE   DEFAULT NULL,
   bitmap_block            IN    POSITIVE   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace |
| bitmap_relative_file | POSITIVE | IN | Relative file number of bitmap block to rebuild |
| bitmap_block | POSITIVE | IN | Block number of bitmap block to rebuild |

## Usage Notes

The procedure cannot be used on the SYSTEM tablespace. Syntax DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS ( tablespace_name IN VARCHAR2, bitmap_relative_file IN POSITIVE DEFAULT NULL, bitmap_block IN POSITIVE DEFAULT NULL); Parameters Table 159-17 TABLESPACE_REBUILD_BITMAPS Procedure Parameters Parameter Description tablespace_name Name of tablespace bitmap_relative_file Relative file number of bitmap block to rebuild bitmap_block Block number of bitmap block to rebuild Usage Notes Only full rebuild is supported. Examples The following example rebuilds bitmaps for all the files in the USERS tablespace. EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_BITMAPS('USERS');