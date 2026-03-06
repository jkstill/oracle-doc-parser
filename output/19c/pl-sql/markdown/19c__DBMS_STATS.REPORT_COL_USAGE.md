---
id: 19c__DBMS_STATS.REPORT_COL_USAGE
name: DBMS_STATS.REPORT_COL_USAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REPORT_COL_USAGE

This function reports the recorded column (group) usage information.

## Syntax

```sql
DBMS_STATS.REPORT_COL_USAGE (
   ownname    IN    VARCHAR2,
   tabname    IN    VARCHAR2)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name. If NULL it reports column usage information for tables in all schemas in the database. |
| tabname | VARCHAR2) | IN | Table name. If NULL it reports column usage information for all tables of ownname . |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_STATS.REPORT_COL_USAGE ( ownname IN VARCHAR2, tabname IN VARCHAR2) RETURN CLOB; Parameters Table 171-99 REPORT_COL_USAGE Function Parameters Parameter Description ownname Owner name. If NULL it reports column usage information for tables in all schemas in the database. tabname Table name. If NULL it reports column usage information for all tables of ownname . Usage Notes To run this procedure, you need to have the SYSDBA administrative privilege or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privileges.