---
id: 19c__DBA_HIST_WR_SETTINGS
name: DBA_HIST_WR_SETTINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_WR_SETTINGS.html
---

# DBA_HIST_WR_SETTINGS

DBA_HIST_WR_SETTINGS displays the settings and metadata for the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOCAL_AWRDBID | NUMBER | Database ID of the local database |
| VIEW_LOCATION | VARCHAR2(8) | Data source of the DBA_HIST dictionary views. Possible values include: AWR_PDB : Views display AWR data stored in the PDB. AWR_ROOT : Views display AWR data stored in the root. |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |