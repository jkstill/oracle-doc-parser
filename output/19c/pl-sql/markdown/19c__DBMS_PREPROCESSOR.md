---
id: 19c__DBMS_PREPROCESSOR
name: DBMS_PREPROCESSOR
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PREPROCESSOR
tags: [dbms_preprocessor]
source_file: DBMS_PREPROCESSOR.html
---

# DBMS_PREPROCESSOR

The DBMS_PREPROCESSOR package defines a TABLE type.

## Syntax

```sql
TYPE source_lines_t IS
    TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;
```

## Usage Notes

Table Types SOURCE_LINES_T Table Type Syntax TYPE source_lines_t IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;