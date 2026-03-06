---
id: 19c__DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_ANALYTICS
name: DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_ANALYTICS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_ANALYTICS

This function returns the ASH Analytics active report.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_ANALYTICS(
   dbid           IN NUMBER DEFAULT NULL,
   inst_id        IN NUMBER DEFAULT NULL,
   begin_time     IN DATE,
   end_time       IN DATE,
   report_level   IN VARCHAR2 DEFAULT NULL,
   filter_list    IN VARCHAR2 DEFAULT NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dbid | NUMBER | IN | Database identifier. If its value is set to NULL, then the database identifier for the local database is used. Its default value is NULL. |
| inst_id | NUMBER | IN | Instance number of the database for which the statistics are required. If its value is set to NULL, then the statistics for the local database are returned. Its default value is NULL. |
| begin_time | DATE | IN | The start time of the interval for which the ASH report is required. |
| end_time | DATE | IN | The end time of the interval for which the ASH report is required. |
| report_level | VARCHAR2 | IN | Describes the list of components to build. |
| filter_list | VARCHAR2 | IN | Describes the list of filters to apply. Its default value is NULL (no filters to apply). |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_ANALYTICS( dbid IN NUMBER DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, begin_time IN DATE, end_time IN DATE, report_level IN VARCHAR2 DEFAULT NULL, filter_list IN VARCHAR2 DEFAULT NULL) RETURN CLOB; Parameters Table 192-8 ASH_REPORT_ANALYTICS Parameters Parameter Description dbid Database identifier. If its value is set to NULL, then the database identifier for the local database is used. Its default value is NULL. inst_id Instance number of the database for which the statistics are required. If its value is set to NULL, then the statistics for the local database are returned. Its default value is NULL. begin_time The start time of the interval for which the ASH report is required. end_time The end time of the interval for which the ASH report is required. report_level Describes the list of components to build. filter_list Describes the list of filters to apply. Its default value is NULL (no filters to apply). Return Values Returns the ASH Analytics active report.