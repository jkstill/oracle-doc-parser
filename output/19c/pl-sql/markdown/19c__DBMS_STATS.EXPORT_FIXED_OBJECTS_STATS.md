---
id: 19c__DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS
name: DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS

This procedure exports statistics for fixed tables and stores them in the user statistics table identified by stattab .

## Syntax

```sql
DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS (
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to store the statistics |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different from current schema) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS ( stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-44 EXPORT_FIXED_OBJECTS_STATS Procedure Parameters Parameter Description stattab User statistics table identifier describing where to store the statistics statid Identifier (optional) to associate with these statistics within stattab statown Schema containing stattab (if different from current schema) Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20002 : Bad user statistics table, may need to upgrade it Usage Notes Oracle Database does not support export or import of statistics across databases of different character sets.