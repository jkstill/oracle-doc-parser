---
id: 19c__DBMS_STATS.EXPORT_COLUMN_STATS
name: DBMS_STATS.EXPORT_COLUMN_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_COLUMN_STATS

This procedure exports statistics for a specified column and stores them in the user statistics table identified by stattab .

## Syntax

```sql
DBMS_STATS.EXPORT_COLUMN_STATS (
   ownname  VARCHAR2, 
   tabname  VARCHAR2, 
   colname  VARCHAR2, 
   partname VARCHAR2 DEFAULT NULL,
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| tabname | VARCHAR2 | IN | Name of the table to which this column belongs |
| colname | VARCHAR2 | IN | Name of the column or extension |
| partname | VARCHAR2 | IN | Name of the table partition. If the table is partitioned and if partname is NULL , then global and partition column statistics are exported. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to store the statistics |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_COLUMN_STATS ( ownname VARCHAR2, tabname VARCHAR2, colname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-40 EXPORT_COLUMN_STATS Procedure Parameters Parameter Description ownname Name of the schema tabname Name of the table to which this column belongs colname Name of the column or extension partname Name of the table partition. If the table is partitioned and if partname is NULL , then global and partition column statistics are exported. stattab User statistics table identifier describing where to store the statistics statid Identifier (optional) to associate with these statistics within stattab statown Schema containing stattab (if different than ownname ) Security Model To invoke this procedure you must be owner of the table or have the ANALYZE ANY privilege. For objects owned by SYS , you must be either the owner of the table or have either the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes Oracle Database does not support export or import of statistics across databases of different character sets.