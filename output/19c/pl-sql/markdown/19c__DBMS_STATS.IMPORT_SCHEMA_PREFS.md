---
id: 19c__DBMS_STATS.IMPORT_SCHEMA_PREFS
name: DBMS_STATS.IMPORT_SCHEMA_PREFS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.IMPORT_SCHEMA_PREFS

This procedure is used to import the statistics preferences of all the tables owned by the specified owner name.

## Syntax

```sql
DBMS_STATS.IMPORT_SCHEMA_PREFS (
    ownname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name |
| stattab | VARCHAR2 | IN | Statistics table name from where to import the statistics |
| statid | VARCHAR2 | IN | (Optional) Identifier to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if other than ownname ) |

## Usage Notes

Syntax DBMS_STATS.IMPORT_SCHEMA_PREFS ( ownname IN VARCHAR2, stattab IN VARCHAR2, statid IN VARCHAR2 DEFAULT NULL, statown IN VARCHAR2 DEFAULT NULL); Parameters Table 171-77 IMPORT_SCHEMA_PREFS Procedure Parameters Parameter Description ownname Owner name stattab Statistics table name from where to import the statistics statid (Optional) Identifier to associate with these statistics within stattab statown Schema containing stattab (if other than ownname ) Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes To run this procedure, you need to connect as owner, or have the SYSDBA privilege, or have the ANALYZE ANY system privilege. All arguments are of type VARCHAR2 and values are enclosed in quotes. Oracle does not support export or import of statistics across databases of different character sets. Examples DBMS_STATS.IMPORT_SCHEMA_PREFS('SH', 'STAT');