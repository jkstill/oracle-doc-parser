---
id: 19c__DBMS_ASSERT.NOOP
name: DBMS_ASSERT.NOOP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.NOOP

This function returns the value without any checking.

## Syntax

```sql
DBMS_ASSERT.NOOP (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2 | IN | Input value |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.NOOP ( str VARCHAR2 CHARACTER SET ANY_CS) RETURN VARCHAR2 CHARACTER SET str%CHARSET; DBMS_ASSERT.NOOP ( str CLOB CHARACTER SET ANY_CS) RETURN CLOB CHARACTER SET str%CHARSET; Parameters Table 26-4 NOOP Function Parameters Parameter Description str Input value