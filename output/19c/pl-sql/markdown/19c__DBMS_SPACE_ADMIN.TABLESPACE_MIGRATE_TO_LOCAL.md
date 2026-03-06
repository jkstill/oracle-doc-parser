---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL
name: DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL

This procedure migrates the tablespace from a dictionary-managed format to a locally managed format. Tablespaces migrated to locally managed format are user managed.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL (
   tablespace_name     IN     VARCHAR2,
   unit_size           IN     POSITIVE DEFAULT NULL,
   rfno                IN     POSITIVE DEFAULT NULL);
```

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL ( tablespace_name IN VARCHAR2, unit_size IN POSITIVE DEFAULT NULL, rfno IN POSITIVE DEFAULT NULL); Parameters Table 159-16 TABLESPACE_MIGRATE_TO_LOCAL Procedure Parameters Parameter Name Description tablespace_name Name of the tablespace to be migrated unit_size Bitmap unit size (which is the size of the smallest possible chunk of space that can be allocated) in the tablespace specified in number of blocks rfno Relative File Number of the file where the bitmap blocks are placed Usage Notes Before you migrate the SYSTEM tablespace, migrate any dictionary-managed tablespaces that you want to use in read/write mode to locally managed. After the SYSTEM tablespace is migrated, you cannot change dictionary-managed tablespaces to read/write. See Also: Oracle Database Administrator's Guide The tablespace must be kept online and read/write during migration. Note that temporary tablespaces cannot be migrated. Allocation Unit may be specified optionally. The default is calculated by the system based on the highest common divisor of all extents (used or free) for the tablespace. This number is further trimmed based on the MINIMUM EXTENT for the tablespace (5 if MINIMUM EXTENT is not specified). Thus, the calculated value will not be larger than the MINIMUM EXTENT for the tablespace. The last free extent in every file is ignored for GCD calculation. If you specify the unit size, then it must be a factor of the unit_size calculated by the system; otherwise an error message is returned. The Relative File Number parameter is used to place the bitmaps in a desired file. If space is not found in the file, then an error is issued. The data file specified must be part of the tablespace being migrated. If the dataflow is not specified, then the system chooses a dataflow in which to place the initial bitmap blocks. If space is not found for the initial bitmaps, then an error is raised. See Also: Oracle Database Administrator's Guide Examples To migrate a tablespace 'TS1' in 2KB blocksize with minimum extent size 1MB: EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL('TS1', 512, 2); The bitmaps are placed in file with relative file number 2.