---
id: 19c__DBMS_STATS.GENERATE_STATS
name: DBMS_STATS.GENERATE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GENERATE_STATS

This deprecated procedure generates object statistics from previously collected statistics of related objects. The currently supported objects are b-tree and bitmap indexes.

## Syntax

```sql
DBMS_STATS.GENERATE_STATS (
   ownname    VARCHAR2, 
   objname    VARCHAR2,
   organized  NUMBER DEFAULT 7,
   force      BOOLEAN default FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Schema of object |
| objname | VARCHAR2 | IN | Name of object |
| organized | NUMBER | IN | Amount of ordering associated between the index and its underlying table. A heavily organized index would have consecutive index keys referring to consecutive rows on disk for the table (the same block). A heavily disorganized index would have consecutive keys referencing different table blocks on disk. This parameter is only used for b-tree indexes. The number can be in the range of 0-10, with 0 representing a completely organized index and 10 a completely disorganized one. |
| force | BOOLEAN | IN | If TRUE , generates statistics for the target object even if it is locked |

## Usage Notes

Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, use the GATHER_INDEX_STAT procedure. See " GATHER_INDEX_STATS Procedure " . Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, use the GATHER_INDEX_STAT procedure. See " GATHER_INDEX_STATS Procedure " . Syntax DBMS_STATS.GENERATE_STATS ( ownname VARCHAR2, objname VARCHAR2, organized NUMBER DEFAULT 7, force BOOLEAN default FALSE); Parameters Table 171-60 GENERATE_STATS Procedure Parameters Parameter Description ownname Schema of object objname Name of object organized Amount of ordering associated between the index and its underlying table. A heavily organized index would have consecutive index keys referring to consecutive rows on disk for the table (the same block). A heavily disorganized index would have consecutive keys referencing different table blocks on disk. This parameter is only used for b-tree indexes. The number can be in the range of 0-10, with 0 representing a completely organized index and 10 a completely disorganized one. force If TRUE , generates statistics for the target object even if it is locked Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS, you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. For fully populated schemas, the gather procedures should be used instead when more accurate statistics are desired.