---
id: 19c__DBMS_ASSERT.SCHEMA_NAME
name: DBMS_ASSERT.SCHEMA_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.SCHEMA_NAME

This function verifies that the input string is an existing schema name.

## Syntax

```sql
DBMS_ASSERT.SCHEMA_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Input value |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.SCHEMA_NAME ( str VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 26-6 SCHEMA_NAME Function Parameters Parameter Description str Input value Exceptions ORA44001 : Invalid schema name Usage Notes By definition, a schema name need not be just a simple SQL name. For example, " FIRST LAST " is a valid schema name. As a consequence, care must be taken to quote the output of schema name before concatenating it with SQL text.