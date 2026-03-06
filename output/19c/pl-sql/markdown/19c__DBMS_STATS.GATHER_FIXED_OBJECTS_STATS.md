---
id: 19c__DBMS_STATS.GATHER_FIXED_OBJECTS_STATS
name: DBMS_STATS.GATHER_FIXED_OBJECTS_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GATHER_FIXED_OBJECTS_STATS

This procedure gathers statistics for all fixed objects (dynamic performance tables).

## Syntax

```sql
DBMS_STATS.GATHER_FIXED_OBJECTS_STATS (
   stattab        VARCHAR2 DEFAULT NULL,
   statid         VARCHAR2 DEFAULT NULL,
   statown        VARCHAR2 DEFAULT NULL, 
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to save the current statistics |
| statid | VARCHAR2 | IN | Identifier to associate with these statistics within stattab (optional) |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |
| no_invalidate | BOOLEAN | IN | Does not invalidate the dependent cursors if set to TRUE . The procedure invalidates the dependent cursors immediately if set to FALSE . Use DBMS_STATS . AUTO_INVALIDATE . to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . |

## Usage Notes

Syntax DBMS_STATS.GATHER_FIXED_OBJECTS_STATS ( stattab VARCHAR2 DEFAULT NULL, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, no_invalidate BOOLEAN DEFAULT to_no_invalidate_type ( get_param('NO_INVALIDATE'))); Parameters Table 171-54 GATHER_FIXED_OBJECTS_STATS Procedure Parameters Parameter Description stattab User statistics table identifier describing where to save the current statistics statid Identifier to associate with these statistics within stattab (optional) statown Schema containing stattab (if different from current schema) no_invalidate Does not invalidate the dependent cursors if set to TRUE . The procedure invalidates the dependent cursors immediately if set to FALSE . Use DBMS_STATS . AUTO_INVALIDATE . to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET_DATABASE_PREFS Procedure , SET_GLOBAL_PREFS Procedure , SET_SCHEMA_PREFS Procedure and SET_TABLE_PREFS Procedure . Usage Notes You must have the SYSDBA or ANALYZE ANY DICTIONARY system privilege to execute this procedure. Exceptions ORA-20000 : Insufficient privileges ORA-20001 : Bad input value ORA-20002 : Bad user statistics table, may need to upgrade it