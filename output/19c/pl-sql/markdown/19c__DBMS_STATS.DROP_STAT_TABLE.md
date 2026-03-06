---
id: 19c__DBMS_STATS.DROP_STAT_TABLE
name: DBMS_STATS.DROP_STAT_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DROP_STAT_TABLE

This procedure drops a user statistics table.

## Syntax

```sql
DBMS_STATS.DROP_STAT_TABLE (
   ownname VARCHAR2, 
   stattab VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| stattab | VARCHAR2) | IN | User statistics table identifier |

## Usage Notes

Syntax DBMS_STATS.DROP_STAT_TABLE ( ownname VARCHAR2, stattab VARCHAR2); Parameters Table 171-38 DROP_STAT_TABLE Procedure Parameters Parameter Description ownname Name of the schema stattab User statistics table identifier Exceptions ORA-20000 : Table does not exists or insufficient privileges. Usage Notes To invoke this procedure you need the privileges for dropping the specified table.