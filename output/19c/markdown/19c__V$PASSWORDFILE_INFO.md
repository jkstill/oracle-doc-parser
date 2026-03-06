---
id: 19c__V$PASSWORDFILE_INFO
name: V$PASSWORDFILE_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PASSWORDFILE_INFO.html
---

# V$PASSWORDFILE_INFO

V$PASSWORDFILE_INFO provides information about the database password file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NAME | VARCHAR2(513) |  |
| FORMAT | VARCHAR2(6) |  |
| IS_ASM | VARCHAR2(5) |  |
| CON_ID | NUMBER |  |

## Usage Notes

This view can be queried from the root or from a pluggable database (PDB) in a multitenant container database (CDB). When queried, this view always returns one row. Note: If the database password file name or location was recently changed, and you do not see the change reflected in this view, you can run the following SQL statement: SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE; This statement flushes the metadata cache and updates the database to use the new password file. It also updates this view with the current password file information. Note: If the database password file name or location was recently changed, and you do not see the change reflected in this view, you can run the following SQL statement: SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE; This statement flushes the metadata cache and updates the database to use the new password file. It also updates this view with the current password file information.