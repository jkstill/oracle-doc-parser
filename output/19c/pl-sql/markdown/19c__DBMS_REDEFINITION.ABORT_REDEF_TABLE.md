---
id: 19c__DBMS_REDEFINITION.ABORT_REDEF_TABLE
name: DBMS_REDEFINITION.ABORT_REDEF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.ABORT_REDEF_TABLE

This procedure cleans up errors that occur during the redefinition process.

## Syntax

```sql
DBMS_REDEFINITION.ABORT_REDEF_TABLE (
   uname                   IN  VARCHAR2,
   orig_table              IN  VARCHAR2,
   int_table               IN  VARCHAR2,
   part_name               IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the tables |
| orig_table | VARCHAR2 | IN | Name of the table to be redefined |
| int_table | VARCHAR2 | IN | Name of the interim table. Can take a comma-delimited list of interim table names. |
| part_name | VARCHAR2 | IN | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. |

## Usage Notes

This procedure can also be used to terminate the redefinition process any time after the START_REDEF_TABLE Procedure has been called and before the FINISH_REDEF_TABLE Procedure is called. This process will remove the temporary objects that are created by the redefinition process such as materialized view logs. Syntax DBMS_REDEFINITION.ABORT_REDEF_TABLE ( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, part_name IN VARCHAR2 := NULL); Parameters Table 138-3 ABORT_REDEF_TABLE Procedure Parameters Parameter Description uname Schema name of the tables orig_table Name of the table to be redefined int_table Name of the interim table. Can take a comma-delimited list of interim table names. part_name Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined.