---
id: 19c__DBMS_STATS.MERGE_COL_USAGE
name: DBMS_STATS.MERGE_COL_USAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.MERGE_COL_USAGE

This procedure merges column usage information from a source database by means of a dblink into the local database.

## Syntax

```sql
DBMS_STATS.MERGE_COL_USAGE (
   dblink    IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dblink | VARCHAR2) | IN | Name of dblink |

## Usage Notes

Syntax If column usage information already exists for a given table or column MERGE_COL_USAGE will combine both the local and the remote information. DBMS_STATS.MERGE_COL_USAGE ( dblink IN VARCHAR2); Parameters Table 171-86 MERGE_COL_USAGE Procedure Parameters Parameter Description dblink Name of dblink Usage Notes User must be SYS to execute this procedure. addition the user specified during the creation of the dblink is expected to have privileges to select from tables in the SYS schema. Exceptions ORA-20000 : Insufficient privileges ORA-20001 : Parameter dblink cannot be NULL ORA-20002 : Unable to create a TEMP table