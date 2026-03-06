---
id: 19c__DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY
name: DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY

This procedure is called after invoking the CREATE_TEMP_HISTORY_TABLE procedure, and after the TEMP_HISTORY table is populated with user-generated history data

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY (
   owner_name1         IN   VARCHAR2, 
   table_name1         IN   VARCHAR2 
   temp_history_name   IN   VARCHAR2 DEFAULT 'TEMP_HISTORY',
   options             IN   BINARY_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name 1 |  |  | Schema of the Flashback Time Travel-enabled table |
| table_name 1 |  |  | Name of the Flashback Time Travel-enabled table |
| temp_history_name | VARCHAR2 | IN | Optional temporary history table from which we import history data |
| options | BINARY_INTEGER | IN | One (or a combination) of constants ( NODROP , NOCOMMIT , and NODELETE ) to specify if we want to drop, commit changes of, or truncate the temporary history table |

## Usage Notes

Caution: Importing user-generated history can lead to inaccurate, or unreliable results. This procedure should only be used after consulting with Oracle Support. The DBMS_FLASHBACK_ARCHIVE package does not support migration between databases. It allows you to move Flashback Time Travel history within the same database only, and not outside it. This package does not allow you to move Flashback Time Travel table data. It allows you to import customer history only and not Flashback Time Travel history. Caution: Importing user-generated history can lead to inaccurate, or unreliable results. This procedure should only be used after consulting with Oracle Support. The DBMS_FLASHBACK_ARCHIVE package does not support migration between databases. It allows you to move Flashback Time Travel history within the same database only, and not outside it. This package does not allow you to move Flashback Time Travel table data. It allows you to import customer history only and not Flashback Time Travel history. Syntax DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY ( owner_name1 IN VARCHAR2, table_name1 IN VARCHAR2 temp_history_name IN VARCHAR2 DEFAULT 'TEMP_HISTORY', options IN BINARY_INTEGER DEFAULT 0); Parameters Table 73-12 IMPORT_HISTORY Procedure Parameters Parameter Description owner_name 1 Schema of the Flashback Time Travel-enabled table table_name 1 Name of the Flashback Time Travel-enabled table temp_history_name Optional temporary history table from which we import history data options One (or a combination) of constants ( NODROP , NOCOMMIT , and NODELETE ) to specify if we want to drop, commit changes of, or truncate the temporary history table Usage Notes The database function TIMESTAMP_TO_SCN can be used to convert times to SCN when populating the temporary history table.