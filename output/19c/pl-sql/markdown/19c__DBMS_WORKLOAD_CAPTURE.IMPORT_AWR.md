---
id: 19c__DBMS_WORKLOAD_CAPTURE.IMPORT_AWR
name: DBMS_WORKLOAD_CAPTURE.IMPORT_AWR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.IMPORT_AWR

This procedure imports the AWR snapshots associated with a given capture ID provided those AWR snapshots were exported earlier from the original capture system using the EXPORT_AWR procedure.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.IMPORT_AWR (
   capture_id       IN   NUMBER,
   staging_schema   IN   VARCHAR2,
   force_cleanup    IN   BOOLEAN DEFAULT FALSE)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| capture_id | NUMBER | IN | ID of the capture whose AWR snapshots should be imported. (Mandatory) |
| staging_schema | VARCHAR2 | IN | Name of a valid schema in the current database which can be used as a staging area while importing the AWR snapshots from the capture directory to the SYS AWR schema.The SYS schema is not a valid input. (Mandatory, Case sensitive). |
| force_cleanup | BOOLEAN | IN | Values: TRUE - any AWR data present in the given staging_schema are removed before the actual import operation. All tables with names that match any of the tables in AWR are dropped before the actual import. This typically is equivalent to dropping all tables returned by the following SQL: SELECT table_name FROM dba_tables WHERE owner = staging_schema AND table_name like 'WR_$%'; Use this option only if you are sure that there are no important data in any such tables in the staging_schema . FALSE - (default) no tables dropped from the staging_schema prior to the import operation |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.IMPORT_AWR ( capture_id IN NUMBER, staging_schema IN VARCHAR2, force_cleanup IN BOOLEAN DEFAULT FALSE) RETURN NUMBER; Parameters Table 190-10 IMPORT_AWR Function Parameters Parameter Description capture_id ID of the capture whose AWR snapshots should be imported. (Mandatory) staging_schema Name of a valid schema in the current database which can be used as a staging area while importing the AWR snapshots from the capture directory to the SYS AWR schema.The SYS schema is not a valid input. (Mandatory, Case sensitive). force_cleanup Values: TRUE - any AWR data present in the given staging_schema are removed before the actual import operation. All tables with names that match any of the tables in AWR are dropped before the actual import. This typically is equivalent to dropping all tables returned by the following SQL: SELECT table_name FROM dba_tables WHERE owner = staging_schema AND table_name like 'WR_$%'; Use this option only if you are sure that there are no important data in any such tables in the staging_schema . FALSE - (default) no tables dropped from the staging_schema prior to the import operation Return Values Returns the new randomly generated database ID that was used to import the AWR snapshots. The same value can be found in the AWR_DBID column in the DBA_WORKLOAD_CAPTURES view. Usage Notes IMPORT_AWR fails if the staging_schema provided as input contains any tables with the same name as any of the AWR tables, such as WRM$_SNAPSHOT or WRH$_PARAMETER . Please drop any such tables in the staging_schema before invoking IMPORT_AWR .