---
id: 19c__DBMS_WORKLOAD_REPOSITORY.UPDATE_DATAFILE_INFO
name: DBMS_WORKLOAD_REPOSITORY.UPDATE_DATAFILE_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.UPDATE_DATAFILE_INFO

This procedure updates the data file and tablespace information stored in the Automatic Workload Repository (AWR) with the current information in the database. This procedure is useful when a data file or a tablespace has been moved or renamed. As this change is not always captured in the next snapshot, AWR report may not show the most current information.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.UPDATE_DATAFILE_INFO();
```

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.UPDATE_DATAFILE_INFO();