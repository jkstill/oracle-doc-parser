---
id: 19c__DBMS_STATS.CREATE_EXTENDED_STATS
name: DBMS_STATS.CREATE_EXTENDED_STATS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CREATE_EXTENDED_STATS

This function creates a column statistics entry in the system for a user-specified column group or an expression in a table.

## Syntax

```sql
DBMS_STATS.CREATE_EXTENDED_STATS (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2)
 RETURN VARCHAR2;

DBMS_STATS.CREATE_EXTENDED_STATS (
   ownname    VARCHAR2, 
   tabname    VARCHAR2)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name of a table |
| tabname | VARCHAR2 | IN | Name of the table |
| extension | VARCHAR2) | IN | Can be either a column group or an expression. Suppose the specified table has columns c1 , c2 . An example column group is "( c1 , c2 )". An example expression is "( c1 + c2 )". |

**Returns:** `VARCHAR2`

## Usage Notes

The database gathers statistics for this extension when a user-initiated or automatic statistics gathering job gathers statistics for the table. Statistics for such an extension are called extended statistics . This function returns the name of this newly created entry for the extension. This second form of this function creates statistics extensions based on the column group usage recorded by the SEED_COL_USAGE Procedure . This function returns a report of extensions created. Syntax DBMS_STATS.CREATE_EXTENDED_STATS ( ownname VARCHAR2, tabname VARCHAR2, extension VARCHAR2) RETURN VARCHAR2; DBMS_STATS.CREATE_EXTENDED_STATS ( ownname VARCHAR2, tabname VARCHAR2) RETURN CLOB; Parameters Table 171-15 CREATE_EXTENDED_STATS Function Parameters Parameter Description ownname Owner name of a table tabname Name of the table extension Can be either a column group or an expression. Suppose the specified table has columns c1 , c2 . An example column group is "( c1 , c2 )". An example expression is "( c1 + c2 )". Return Values This function returns the name of this newly created entry for the extension. Exceptions ORA-20000 : Insufficient privileges / creating extension is not supported ORA-20001 : Error when processing extension ORA-20007 : Extension already exists ORA-20008 : Reached the upper limit on number of extensions