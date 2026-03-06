---
id: 19c__DBMS_OUTPUT
name: DBMS_OUTPUT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT

The DBMS_OUTPUT package declares 2 collection types for use with the GET_LINES Procedure.

## Syntax

```sql
TYPE CHARARR IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;
```

## Usage Notes

TABLE Types CHARARR Table Type OBJECT Types DBMSOUTPUT_LINESARRAY Object Type Syntax TYPE CHARARR IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER; Syntax TYPE DBMSOUTPUT_LINESARRAY IS VARRAY(2147483647) OF VARCHAR2(32767);