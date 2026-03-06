---
id: 19c__DBMS_ASSERT.QUALIFIED_SQL_NAME
name: DBMS_ASSERT.QUALIFIED_SQL_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.QUALIFIED_SQL_NAME

This function verifies that the input string is a qualified SQL name.

## Syntax

```sql
DBMS_ASSERT.QUALIFIED_SQL_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Input value |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.QUALIFIED_SQL_NAME ( str VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 26-5 QUALIFIED_SQL_NAME Function Parameters Parameter Description str Input value Exceptions ORA44004 : string is not a qualified SQL name Usage Notes A qualified SQL name <qualified name> can be expressed by the following grammar: <local qualified name> ::= <simple name> {'.' <simple name>} <database link name> ::= <local qualified name> ['@' <connection string>] <connection string> ::= <simple name> <qualified name> ::= <local qualified name> ['@' <database link name>]