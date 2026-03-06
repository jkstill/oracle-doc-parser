---
id: 19c__DBMS_STATS.EXPORT_SCHEMA_STATS
name: DBMS_STATS.EXPORT_SCHEMA_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_SCHEMA_STATS

This procedure exports statistics for all objects in the schema identified by ownname and stores them in the user statistics tables identified by stattab .

## Syntax

```sql
DBMS_STATS.EXPORT_SCHEMA_STATS (
   ownname         VARCHAR2,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Specifies the name of the schema. |
| stattab | VARCHAR2 | IN | Identifies the user statistics table in which to store the exported statistics. |
| statid | VARCHAR2 | IN | Specifies the identifier (optional) associated with these statistics within stattab . |
| statown | VARCHAR2 | IN | Specifies the schema containing stattab (if different than ownname ). |
| stat_category | VARCHAR2 | IN | Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . |

## Usage Notes

Syntax DBMS_STATS.EXPORT_SCHEMA_STATS ( ownname VARCHAR2, stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL, stat_category VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY); Parameters Table 171-48 EXPORT_SCHEMA_STATS Procedure Parameters Parameter Description ownname Specifies the name of the schema. stattab Identifies the user statistics table in which to store the exported statistics. statid Specifies the identifier (optional) associated with these statistics within stattab . statown Specifies the schema containing stattab (if different than ownname ). stat_category Specifies which statistics to process. The following values are supported: OBJECT_STATS — Specifies table statistics, column statistics, and index statistics. SYNOPSES — Specifies metadata for incremental statistics. REALTIME_STATS — Specifies only real-time statistics . You can specify a list of comma-delimited values. For example, 'OBJECT_STATS, SYNOPSES' specifies table statistics, column statistics, index statistics, and synopses. The default value is 'OBJECT_STATS, REALTIME_STATS' . Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes Oracle Database does not support export or import of statistics across databases of different character sets.