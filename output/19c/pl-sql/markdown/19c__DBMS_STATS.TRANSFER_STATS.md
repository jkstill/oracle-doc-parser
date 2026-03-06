---
id: 19c__DBMS_STATS.TRANSFER_STATS
name: DBMS_STATS.TRANSFER_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.TRANSFER_STATS

This procedure transfers statistics for specified table(s) from a remote database specified by dblink to the local database.

## Syntax

```sql
DBMS_STATS.TRANSFER_STATS (
   ownname     IN     VARCHAR2,
   tabname     IN     VARCHAR2,
   dblink      IN     VARCHAR2,   options     IN     NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name of a table. If NULL all schemas in the database. If NULL , the procedure will transfer global preferences as well. |
| tabname | VARCHAR2 | IN | Name of the table. If NULL , all tables in OWNNAME . |
| dblink | VARCHAR2 | IN | Database link name |
| options | NUMBER | IN | By default the procedure does not transfer the global preferences. Specifying ADD_GLOBAL_PREFS copies global preferences. |

## Usage Notes

The statistics at the source database are retained. It likewise transfers statistics-related structures such as synopses and DML monitoring information. Syntax DBMS_STATS.TRANSFER_STATS ( ownname IN VARCHAR2, tabname IN VARCHAR2, dblink IN VARCHAR2, options IN NUMBER DEFAULT NULL); Parameters Table 171-135 TRANSFER_STATS Procedure Parameters Parameter Description ownname Owner name of a table. If NULL all schemas in the database. If NULL , the procedure will transfer global preferences as well. tabname Name of the table. If NULL , all tables in OWNNAME . dblink Database link name options By default the procedure does not transfer the global preferences. Specifying ADD_GLOBAL_PREFS copies global preferences. Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.