---
id: 19c__DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE
name: DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE

This function and procedure creates a baseline.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE(
   start_snap_id    IN  NUMBER,
   end_snap_id      IN  NUMBER,
   baseline_name    IN  VARCHAR2,
   dbid             IN  NUMBER DEFAULT NULL,
   expiration       IN  NUMBER DEFAULT NULL);

DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE(
   start_snap_id    IN  NUMBER,
   end_snap_id      IN  NUMBER,
   baseline_name    IN  VARCHAR2,
   dbid             IN  NUMBER DEFAULT NULL,
   expiration       IN  NUMBER DEFAULT NULL)
 RETURN NUMBER;

DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE(
   start_time       IN  DATE,
   end_time         IN  DATE,
   baseline_name    IN  VARCHAR2,
   dbid             IN  NUMBER DEFAULT NULL,
   expiration       IN  NUMBER DEFAULT NULL);

DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE(
   start_time       IN  DATE,
   end_time         IN  DATE,
   baseline_name    IN  VARCHAR2,
   dbid             IN  NUMBER DEFAULT NULL,
   expiration       IN  NUMBER DEFAULT NULL);
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| start_snap_id | NUMBER | IN | Start snapshot sequence number for the baseline. |
| end_snap_id | NUMBER | IN | End snapshot sequence number for the baseline. |
| start_time | DATE | IN | Start time for the baseline. |
| end_time | DATE | IN | End time for the baseline. |
| baseline_name | VARCHAR2 | IN | Name of baseline. |
| dbid | NUMBER | IN | Database Identifier for baseline. If NULL , this takes the database identifier for the local database. Defaults to NULL . |
| expiration | NUMBER | IN | Expiration in number of days for the baseline. If NULL , then expiration is infinite, meaning do not drop baseline ever. Defaults to NULL . |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE( start_snap_id IN NUMBER, end_snap_id IN NUMBER, baseline_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL, expiration IN NUMBER DEFAULT NULL); DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE( start_snap_id IN NUMBER, end_snap_id IN NUMBER, baseline_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL, expiration IN NUMBER DEFAULT NULL) RETURN NUMBER; DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE( start_time IN DATE, end_time IN DATE, baseline_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL, expiration IN NUMBER DEFAULT NULL); DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE( start_time IN DATE, end_time IN DATE, baseline_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL, expiration IN NUMBER DEFAULT NULL); RETURN NUMBER; Parameters Table 192-27 CREATE_BASELINE Function & Procedure Parameters Parameter Description start_snap_id Start snapshot sequence number for the baseline. end_snap_id End snapshot sequence number for the baseline. start_time Start time for the baseline. end_time End time for the baseline. baseline_name Name of baseline. dbid Database Identifier for baseline. If NULL , this takes the database identifier for the local database. Defaults to NULL . expiration Expiration in number of days for the baseline. If NULL , then expiration is infinite, meaning do not drop baseline ever. Defaults to NULL . Exceptions An error will be returned if this baseline name already exists in the system. The snapshot range that is specified for this interface must be an existing pair of snapshots in the database. An error will be returned if the inputted snapshots do not exist in the system. Examples This example creates a baseline (named ' oltp_peakload_bl ') between snapshots 105 and 107 for the local database: EXECUTE DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE (start_snap_id => 105, end_snap_id => 107, baseline_name => 'oltp_peakload_bl'); If you query the DBA_HIST_BASELINE view after the CREATE BASELINE action, you will see the newly created baseline in the Workload Repository.