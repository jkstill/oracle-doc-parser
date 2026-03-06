---
id: 19c__DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL
name: DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL

This procedure removes a colored SQL ID. After a SQL is uncolored, it will no longer be captured in a snapshot automatically, unless it makes the TOP list.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL(
   sql_id         IN VARCHAR2,
   dbid           IN NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | 13-character external SQL ID |
| dbid | NUMBER | IN | Optional dbid, defaults to Local DBID |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL( sql_id IN VARCHAR2, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-38 REMOVE_COLORED_SQL Procedure Parameters Parameter Description sql_id 13-character external SQL ID dbid Optional dbid, defaults to Local DBID