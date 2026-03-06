---
id: 19c__DBMS_STATS.DROP_EXTENDED_STATS
name: DBMS_STATS.DROP_EXTENDED_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.DROP_EXTENDED_STATS

This function drops the statistics entry that is created for the user specified extension.

## Syntax

```sql
DBMS_STATS.DROP_EXTENDED_STATS (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner name of a table |
| tabname | VARCHAR2 | IN | Name of the table |
| extension | VARCHAR2) | IN | Can be either a column group or an expression. Suppose the specified table has two column c1 , c2 . An example column group can be "( c1 , c2 )" and an example expression can be "( c1 + c2 )". |

## Usage Notes

This cancels the effects of the CREATE_EXTENDED_STATS Function . Syntax DBMS_STATS.DROP_EXTENDED_STATS ( ownname VARCHAR2, tabname VARCHAR2, extension VARCHAR2); Parameters Table 171-37 DROP_EXTENDED_STATS Procedure Parameters Parameter Description ownname Owner name of a table tabname Name of the table extension Can be either a column group or an expression. Suppose the specified table has two column c1 , c2 . An example column group can be "( c1 , c2 )" and an example expression can be "( c1 + c2 )". Exceptions ORA-20000 : Insufficient privileges or extension does not exist ORA-20001 : Error when processing extension Usage Notes To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. If no extended statistics set is created for the extension, this function throws an error.