---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS
name: DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS

This procedure marks the appropriate block range (extent) as free or used in bitmap. It cannot be used on the SYSTEM tablespace.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS (
   tablespace_name         IN    VARCHAR2,
   dbarange_relative_file  IN    POSITIVE,
   dbarange_begin_block    IN    POSITIVE,
   dbarange_end_block      IN    POSITIVE,
   fix_option              IN    POSITIVE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace |
| dbarange_relative_file | POSITIVE | IN | Relative file number of block range (extent) |
| dbarange_begin_block | POSITIVE | IN | Block number of beginning of extent |
| dbarange_end_block | POSITIVE | IN | Block number (inclusive) of end of extent |
| fix_option | POSITIVE) | IN | One of the following options: TABLESPACE_EXTENT_MAKE_FREE TABLESPACE_EXTENT_MAKE_USED |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS ( tablespace_name IN VARCHAR2, dbarange_relative_file IN POSITIVE, dbarange_begin_block IN POSITIVE, dbarange_end_block IN POSITIVE, fix_option IN POSITIVE); Parameters Table 159-13 TABLESPACE_FIX_BITMAPS Procedure Parameters Parameter Description tablespace_name Name of tablespace dbarange_relative_file Relative file number of block range (extent) dbarange_begin_block Block number of beginning of extent dbarange_end_block Block number (inclusive) of end of extent fix_option One of the following options: TABLESPACE_EXTENT_MAKE_FREE TABLESPACE_EXTENT_MAKE_USED Examples The following example marks bits for 51 blocks for relative file number 4, beginning at block number 33 and ending at 83, as USED in bitmaps. EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_FIX_BITMAPS('USERS', 4, 33, 83, DBMS_SPACE_ADMIN.EXTENT_MAKE_USED); Alternatively, specifying an option of TABLESPACE_EXTENT_MAKE_FREE marks the bits free in bitmaps. The BEGIN and END blocks must be in extent boundary and be extent multiple; otherwise, an error is raised.