---
id: 19c__DBMS_ASSERT.SQL_OBJECT_NAME
name: DBMS_ASSERT.SQL_OBJECT_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.SQL_OBJECT_NAME

This function verifies that the input parameter string is a qualified SQL identifier of an existing SQL object.

## Syntax

```sql
DBMS_ASSERT.SQL_OBJECT_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Input value |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.SQL_OBJECT_NAME ( str VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; Parameters Table 26-8 SQL_OBJECT_NAME Function Parameters Parameter Description str Input value Exceptions ORA44002 : Invalid object name Usage Notes The use of synonyms requires that the base object exists.