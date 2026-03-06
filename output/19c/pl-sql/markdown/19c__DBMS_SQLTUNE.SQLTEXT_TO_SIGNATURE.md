---
id: 19c__DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE
name: DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE

This function returns a SQL text's signature. The signature can be used to identify SQL text in dba_sql_profiles .

## Syntax

```sql
DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE (
  sql_text    IN CLOB,  
  force_match IN BOOLEAN  := FALSE)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | SQL text whose signature is required. Required. |
| force_match | BOOLEAN | IN | If TRUE , this returns a signature that supports SQL matching with literal values transformed into bind variables. If FALSE , returns the signature based on the text with literals not transformed |

**Returns:** `NUMBER`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE ( sql_text IN CLOB, force_match IN BOOLEAN := FALSE) RETURN NUMBER; Parameters Table 169-47 SQLTEXT_TO_SIGNATURE Function Parameters Parameter Description sql_text SQL text whose signature is required. Required. force_match If TRUE , this returns a signature that supports SQL matching with literal values transformed into bind variables. If FALSE , returns the signature based on the text with literals not transformed Return Values This function returns the signature of the specified SQL text.