---
id: 19c__DBA_PDB_SAVED_STATES
name: DBA_PDB_SAVED_STATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_PDB_SAVED_STATES.html
---

# DBA_PDB_SAVED_STATES

DBA_PDB_SAVED_STATES shows information about the current saved PDB states in the CDB.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CON_ID | NUMBER | The ID of the PDB |
| CON_NAME | VARCHAR2(128) | Name of the PDB |
| INSTANCE_NAME | VARCHAR2(128) | Name of the instance for which the state is saved |
| CON_UID | NUMBER | Unique ID assigned to the PDB at creation time |
| GUID | RAW(16) | Globally unique immutable ID assigned to the PDB at creation time |
| STATE | VARCHAR2(14) | Open state of the PDB |
| RESTRICTED | VARCHAR2(3) | Restricted mode of the PDB |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is a data link, so the data is also available within the PDB. See Also: Oracle Database SQL Language Reference for more information about preserving a PDB's open mode across an instance restart See Also: Oracle Database SQL Language Reference for more information about preserving a PDB's open mode across an instance restart