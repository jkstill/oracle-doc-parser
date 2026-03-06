---
id: 19c__UTL_CALL_STACK.UNIT_QUALIFIED_NAME
name: UTL_CALL_STACK.UNIT_QUALIFIED_NAME
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.UNIT_QUALIFIED_NAME

This data structure is a varray whose individual elements are, in order, the unit name, any lexical parents of the subprogram, and the subprogram name.

## Syntax

```sql
TYPE UNIT_QUALIFIED_NAME IS VARRAY(256) OF VARCHAR2(32767);
```

## Usage Notes

TYPE UNIT_QUALIFIED_NAME IS VARRAY(256) OF VARCHAR2(32767); Consider the following contrived PL/SQL procedure: PROCEDURE topLevel IS FUNCTION localFunction(...) RETURNS VARCHAR2 IS FUNCTION innerFunction(...) RETURNS VARCHAR2 IS BEGIN DECLARE localVar PLS_INTEGER; BEGIN ... (1) END; END; BEGIN ... END; The unit qualified name at (1) would be ["topLevel", "localFunction", "innerFunction"] If the unit were an anonymous block, the unit name would be "__anonymous_block"