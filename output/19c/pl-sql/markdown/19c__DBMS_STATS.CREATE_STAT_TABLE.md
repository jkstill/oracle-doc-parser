---
id: 19c__DBMS_STATS.CREATE_STAT_TABLE
name: DBMS_STATS.CREATE_STAT_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CREATE_STAT_TABLE

This procedure creates a table with name stattab in ownname 's schema which is capable of holding statistics. The columns and types that compose this table are not relevant as it should be accessed solely through the procedures in this package.

## Syntax

```sql
DBMS_STATS.CREATE_STAT_TABLE (
   ownname             VARCHAR2, 
   stattab             VARCHAR2,
   tblspace            VARCHAR2 DEFAULT NULL,
   global_temporary    BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Name of the schema |
| stattab | VARCHAR2 | IN | Name of the table to create. This value should be passed as the stattab parameter to other procedures when the user does not want to modify the dictionary statistics directly. |
| tblspace | VARCHAR2 | IN | Tablespace in which to create the statistics tables. If none is specified, then they are created in the user's default tablespace. |
| global_temporary | BOOLEAN | IN | Whether or not the table should be created as a global temporary table |

## Usage Notes

Syntax DBMS_STATS.CREATE_STAT_TABLE ( ownname VARCHAR2, stattab VARCHAR2, tblspace VARCHAR2 DEFAULT NULL, global_temporary BOOLEAN DEFAULT FALSE); Parameters Table 171-16 CREATE_STAT_TABLE Procedure Parameters Parameter Description ownname Name of the schema stattab Name of the table to create. This value should be passed as the stattab parameter to other procedures when the user does not want to modify the dictionary statistics directly. tblspace Tablespace in which to create the statistics tables. If none is specified, then they are created in the user's default tablespace. global_temporary Whether or not the table should be created as a global temporary table Security Model To invoke this procedure you need whichever privileges are required for creating a table in the specified schema. Exceptions ORA-20000 : Table already exists or insufficient privileges ORA-20001 : Tablespace does not exist