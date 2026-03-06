---
id: 19c__DBA_APP_PDB_STATUS
name: DBA_APP_PDB_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_APP_PDB_STATUS.html
---

# DBA_APP_PDB_STATUS

DBA_APP_PDB_STATUS provides information about applications in all the application PDBs in the current application container. It provides this information when queried in the application root.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_UID | NUMBER | Unique ID of the PDB |
| APP_NAME | VARCHAR2(128) | Name of the application |
| APP_ID | NUMBER | Id of the application |
| APP_VERSION | VARCHAR2(30) | Version of the application |
| APP_STATUS | VARCHAR2(12) | Status of the application |

## Usage Notes

The view should be queried in the application root. This view can be used to show which version of an application has been synced to which application PDBs.