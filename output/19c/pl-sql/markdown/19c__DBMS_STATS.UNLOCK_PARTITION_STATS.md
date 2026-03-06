---
id: 19c__DBMS_STATS.UNLOCK_PARTITION_STATS
name: DBMS_STATS.UNLOCK_PARTITION_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.UNLOCK_PARTITION_STATS

This procedure enables the user to unlock statistics for a partition.

## Syntax

```sql
DBMS_STATS.UNLOCK_PARTITION_STATS (
    ownname    VARCHAR2,
    tabname    VARCHAR2,
    partname   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema to unlock |
| tabname | VARCHAR2 | IN | Name of the table |
| partname | VARCHAR2) | IN | [Sub]Partition name |

## Usage Notes

Syntax DBMS_STATS.UNLOCK_PARTITION_STATS ( ownname VARCHAR2, tabname VARCHAR2, partname VARCHAR2); Parameters Table 171-136 UNLOCK_PARTITION_STATS Procedure Parameters Parameter Description ownname Name of the schema to unlock tabname Name of the table partname [Sub]Partition name Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.