---
id: 19c__DBMS_REPAIR.ADMIN_TABLES
name: DBMS_REPAIR.ADMIN_TABLES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.ADMIN_TABLES

This procedure provides administrative functions for the DBMS_REPAIR package repair and orphan key tables.

## Syntax

```sql
DBMS_REPAIR.ADMIN_TABLES (
   table_name  IN   VARCHAR2,
   table_type  IN   BINARY_INTEGER,
   action      IN   BINARY_INTEGER,
   tablespace  IN   VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Name of the table to be processed. Defaults to ORPHAN_KEY_TABLE or REPAIR_TABLE based on the specified table_type . When specified, the table name must have the appropriate prefix: ORPHAN_ or REPAIR_ . |
| table_type | BINARY_INTEGER | IN | Type of table; must be either ORPHAN_TABLE or REPAIR_TABLE . See " Constants " . |
| action | BINARY_INTEGER | IN | Indicates what administrative action to perform. Must be either CREATE_ACTION , PURGE_ACTION , or DROP_ACTION . If the table already exists, and if CREATE_ACTION is specified, then an error is returned. PURGE_ACTION indicates to delete all rows in the table that are associated with non-existent objects. If the table does not exist, and if DROP_ACTION is specified, then an error is returned. When CREATE_ACTION and DROP_ACTION are specified, an associated view named DBA_<table_name> is created and dropped respectively. The view is defined so that rows associated with non-existent objects are eliminated. Created in the SYS schema. See " Constants " . |
| tablespace | VARCHAR2 | IN | Indicates the tablespace to use when creating a table. By default, the SYS default tablespace is used. An error is returned if the tablespace is specified and if the action is not CREATE_ACTION . |

## Usage Notes

Syntax DBMS_REPAIR.ADMIN_TABLES ( table_name IN VARCHAR2, table_type IN BINARY_INTEGER, action IN BINARY_INTEGER, tablespace IN VARCHAR2 DEFAULT NULL); Parameters Table 140-4 ADMIN_TABLES Procedure Parameters Parameter Description table_name Name of the table to be processed. Defaults to ORPHAN_KEY_TABLE or REPAIR_TABLE based on the specified table_type . When specified, the table name must have the appropriate prefix: ORPHAN_ or REPAIR_ . table_type Type of table; must be either ORPHAN_TABLE or REPAIR_TABLE . See " Constants " . action Indicates what administrative action to perform. Must be either CREATE_ACTION , PURGE_ACTION , or DROP_ACTION . If the table already exists, and if CREATE_ACTION is specified, then an error is returned. PURGE_ACTION indicates to delete all rows in the table that are associated with non-existent objects. If the table does not exist, and if DROP_ACTION is specified, then an error is returned. When CREATE_ACTION and DROP_ACTION are specified, an associated view named DBA_<table_name> is created and dropped respectively. The view is defined so that rows associated with non-existent objects are eliminated. Created in the SYS schema. See " Constants " . tablespace Indicates the tablespace to use when creating a table. By default, the SYS default tablespace is used. An error is returned if the tablespace is specified and if the action is not CREATE_ACTION .