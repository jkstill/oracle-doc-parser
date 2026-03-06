---
id: 19c__DBMS_STATS.EXPORT_INDEX_STATS
name: DBMS_STATS.EXPORT_INDEX_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.EXPORT_INDEX_STATS

This procedure retrieves statistics for a particular index and stores them in the user statistics table identified by stattab .

## Syntax

```sql
DBMS_STATS.EXPORT_INDEX_STATS (
   ownname  VARCHAR2, 
   indname  VARCHAR2, 
   partname VARCHAR2 DEFAULT NULL,
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| indname | VARCHAR2 | IN | Name of the index |
| partname | VARCHAR2 | IN | Name of the index partition. If the index is partitioned and if partname is NULL , then global and partition index statistics are exported. |
| stattab | VARCHAR2 | IN | User statistics table identifier describing where to store the statistics |
| statid | VARCHAR2 | IN | Identifier (optional) to associate with these statistics within stattab |
| statown | VARCHAR2 | IN | Schema containing stattab (if different than ownname ) |

## Usage Notes

Syntax DBMS_STATS.EXPORT_INDEX_STATS ( ownname VARCHAR2, indname VARCHAR2, partname VARCHAR2 DEFAULT NULL, stattab VARCHAR2, statid VARCHAR2 DEFAULT NULL, statown VARCHAR2 DEFAULT NULL); Parameters Table 171-45 EXPORT_INDEX_STATS Procedure Parameters Parameter Description ownname Name of the schema indname Name of the index partname Name of the index partition. If the index is partitioned and if partname is NULL , then global and partition index statistics are exported. stattab User statistics table identifier describing where to store the statistics statid Identifier (optional) to associate with these statistics within stattab statown Schema containing stattab (if different than ownname ) Exceptions ORA-20000 : Object does not exist or insufficient privileges Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Oracle does not support export or import of statistics across databases of different character sets.