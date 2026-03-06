---
id: 19c__DBMS_STATS.SHOW_EXTENDED_STATS_NAME
name: DBMS_STATS.SHOW_EXTENDED_STATS_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SHOW_EXTENDED_STATS_NAME

This function returns the name of the statistics entry that is created for the user-specified extension. It raises an error if no extension has been created.

## Syntax

```sql
DBMS_STATS.SHOW_EXTENDED_STATS_NAME (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name of a table |
| tabname | VARCHAR2 | IN | Name of the table |
| extension | VARCHAR2) | IN | Can be either a column group or an expression. Suppose the specified table has two column c1 , c2 . An example column group can be "( c1 , c2 )" and an example expression can be "( c1 + c2 )". |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_STATS.SHOW_EXTENDED_STATS_NAME ( ownname VARCHAR2, tabname VARCHAR2, extension VARCHAR2) RETURN VARCHAR2; Parameters Table 171-134 SHOW_EXTENDED_STATS_NAME Function Parameters Parameter Description ownname Owner name of a table tabname Name of the table extension Can be either a column group or an expression. Suppose the specified table has two column c1 , c2 . An example column group can be "( c1 , c2 )" and an example expression can be "( c1 + c2 )". Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Error when processing extension Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege.