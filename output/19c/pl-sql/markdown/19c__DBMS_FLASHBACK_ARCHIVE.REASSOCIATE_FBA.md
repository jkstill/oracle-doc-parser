---
id: 19c__DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA
name: DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA

This procedure reassociates the given table with the Flashback Time Travel.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA (
   owner_name      VARCHAR2, 
   table_name      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name | VARCHAR2 | IN | Schema of the Flashback Time Travel enabled base table |
| table_name | VARCHAR2) | IN | Name of the Flashback Time Travel enabled base table |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA ( owner_name VARCHAR2, table_name VARCHAR2); Parameters Table 73-14 REASSOCIATE_FBA Procedure Parameters Parameter Description owner_name Schema of the Flashback Time Travel enabled base table table_name Name of the Flashback Time Travel enabled base table Exceptions Table 73-15 REASSOCIATE_FBA Procedure Exceptions Parameter Description ORA-55602 User table is not enabled for Flashback Time Travel ORA-55636 Table definition validation failed Usage Notes The procedure will signal an error if the base table and the history table do not have identical data definitions. For example, when columns are added or table is split, the resulting base table and history table need to have the same schema. The Flashback Time Travel internal history table schema has some row versions metadata columns. The procedure will signal an error if any metadata column is dropped by users.