---
id: 19c__DBMS_ILM_ADMIN.CLEAR_HEAT_MAP_TABLE
name: DBMS_ILM_ADMIN.CLEAR_HEAT_MAP_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM_ADMIN
tags: [dbms_ilm_admin]
source_file: DBMS_ILM_ADMIN.html
---

# DBMS_ILM_ADMIN.CLEAR_HEAT_MAP_TABLE

This procedure clears all or some statistics for the heat map table, deleting rows for a given table or segment which match a given pattern, or all such rows.

## Syntax

```sql
DBMS_ILM_ADMIN.CLEAR_HEAT_MAP_TABLE  (
   owner                   IN  VARCHAR2,
   tablename               IN  VARCHAR2,
   partition               IN  VARCHAR2 default '',
   access_date             IN  DATE DEFAULT NULL,
   segment_access_summary  IN  NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Table owner |
| tablename | VARCHAR2 | IN | Table name |
| partition | VARCHAR2 | IN | Name of the subobject, defaults to NULL |
| access_date | DATE | IN | Date for the entry in HEAT_MAP_STAT$ to be removed |
| segment_access_summary | NUMBER | IN | Summary of segment access constants indicating access operations performed on the segment |

## Usage Notes

Syntax DBMS_ILM_ADMIN.CLEAR_HEAT_MAP_TABLE ( owner IN VARCHAR2, tablename IN VARCHAR2, partition IN VARCHAR2 default '', access_date IN DATE DEFAULT NULL, segment_access_summary IN NUMBER DEFAULT NULL); Parameters Table 87-4 CLEAR_HEAT_MAP_TABLE Procedure Parameters Parameter Description owner Table owner tablename Table name partition Name of the subobject, defaults to NULL access_date Date for the entry in HEAT_MAP_STAT$ to be removed segment_access_summary Summary of segment access constants indicating access operations performed on the segment