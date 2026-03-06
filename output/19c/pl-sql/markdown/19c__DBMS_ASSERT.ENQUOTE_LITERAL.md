---
id: 19c__DBMS_ASSERT.ENQUOTE_LITERAL
name: DBMS_ASSERT.ENQUOTE_LITERAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ASSERT
tags: [dbms_assert]
source_file: DBMS_ASSERT.html
---

# DBMS_ASSERT.ENQUOTE_LITERAL

This function adds leading and trailing single quotes to a string literal.

## Syntax

```sql
DBMS_ASSERT.ENQUOTE_LITERAL (
   str            VARCHAR2) 
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| str | VARCHAR2) | IN | String to enquote |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_ASSERT.ENQUOTE_LITERAL ( str VARCHAR2) RETURN VARCHAR2; Parameters Table 26-2 ENQUOTE_LITERAL Function Parameters Parameter Description str String to enquote Usage Notes Verify that all single quotes except leading and trailing characters are paired with adjacent single quotes. No additional quotes are added if the name was already in quotes.