---
id: 19c__DBMS_ASSERT.SIMPLE_SQL_NAME
name: DBMS_ASSERT.SIMPLE_SQL_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.SIMPLE_SQL_NAME

This function verifies that the input string is a simple SQL name.

## Syntax

```sql
DBMS_ASSERT.SIMPLE_SQL_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Input value |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.SIMPLE_SQL_NAME ( str VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 26-7 SIMPLE_SQL_NAME Function Parameters Parameter Description str Input value Exceptions ORA44003 : string is not a simple SQL name Usage Notes The input value must be meet the following conditions: The name must begin with an alphabetic character. It may contain alphanumeric characters as well as the characters _, $, and # in the second and subsequent character positions. Quoted SQL names are also allowed. Quoted names must be enclosed in double quotes. Quoted names allow any characters between the quotes. Quotes inside the name are represented by two quote characters in a row, for example, "a name with "" inside" is a valid quoted name. The input parameter may have any number of leading and/or trailing white space characters. The length of the name is not checked.