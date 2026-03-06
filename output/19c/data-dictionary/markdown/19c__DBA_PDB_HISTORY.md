---
id: 19c__DBA_PDB_HISTORY
name: DBA_PDB_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PDB_HISTORY.html
---

# DBA_PDB_HISTORY

DBA_PDB_HISTORY describes the lineage of the PDB to which it belongs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PDB_NAME | VARCHAR2(128) | Name of this PDB in one of its incarnations |
| PDB_ID | NUMBER | Container ID of this PDB in one of its incarnations. |
| PDB_DBID | NUMBER | Database ID of this PDB in one of its incarnations |
| PDB_GUID | RAW(16) | Globally unique ID of this PDB in one of its incarnations |
| OP_SCNBAS | NUMBER | SCN base when an operation was performed on one of the incarnations of this PDB |
| OP_SCNWRP | NUMBER | SCN wrap when an operation was performed on one of incarnations of this PDB |
| OP_TIMESTAMP | DATE | Timestamp of an operation performed on one of the incarnations of this PDB |
| OPERATION | VARCHAR2(16) | Operation that was performed on one of the incarnations of this PDB |
| DB_VERSION | NUMBER | Database version |
| CLONED_FROM_PDB_NAME | VARCHAR2(128) | Name of a PDB from which one of the incarnations of this PDB was cloned |
| CLONED_FROM_PDB_DBID | NUMBER | Database ID of a PDB from which one of the incarnations of this PDB was cloned |
| CLONED_FROM_PDB_GUID | RAW(16) | Globally unique ID of a PDB from which one of the incarnations of this PDB was cloned |
| DB_NAME | VARCHAR2(128) | Name of a CDB in which one of the incarnations of this PDB was created |
| DB_UNIQUE_NAME | VARCHAR2(128) | Unique name of a CDB in which one of the incarnations of this PDB was created |
| DB_DBID | NUMBER | Database ID of a CDB in which one of the incarnations of this PDB was created |
| CLONETAG | VARCHAR2(128) | Clone tag name for the PDB if the PDB was cloned using the snapshot copy mechanism |
| DB_VERSION_STRING | VARCHAR2(204) | Database version string |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content