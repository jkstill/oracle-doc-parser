---
id: 19c__DBMS_STATS.RESET_COL_USAGE
name: DBMS_STATS.RESET_COL_USAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.RESET_COL_USAGE

This procedure deletes the recorded column (group) usage information.

## Syntax

```sql
DBMS_STATS.RESET_COL_USAGE (
   ownname    IN    VARCHAR2,
   tabname    IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name. If NULL it deletes column usage information for tables in all schemas in the database. |
| tabname | VARCHAR2) | IN | Table name. If NULL it deletes column usage information for all tables of ownname . If both the owner and tabname is NULL , the seed column usage is stopped if applicable. See : SEED_COL_USAGE Procedure for more information. |

## Usage Notes

This procedure should only be used in very rare cases when the seed column usage needs to be initialized. Syntax DBMS_STATS.RESET_COL_USAGE ( ownname IN VARCHAR2, tabname IN VARCHAR2); Parameters Table 171-109 RESET_COL_USAGE Procedure Parameters Parameter Description ownname Owner name. If NULL it deletes column usage information for tables in all schemas in the database. tabname Table name. If NULL it deletes column usage information for all tables of ownname . If both the owner and tabname is NULL , the seed column usage is stopped if applicable. See : SEED_COL_USAGE Procedure for more information. Usage Notes To run this procedure, you need to have the SYSDBA administrative privilege, or both the ANALYZE ANY DICTIONARY and the ANALYZE ANY system privileges.