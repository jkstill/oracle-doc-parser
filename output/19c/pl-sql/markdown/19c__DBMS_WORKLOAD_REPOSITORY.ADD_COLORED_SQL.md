---
id: 19c__DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL
name: DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL

This procedure adds a colored SQL ID.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL(
   sql_id         IN VARCHAR2,
   dbid           IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | 13-character external SQL ID |
| dbid | NUMBER | IN | Optional DBID, defaults to Local DBID |

## Usage Notes

If an SQL ID is colored, it will be captured in every snapshot, independent of its level of activities (so that it does not have to be a TOP SQL ). Capture occurs if the SQL is found in the cursor cache at snapshot time.To uncolor the SQL, invoke the REMOVE_COLORED_SQL Procedure . Syntax DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL( sql_id IN VARCHAR2, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-3 ADD_COLORED_SQL Procedure Parameters Parameter Description sql_id 13-character external SQL ID dbid Optional DBID, defaults to Local DBID