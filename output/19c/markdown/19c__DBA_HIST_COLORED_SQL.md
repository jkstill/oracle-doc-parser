---
id: 19c__DBA_HIST_COLORED_SQL
name: DBA_HIST_COLORED_SQL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_HIST_COLORED_SQL.html
---

# DBA_HIST_COLORED_SQL

DBA_HIST_COLORED_SQL displays the SQL IDs that have been marked for AWR SQL capture.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| SQL_ID | VARCHAR2(13) | SQL ID of colored SQL statement |
| CREATE_TIME | DATE | Time the SQL ID was colored |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

If a SQL statement is colored using the DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL procedure, then AWR will always capture the SQL statistics for the colored SQL ID. A SQL statement can be removed from coloring using the DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL procedure. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_WORKLOAD_REPOSITORY package. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_WORKLOAD_REPOSITORY package.