---
id: 19c__DBMS_WORKLOAD_REPOSITORY.UPDATE_OBJECT_INFO
name: DBMS_WORKLOAD_REPOSITORY.UPDATE_OBJECT_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.UPDATE_OBJECT_INFO

This procedure updates rows of WRH$_SEG_STAT_OBJ table that represent objects in the local database. It attempts to determine the current names for all object belonging to the local database, except those with 'MISSING' and/or 'TRANSIENT' values in the name columns.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.UPDATE_OBJECT_INFO(
   maxrows   IN  NUMBER  DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| maxrows | NUMBER | IN | Maximum number of rows to be updated. Default= 0 , meaning there is no limit. |

## Usage Notes

The amount of work performed at each invocation of this routine may be controlled by setting the input parameter. Syntax DBMS_WORKLOAD_REPOSITORY.UPDATE_OBJECT_INFO( maxrows IN NUMBER DEFAULT 0); Parameters Table 192-43 UPDATE_OBJECT_INFO Procedure Parameters Parameter Description maxrows Maximum number of rows to be updated. Default= 0 , meaning there is no limit.