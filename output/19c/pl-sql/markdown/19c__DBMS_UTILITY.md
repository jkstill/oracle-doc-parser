---
id: 19c__DBMS_UTILITY
name: DBMS_UTILITY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY

The DBMS_UTILITY package defines a single RECORD type and TABLE types.

## Syntax

```sql
TYPE INSTANCE_RECORD IS RECORD (
       inst_number   NUMBER,
       inst_name     VARCHAR2(60));
```

## Usage Notes

Record Types INSTANCE_RECORD Record Type Table Types DBLINK_ARRAY TABLE Type INDEX_TABLE_TYPE Table Type INSTANCE_TABLE Table Type LNAME_ARRAY Table Type NAME_ARRAY Table Type NUMBER_ARRAY Table Type UNCL_ARRAY Table Type Syntax TYPE INSTANCE_RECORD IS RECORD ( inst_number NUMBER, inst_name VARCHAR2(60)); Fields Table 187-3 INSTANCE_RECORD Record Type Fields Field Description inst_number Active instance number inst_name Instance name Syntax TYPE DBLINK_ARRAY IS TABLE OF VARCHAR2(128) INDEX BY BINARY_INTEGER;