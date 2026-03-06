---
id: 19c__DBMS_STATS.SEED_COL_USAGE
name: DBMS_STATS.SEED_COL_USAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SEED_COL_USAGE

This procedure seeds column usage information from a statements in the specified SQL tuning set, or in the database.

## Syntax

```sql
DBMS_STATS.SEED_COL_USAGE (
   sqlset_name    IN    VARCHAR2,
   owner_name     IN    VARCHAR2,
   time_limit     IN    POSITIVE DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Name of the SQL tuning set that contains the statements to be monitored. If this parameter and owner_name are both null, then the procedure monitors all statements in the database for the specified time limit. |
| owner_name | VARCHAR2 | IN | Owner of the SQL tuning set that contains the statements to be monitored. If this parameter and sqlset_name are both null, then the procedure monitors all statements in the database for the specified time limit. |
| time_limit | POSITIVE | IN | Time limit (in seconds). |

## Usage Notes

The procedure iterates over the SQL statements, compiles them, and then seeds column usage information for the columns that appear in these statements. You can monitor the workload on the system for given amount of time and seed the and seed the column usage information based on the columns that appear in statements executed during the monitoring window. Syntax DBMS_STATS.SEED_COL_USAGE ( sqlset_name IN VARCHAR2, owner_name IN VARCHAR2, time_limit IN POSITIVE DEFAULT NULL); Parameters Table 171-118 SEED_COL_USAGE Procedure Parameters Parameter Description sqlset_name Name of the SQL tuning set that contains the statements to be monitored. If this parameter and owner_name are both null, then the procedure monitors all statements in the database for the specified time limit. owner_name Owner of the SQL tuning set that contains the statements to be monitored. If this parameter and sqlset_name are both null, then the procedure monitors all statements in the database for the specified time limit. time_limit Time limit (in seconds). Security Model To invoke this procedure you must have the ANALYZE ANY privilege and the ANALYZE ANY DICTIONARY privilege. Exceptions ORA-20000 : Insufficient privileges