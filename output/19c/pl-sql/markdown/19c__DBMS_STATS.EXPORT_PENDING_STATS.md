---
id: 19c__DBMS_STATS.EXPORT_PENDING_STATS
name: DBMS_STATS.EXPORT_PENDING_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_PENDING_STATS

This procedure is used to export the statistics gathered and stored as pending.

## Syntax

```sql
DBMS_STATS.EXPORT_PENDING_STATS (
    ownname    IN  VARCHAR2  DEFAULT USER,
    tabname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT USER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name |
| tabname | VARCHAR2 | IN | Table name |
| stattab | VARCHAR2 | IN | Statistics table name to where to export the statistics |
| statid | VARCHAR2 | IN | (Optional) Identifier to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if other than ownname ) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_PENDING_STATS ( ownname IN VARCHAR2 DEFAULT USER, tabname IN VARCHAR2, stattab IN VARCHAR2, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT USER); Parameters Table 171-46 EXPORT_PENDING_STATS Procedure Parameters Parameter Description ownname Owner name tabname Table name stattab Statistics table name to where to export the statistics statid (Optional) Identifier to associate with these statistics within stattab statown Schema containing stattab (if other than ownname ) Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes If the parameter tabname is NULL then export applies to all tables of the specified schema. The default owner/schema is the user who runs the procedure. To run this procedure, you need to have the same privilege for gathering statistics on the tables that will be touched by this procedure. All arguments are of type VARCHAR2 and values are enclosed in quotes. Oracle does not support export or import of statistics across databases of different character sets. Examples DBMS_STATS.EXPORT_PENDING_STATS(NULL, NULL, 'MY_STAT_TABLE');