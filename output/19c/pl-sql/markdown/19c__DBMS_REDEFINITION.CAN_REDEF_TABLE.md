---
id: 19c__DBMS_REDEFINITION.CAN_REDEF_TABLE
name: DBMS_REDEFINITION.CAN_REDEF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.CAN_REDEF_TABLE

This procedure determines if a given table can be redefined online. This is the first step of the online redefinition process. If the table is not a candidate for online redefinition, an error message is raised.

## Syntax

```sql
DBMS_REDEFINITION.CAN_REDEF_TABLE (
   uname         IN  VARCHAR2,
   tname        IN  VARCHAR2,
   options_flag  IN  PLS_INTEGER := 1,
   part_name     IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the table |
| tname | VARCHAR2 | IN | Name of the table to be re-organized |
| options_flag | PLS_INTEGER | IN | Indicates the type of redefinition method to use. If dbms_redefinition.cons_use_pk , the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having NOT NULL constraints). The default method of redefinition is using primary keys. If dbms_redefinition.cons_use_rowid , the redefinition is done using rowids. |
| part_name | VARCHAR2 | IN | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. |

## Usage Notes

Syntax DBMS_REDEFINITION.CAN_REDEF_TABLE ( uname IN VARCHAR2, tname IN VARCHAR2, options_flag IN PLS_INTEGER := 1, part_name IN VARCHAR2 := NULL); Parameters Table 138-6 CAN_REDEF_TABLE Procedure Parameters Parameter Description uname Schema name of the table tname Name of the table to be re-organized options_flag Indicates the type of redefinition method to use. If dbms_redefinition.cons_use_pk , the redefinition is done using primary keys or pseudo-primary keys (unique keys with all component columns having NOT NULL constraints). The default method of redefinition is using primary keys. If dbms_redefinition.cons_use_rowid , the redefinition is done using rowids. part_name Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Exceptions If the table is not a candidate for online redefinition, an error message is raised.