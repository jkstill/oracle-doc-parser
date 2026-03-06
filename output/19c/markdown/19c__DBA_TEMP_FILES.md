---
id: 19c__DBA_TEMP_FILES
name: DBA_TEMP_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TEMP_FILES.html
---

# DBA_TEMP_FILES

DBA_TEMP_FILES describes all temporary files (tempfiles) in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NAME | VARCHAR2(513) | Name of the database temp file |
| FILE_ID | NUMBER | File identifier number of the database temp file |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace to which the file belongs |
| BYTES | NUMBER | Size of the file (in bytes) |
| BLOCKS | NUMBER | Size of the file (in Oracle blocks) |
| STATUS | VARCHAR2(7) | File status: OFFLINE ONLINE UNKNOWN |
| RELATIVE_FNO | NUMBER | Tablespace-relative file number |
| AUTOEXTENSIBLE | VARCHAR2(3) | Indicates whether the file is autoextensible ( YES ) or not ( NO ) |
| MAXBYTES | NUMBER | maximum size of the file (in bytes) |
| MAXBLOCKS | NUMBER | Maximum size of the file (in Oracle blocks) |
| INCREMENT_BY | NUMBER | Default increment for autoextension (in Oracle blocks) |
| USER_BYTES | NUMBER | Size of the useful portion of the file (in bytes) |
| USER_BLOCKS | NUMBER | Size of the useful portion of the file (in Oracle blocks) |
| SHARED | VARCHAR2(12) | Type of tablespace this file belongs to: SHARED : For shared tablespace LOCAL_FOR_RIM : Local temporary tablespace for RIM (read-only) instances LOCAL_FOR_ALL : Local temporary tablespace for all instance types |
| INST_ID | NUMBER | Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared tablespaces. |