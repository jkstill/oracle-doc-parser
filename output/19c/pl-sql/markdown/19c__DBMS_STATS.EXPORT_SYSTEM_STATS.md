---
id: 19c__DBMS_STATS.EXPORT_SYSTEM_STATS
name: DBMS_STATS.EXPORT_SYSTEM_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_SYSTEM_STATS

This procedure retrieves system statistics and stores them in the user statistics table, identified by stattab .

## Syntax

```sql
DBMS_STATS.EXPORT_SYSTEM_STATS (
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | Identifier of the user statistics table that describes where the statistics will be stored |
| statid | VARCHAR2 | IN | Optional identifier associated with the statistics stored from the stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_SYSTEM_STATS ( stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-49 EXPORT_SYSTEM_STATS Procedure Parameters Parameter Description stattab Identifier of the user statistics table that describes where the statistics will be stored statid Optional identifier associated with the statistics stored from the stattab statown Schema containing stattab (if different from current schema) Security Model To run this procedure, you must have the GATHER_SYSTEM_STATISTICS role. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20002 : Bad user statistics table; may need to be upgraded ORA-20003 : Unable to export system statistics Usage Notes Oracle Database does not support the export or import of statistics across databases of different character sets.