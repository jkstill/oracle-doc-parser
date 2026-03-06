---
id: 19c__DBMS_OUTPUT.DISABLE
name: DBMS_OUTPUT.DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.DISABLE

This procedure disables calls to PUT , PUT_LINE , NEW_LINE , GET_LINE , and GET_LINES , and purges the buffer of any remaining information.

## Syntax

```sql
DBMS_OUTPUT.DISABLE;
```

## Usage Notes

As with the ENABLE Procedure , you do not need to call this procedure if you are using the SERVEROUTPUT option of SQL*Plus. Syntax DBMS_OUTPUT.DISABLE; Pragmas pragma restrict_references(disable,WNDS,RNDS);