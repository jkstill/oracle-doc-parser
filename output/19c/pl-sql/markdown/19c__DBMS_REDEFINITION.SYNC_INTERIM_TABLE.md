---
id: 19c__DBMS_REDEFINITION.SYNC_INTERIM_TABLE
name: DBMS_REDEFINITION.SYNC_INTERIM_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.SYNC_INTERIM_TABLE

This procedure keeps the interim table synchronized with the original table.

## Syntax

```sql
DBMS_REDEFINITION.SYNC_INTERIM_TABLE (
   uname                   IN  VARCHAR2,
   orig_table              IN  VARCHAR2,
   int_table               IN  VARCHAR2,
   part_name               IN  VARCHAR2 := NULL,
   continue_after_errors   IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the table |
| orig_table | VARCHAR2 | IN | Name of the table to be redefined |
| int_table | VARCHAR2 | IN | Name of the interim table. Can take a comma-delimited list of interim table names. |
| part_name | VARCHAR2 | IN | Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. |
| continue_after_errors | BOOLEAN | IN | When redefining multiple partitions allows operation execution to continue on the next partition (applies only to batched partition redefinition) |

## Usage Notes

Syntax DBMS_REDEFINITION.SYNC_INTERIM_TABLE ( uname IN VARCHAR2, orig_table IN VARCHAR2, int_table IN VARCHAR2, part_name IN VARCHAR2 := NULL, continue_after_errors IN BOOLEAN := FALSE); Parameters Table 138-15 SYNC_INTERIM_TABLE Procedure Parameters Parameter Description uname Schema name of the table orig_table Name of the table to be redefined int_table Name of the interim table. Can take a comma-delimited list of interim table names. part_name Name of the partition being redefined. If redefining only a single partition of a table, specify the partition name in this parameter. NULL implies the entire table is being redefined. Can take a comma-delimited list of partition names to be redefined. continue_after_errors When redefining multiple partitions allows operation execution to continue on the next partition (applies only to batched partition redefinition) Usage Notes This step is useful in minimizing the amount of synchronization needed to be done by the FINISH_REDEF_TABLE Procedure before completing the online redefinition. This procedure can be called between long running operations (such as CREATE INDEX ) on the interim table to sync it up with the data in the original table and speed up subsequent operations.