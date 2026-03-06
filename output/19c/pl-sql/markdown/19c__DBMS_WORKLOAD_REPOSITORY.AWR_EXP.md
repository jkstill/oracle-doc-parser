---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_EXP
name: DBMS_WORKLOAD_REPOSITORY.AWR_EXP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_EXP

This procedure extracts AWR data from the AWR schema and dump the information into a file. You can specify the snapshot range for the data that you want to extract.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_EXP(
   dmpfile              IN   VARCHAR2   DEFAULT 'awrdat',
   dmpdir               IN   VARCHAR2   DEFAULT 'DATA_PUMP_DIR',
   dbid                 IN   NUMBER     DEFAULT NULL,
   bid                  IN   NUMBER     DEFAULT 1,
   eid                  IN   NUMBER     DEFAULT 1000000);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dmpfile | VARCHAR2 | IN | The prefix for the name of the extract dump file and log file. The name of the dump file where all the data from the AWR table will be written is dmpfile.dmp. The dmpfile.log log file shows the status of the export job. The default value for the prefix is awrdat . |
| dmpdir | VARCHAR2 | IN | Name of the Directory Object for the file system directory where the extract dump file will be written. The list of Directory Objects can be queried using the DBA_DIRECTORIES view, and a new directory object can be created using the following command: create directory dmpdir as '/directory/path' . The default value is DATA_PUMP_DIR . |
| dbid | NUMBER | IN | The database ID for the snapshots that you want to export. The default value is NULL , for the local database ID. |
| bid | NUMBER | IN | The begin snapshot ID for snapshots to be exported. The default value is 1 . |
| eid | NUMBER | IN | The end Snapshot Id for snapshots to be exported. The default value is 10000000 . |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_EXP( dmpfile IN VARCHAR2 DEFAULT 'awrdat', dmpdir IN VARCHAR2 DEFAULT 'DATA_PUMP_DIR', dbid IN NUMBER DEFAULT NULL, bid IN NUMBER DEFAULT 1, eid IN NUMBER DEFAULT 1000000); Parameters Table 192-15 AWR_EXP Procedure Parameters Parameter Description dmpfile The prefix for the name of the extract dump file and log file. The name of the dump file where all the data from the AWR table will be written is dmpfile.dmp. The dmpfile.log log file shows the status of the export job. The default value for the prefix is awrdat . dmpdir Name of the Directory Object for the file system directory where the extract dump file will be written. The list of Directory Objects can be queried using the DBA_DIRECTORIES view, and a new directory object can be created using the following command: create directory dmpdir as '/directory/path' . The default value is DATA_PUMP_DIR . dbid The database ID for the snapshots that you want to export. The default value is NULL , for the local database ID. bid The begin snapshot ID for snapshots to be exported. The default value is 1 . eid The end Snapshot Id for snapshots to be exported. The default value is 10000000 .