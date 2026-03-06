---
id: 19c__DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA
name: DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA

This procedure disassociates the given table from the Flashback Time Travel.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA (
   owner_name     IN    VARCHAR2, 
   table_name     IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name | VARCHAR2 | IN | Schema of the Flashback Time Travel enabled base table |
| table_name | VARCHAR2) | IN | Name of the Flashback Time Travel enabled base table |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA ( owner_name IN VARCHAR2, table_name IN VARCHAR2); Parameters Table 73-6 DISASSOCIATE_FBA Procedure Parameters Parameter Description owner_name Schema of the Flashback Time Travel enabled base table table_name Name of the Flashback Time Travel enabled base table Exceptions Table 73-7 DISASSOCIATE_FBA Procedure Exceptions Exception Description ORA-55602 User table is not enabled for Flashback Time Travel ORA-55634 Cannot acquire the lock on the table for disassociation