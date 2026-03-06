---
id: 19c__USER_DBFS_HS_FILES
name: USER_DBFS_HS_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_DBFS_HS_FILES.html
---

# USER_DBFS_HS_FILES

USER_DBFS_HS_FILES displays files in the Database File System (DBFS) hierarchical store owned by the current user and their location on the back-end device.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PATH | VARCHAR2(1024) | Path name of the file |
| SEQUENCENUMBER | NUMBER | Sequence number of this piece of the file |
| STARTOFFSET | NUMBER | Begin offset of this piece in the tarball |
| ENDOFFSET | NUMBER | End offset of this piece in the tarball |
| TARBALLID | NUMBER | Tarball ID |
| BACKUPFILENAME | VARCHAR2(256) | File on back end in which this tarball is located |
| TARSTARTOFFSET | NUMBER | Begin offset of this tarball in the backup file |
| TARENDOFFSET | NUMBER | End offset of this tarball in the backup file |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content