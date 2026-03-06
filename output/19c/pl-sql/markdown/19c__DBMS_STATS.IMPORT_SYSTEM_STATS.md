---
id: 19c__DBMS_STATS.IMPORT_SYSTEM_STATS
name: DBMS_STATS.IMPORT_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.IMPORT_SYSTEM_STATS

This procedure retrieves system statistics from the user statistics table, identified by stattab , and stores the statistics in the dictionary.

## Syntax

```sql
DBMS_STATS.IMPORT_SYSTEM_STATS (
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | Identifier of the user statistics table where the statistics will be retrieved |
| statid | VARCHAR2 | IN | Optional identifier associated with the statistics retrieved from the stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.IMPORT_SYSTEM_STATS ( stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-79 IMPORT_SYSTEM_STATS Procedure Parameters Parameter Description stattab Identifier of the user statistics table where the statistics will be retrieved statid Optional identifier associated with the statistics retrieved from the stattab statown Schema containing stattab (if different from current schema) Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values in the user statistics table ORA-20002 : Bad user statistics table; may need to be upgraded ORA-20003 : Unable to import system statistics Usage Notes To run this procedure, you need the GATHER_SYSTEM_STATISTICS role. Oracle does not support export or import of statistics across databases of different character sets.