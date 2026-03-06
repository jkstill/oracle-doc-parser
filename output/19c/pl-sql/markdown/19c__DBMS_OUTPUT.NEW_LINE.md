---
id: 19c__DBMS_OUTPUT.NEW_LINE
name: DBMS_OUTPUT.NEW_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.NEW_LINE

This procedure puts an end-of-line marker.

## Syntax

```sql
DBMS_OUTPUT.NEW_LINE;
```

## Usage Notes

The GET_LINE Procedure and the GET_LINES Procedure return "lines" as delimited by "newlines". Every call to the PUT_LINE Procedure or NEW_LINE Procedure generates a line that is returned by GET_LINE ( S ). Syntax DBMS_OUTPUT.NEW_LINE;