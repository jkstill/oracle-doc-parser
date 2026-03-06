---
id: 19c__DBA_PDB_SNAPSHOTFILE
name: DBA_PDB_SNAPSHOTFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PDB_SNAPSHOTFILE.html
---

# DBA_PDB_SNAPSHOTFILE

DBA_PDB_SNAPSHOTFILE displays the files associated with snapshots taken of pluggable databases (PDBs).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER | The ID of the PDB |
| SNAPSHOT_SCN | NUMBER | SCN at which the snapshot was taken |
| SNAPSHOT_FILENAME | VARCHAR2(513) | Snapshot file name |
| SNAPSHOT_FILETYPE | VARCHAR2(8) | Snapshot file type. Possible values: ARCH : Archive log file DATA : Data file XML : XML file |

## Usage Notes

You can use this view in conjunction with the DBA_PDB_SNAPSHOT view. Join the SNAPSHOT_SCN column in this view with the SNAPSHOT_SCN column in DBA_PDB_SNAPSHOT to determine the files associated with a particular PDB snapshot. A PDB snapshot consists of an archive log file, one or more data files, and one or more XML files. A row is added to this view for each file associated with a PDB snapshot. Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: " DBA_PDB_SNAPSHOTS " Note: This view is available starting with Oracle Database release 19c, version 19.1. See Also: " DBA_PDB_SNAPSHOTS "