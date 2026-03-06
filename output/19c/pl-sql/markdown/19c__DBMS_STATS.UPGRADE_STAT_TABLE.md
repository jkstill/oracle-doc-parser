---
id: 19c__DBMS_STATS.UPGRADE_STAT_TABLE
name: DBMS_STATS.UPGRADE_STAT_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.UPGRADE_STAT_TABLE

This procedure upgrades a user statistics table from an older version.

## Syntax

```sql
DBMS_STATS.UPGRADE_STAT_TABLE (
   ownname    VARCHAR2,
   stattab    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| stattab | VARCHAR2) | IN | Name of the table |

## Usage Notes

Syntax DBMS_STATS.UPGRADE_STAT_TABLE ( ownname VARCHAR2, stattab VARCHAR2); Parameters Table 171-139 UPGRADE_STAT_TABLE Procedure Parameters Parameter Description ownname Name of the schema stattab Name of the table Exceptions ORA-20000 : Unable to upgrade table Usage Notes To invoke this procedure you need the privileges to drop and create a table.