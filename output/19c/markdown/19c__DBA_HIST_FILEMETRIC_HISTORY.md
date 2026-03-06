---
id: 19c__DBA_HIST_FILEMETRIC_HISTORY
name: DBA_HIST_FILEMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_FILEMETRIC_HISTORY.html
---

# DBA_HIST_FILEMETRIC_HISTORY

DBA_HIST_FILEMETRIC_HISTORY displays the history of file metrics collected in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| FILEID | NUMBER | File number |
| CREATIONTIME | NUMBER | File creation time |
| BEGIN_TIME | DATE | Begin time of the interval |
| END_TIME | DATE | End time of the interval |
| INTSIZE | NUMBER | Interval size (in hundredths of a second) |
| GROUP_ID | NUMBER | ID of the group to which the file belongs |
| AVGREADTIME | NUMBER | Average file read time |
| AVGWRITETIME | NUMBER | Average file write time |
| PHYSICALREAD | NUMBER | Number of physical reads |
| PHYSICALWRITE | NUMBER | Number of physical writes |
| PHYBLKREAD | NUMBER | Number of physical block reads |
| PHYBLKWRITE | NUMBER | Number of physical block writes |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |