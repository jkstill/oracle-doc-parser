---
id: 19c__DBA_ORPHAN_KEY_TABLE
name: DBA_ORPHAN_KEY_TABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_ORPHAN_KEY_TABLE.html
---

# DBA_ORPHAN_KEY_TABLE

DBA_ORPHAN_KEY_TABLE reports key values from indexes where the underlying base table has block corruptions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA_NAME | VARCHAR2(128) | Schema name of the index |
| INDEX_NAME | VARCHAR2(128) | Name of the index |
| IPART_NAME | VARCHAR2(128) | Name of the index partition or subpartition |
| INDEX_ID | NUMBER | Dictionary object ID of the index |
| TABLE_NAME | VARCHAR2(128) | Name of the base table of the index |
| PART_NAME | VARCHAR2(128) | Name of the base table partition or subpartition |
| TABLE_ID | NUMBER | Dictionary object ID of the base table |
| KEYROWID | ROWID | Physical rowid of the corrupt data row |
| KEY | ROWID | Key values for the index entry |
| DUMP_TIMESTAMP | DATE | Timestamp when the entry was made into the orphan key table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content To create the view, run the DBMS_REPAIR . ADMIN_TABLES procedure. To populate the orphan key table for an index, run the DBMS_REPAIR . DUMP_ORPHAN_KEYS procedure on the index. For each key in the index that points to a corrupt data block, Oracle inserts a row into the orphan key table.