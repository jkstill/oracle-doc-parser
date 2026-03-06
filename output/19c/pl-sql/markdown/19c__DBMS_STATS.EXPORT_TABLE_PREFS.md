---
id: 19c__DBMS_STATS.EXPORT_TABLE_PREFS
name: DBMS_STATS.EXPORT_TABLE_PREFS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_TABLE_PREFS

This procedure is used to export the statistics preferences of the specified table in the specified schema into the specified statistics table.

## Syntax

```sql
DBMS_STATS.EXPORT_TABLE_PREFS (
    ownname    IN  VARCHAR2,
    tabname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name |
| tabname | VARCHAR2 | IN | Table name |
| stattab | VARCHAR2 | IN | Statistics table name where to export the statistics |
| statid | VARCHAR2 | IN | Optional identifier to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if other than ownname ) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_TABLE_PREFS ( ownname IN VARCHAR2, tabname IN VARCHAR2, stattab IN VARCHAR2, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL); Parameters Table 171-50 EXPORT_TABLE_PREFS Procedure Parameters Parameter Description ownname Owner name tabname Table name stattab Statistics table name where to export the statistics statid Optional identifier to associate with these statistics within stattab statown Schema containing stattab (if other than ownname ) Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes To run this procedure, you need to connect as owner of the table, or have the ANALYZE ANY system privilege. All arguments are of type VARCHAR2 and values are enclosed in quotes. Oracle does not support export or import of statistics across databases of different character sets. Examples DBMS_STATS.EXPORT_TABLE_PREFS('SH', 'SALES', 'STAT');