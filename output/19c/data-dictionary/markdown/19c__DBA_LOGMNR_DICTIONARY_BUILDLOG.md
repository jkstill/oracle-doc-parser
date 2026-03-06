---
id: 19c__DBA_LOGMNR_DICTIONARY_BUILDLOG
name: DBA_LOGMNR_DICTIONARY_BUILDLOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGMNR_DICTIONARY_BUILDLOG.html
---

# DBA_LOGMNR_DICTIONARY_BUILDLOG

DBA_LOGMNR_DICTIONARY_BUILDLOG describes all successful LogMiner dictionary builds available for GoldenGate REGISTER EXTRACT .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(384) | User-supplied name of the LogMiner dictionary build |
| DATE_OF_BUILD | VARCHAR2(20) | Date and time at which the LogMiner dictionary build was performed |
| START_SCN | NUMBER | Begin SCN of the LogMiner dictionary build operation |
| END_SCN | NUMBER | End SCN of the LogMiner dictionary build operation |
| BUILD_TYPE | VARCHAR2(20) | Internal string that identifies how the LogMiner dictionary build was initiated |
| BUILD_OP | NUMBER | Internal number that identifies how the LogMiner dictionary build was initiated |
| CONTAINER_ID | NUMBER | ID of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| CONTAINER_UID | NUMBER | Unique number that identifies the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| CONTAINER_NAME | VARCHAR2(384) | Name of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| RESETLOGS_CHANGE# | NUMBER | SCN that identifies the redo branch of the LogMiner dictionary build |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When this view is queried from a PDB, it returns only LogMiner dictionary builds performed in that PDB. Column Datatype NULL Description NAME VARCHAR2(384) User-supplied name of the LogMiner dictionary build DATE_OF_BUILD VARCHAR2(20) Date and time at which the LogMiner dictionary build was performed START_SCN NUMBER Begin SCN of the LogMiner dictionary build operation END_SCN NUMBER End SCN of the LogMiner dictionary build operation BUILD_TYPE VARCHAR2(20) Internal string that identifies how the LogMiner dictionary build was initiated BUILD_OP NUMBER Internal number that identifies how the LogMiner dictionary build was initiated CONTAINER_ID NUMBER ID of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) CONTAINER_UID NUMBER Unique number that identifies the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) CONTAINER_NAME VARCHAR2(384) Name of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) RESETLOGS_CHANGE# NUMBER SCN that identifies the redo branch of the LogMiner dictionary build Note: This view is available starting with Oracle Database release 19c, version 19.10. Note: This view is available starting with Oracle Database release 19c, version 19.10.