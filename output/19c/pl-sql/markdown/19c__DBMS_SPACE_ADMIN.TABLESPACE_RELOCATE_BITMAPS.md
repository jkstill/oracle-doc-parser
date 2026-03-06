---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS
name: DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS

This procedure relocates the bitmaps to the destination specified.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS (
   tablespace_name    IN      VARCHAR2,
   filno              IN      POSITIVE,
   blkno              IN      POSITIVE);
```

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS ( tablespace_name IN VARCHAR2, filno IN POSITIVE, blkno IN POSITIVE); Parameters Table 159-19 TABLESPACE_RELOCATE_BITMAPS Procedure Parameters Parameter Name Description tablespace_name Name of tablespace filno Relative File Number of the destination file blkno Block Number of the destination range Usage Notes Migration of a tablespace from dictionary-managed to locally managed format could result in the creation of SPACE HEADER segment that contains the bitmap blocks. The SPACE HEADER segment is treated as user data. If you explicitly resize a file at or below the space header segment, then an error is issued. Use the TABLESPACE_RELOCATE_BITMAPS command to move the control information to a different destination and then resize the file. This procedure cannot be used on the SYSTEM tablespace. The tablespace must be kept online and read/write during relocation of bitmaps. This can be done only on migrated locally managed tablespaces. Examples EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_RELOCATE_BITMAPS('TS1', 3, 4); Moves the bitmaps to file 3, block 4. Note: The source and the destination addresses must not overlap. The destination block number is rounded down to the unit boundary. If there is user data in that location, then an error is raised. Note: The source and the destination addresses must not overlap. The destination block number is rounded down to the unit boundary. If there is user data in that location, then an error is raised.