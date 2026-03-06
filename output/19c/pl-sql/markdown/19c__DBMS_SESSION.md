---
id: 19c__DBMS_SESSION
name: DBMS_SESSION
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION

The DBMS_SESSION package defines TABLE types.

## Syntax

```sql
TYPE integer_array IS TABLE OF BINARY_INTEGER INDEX BY BINARY_INTEGER;
```

## Usage Notes

Table Types INTEGER_ARRAY Table Type LNAME_ARRAY Table Type Syntax TYPE integer_array IS TABLE OF BINARY_INTEGER INDEX BY BINARY_INTEGER; Syntax TYPE lname_array IS TABLE OF VARCHAR2(4000) INDEX BY BINARY_INTEGER;