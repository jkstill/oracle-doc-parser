---
id: 19c__DBMS_DST.CREATE_TRIGGER_TABLE
name: DBMS_DST.CREATE_TRIGGER_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.CREATE_TRIGGER_TABLE

This procedure creates a table to record active triggers that are disabled before performing upgrade on the table, having not been enabled due to fatal failure during the upgrading process.

## Syntax

```sql
CREATE TABLE dst_trigger_table (
trigger_owner  VARCHAR2(30),
trigger_name   VARCHAR2(30));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name |  |  | Name of table to be created |

## Usage Notes

The table that has the following schema. CREATE TABLE dst_trigger_table ( trigger_owner VARCHAR2(30), trigger_name VARCHAR2(30)); Syntax DBMS_DST.CREATE_TRIGGER_TABLE ( table_name IN VARCHAR2); Parameters Table 65-7 CREATE_TRIGGER_TABLE Procedure Parameters Parameter Description table_name Name of table to be created Usage Notes This procedures takes a table_name without schema qualification, creating a table within the current user schema.