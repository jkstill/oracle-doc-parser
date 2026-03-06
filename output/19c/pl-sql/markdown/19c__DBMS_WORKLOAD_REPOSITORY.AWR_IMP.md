---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_IMP
name: DBMS_WORKLOAD_REPOSITORY.AWR_IMP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_IMP

This procedure loads the AWR data from a dump file into the SYS schema.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_IMP(
   dmpfile              IN   VARCHAR2   DEFAULT 'awrdat',
   dmpdir               IN   VARCHAR2   DEFAULT 'DATA_PUMP_DIR',
   new_dbid             IN   NUMBER     DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dmpfile | VARCHAR2 | IN | The prefix for the name of the dump file and log file. This file will be the source of the imported AWR data. The default value is awrdat . |
| dmpdir | VARCHAR2 | IN | The name of the Directory Object for the file system directory where the load dump file is located. The default value is DATA_PUMP_DIR . |
| new_dbid | NUMBER | IN | The database ID to be used instead of existing database ID. |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_IMP( dmpfile IN VARCHAR2 DEFAULT 'awrdat', dmpdir IN VARCHAR2 DEFAULT 'DATA_PUMP_DIR', new_dbid IN NUMBER DEFAULT NULL); Parameters Table 192-20 AWR_IMP Procedure Parameters Parameter Description dmpfile The prefix for the name of the dump file and log file. This file will be the source of the imported AWR data. The default value is awrdat . dmpdir The name of the Directory Object for the file system directory where the load dump file is located. The default value is DATA_PUMP_DIR . new_dbid The database ID to be used instead of existing database ID.