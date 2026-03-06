---
id: 19c__DBA_PDB_SNAPSHOTS
name: DBA_PDB_SNAPSHOTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PDB_SNAPSHOTS.html
---

# DBA_PDB_SNAPSHOTS

DBA_PDB_SNAPSHOTS describes the snapshots taken of pluggable databases (PDBs).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER | The ID of the PDB |
| CON_UID | NUMBER | Unique ID assigned to the PDB at creation time |
| CON_NAME | VARCHAR2(128) | Name of the PDB |
| SNAPSHOT_NAME | VARCHAR2(128) | Snapshot name of the PDB |
| SNAPSHOT_SCN | NUMBER | SCN at which the snapshot was taken |
| PREVIOUS_SNAPSHOT_SCN | NUMBER | SCN at which the previous snapshot for the PDB was taken |
| SNAPSHOT_TIME | NUMBER | Timestamp at which the snapshot was taken |
| PREVIOUS_SNAPSHOT_TIME | NUMBER | Timestamp of the previous snapshot for this PDB |
| FULL_SNAPSHOT_PATH | VARCHAR2(4000) | Full path for the snapshot |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Rows are added to this view when a snapshot of a PDB is taken by using the ALTER PLUGGABLE DATABASE SNAPSHOT SQL statement. Note: This view does not display snapshot copy PDBs, which are created by using the CREATE PLUGGABLE DATABASE ... SNAPSHOT COPY SQL statement. See Also: " DBA_PDB_SNAPSHOTFILE " for information about the files associated with a particular PDB snapshot Note: This view does not display snapshot copy PDBs, which are created by using the CREATE PLUGGABLE DATABASE ... SNAPSHOT COPY SQL statement. See Also: " DBA_PDB_SNAPSHOTFILE " for information about the files associated with a particular PDB snapshot