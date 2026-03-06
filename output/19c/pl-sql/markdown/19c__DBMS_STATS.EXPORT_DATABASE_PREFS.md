---
id: 19c__DBMS_STATS.EXPORT_DATABASE_PREFS
name: DBMS_STATS.EXPORT_DATABASE_PREFS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_DATABASE_PREFS

This procedure is used to export the statistics preferences of all the tables, excluding the tables owned by Oracle. These tables can by included by passing TRUE for the add_sys parameter.

## Syntax

```sql
DBMS_STATS.EXPORT_DATABASE_PREFS (
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL
    add_sys    IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | Statistics table name to where statistics should be exported |
| statid | VARCHAR2 | IN | (Optional) Identifier to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if other than ownname ) |
| add_sys | BOOLEAN | IN | Value TRUE will include the Oracle-owned tables |

## Usage Notes

Syntax DBMS_STATS.EXPORT_DATABASE_PREFS ( stattab IN VARCHAR2, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL add_sys IN BOOLEAN DEFAULT FALSE); Parameters Table 171-41 EXPORT_DATABASE_PREFS Procedure Parameters Parameter Description stattab Statistics table name to where statistics should be exported statid (Optional) Identifier to associate with these statistics within stattab statown Schema containing stattab (if other than ownname ) add_sys Value TRUE will include the Oracle-owned tables Exceptions ORA-20000 : Insufficient privileges Usage Notes To run this procedure, you need to have the SYSDBA role, or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privileges. All arguments are of type VARCHAR2 and values are enclosed in quotes. Oracle does not support export or import of statistics across databases of different character sets. Examples DBMS_STATS.EXPORT_DATABASE_PREFS('STATTAB', statown=>'SH');