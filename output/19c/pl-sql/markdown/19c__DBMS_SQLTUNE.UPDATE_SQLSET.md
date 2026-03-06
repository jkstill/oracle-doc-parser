---
id: 19c__DBMS_SQLTUNE.UPDATE_SQLSET
name: DBMS_SQLTUNE.UPDATE_SQLSET
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.UPDATE_SQLSET

This overloaded procedure updates selected fields for SQL statements in a SQL tuning set.

## Syntax

```sql
DBMS_SQLTUNE.UPDATE_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sql_id           IN  VARCHAR2,
   attribute_name   IN  VARCHAR2,
   attribute_value  IN  VARCHAR2 := NULL);

DBMS_SQLTUNE.UPDATE_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sql_id           IN  VARCHAR2,
   attribute_name   IN  VARCHAR2,
   attribute_value IN NUMBER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set. |
| sql_id | VARCHAR2 | IN | Specifies the identifier of the SQL statement to be updated. |
| plan_hash value |  |  | Specifies the hash value of the execution plan for a SQL statement. Use this parameter when you want to update the attribute for a specific plan for a statement, but not all plans for the statement. |
| attribute_name | VARCHAR2 | IN | Specifies the name of the attribute to be modified. You can update the text field for MODULE , ACTION , PARSING_SCHEMA_NAME , and OTHER . The only numerical field that you can update is PRIORITY . If a statement has multiple plans, then the procedure changes the attribute value for all plans. |
| attribute_value | VARCHAR2 | IN | Specifies the new value of the attribute. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.UPDATE_SQLSET ( sqlset_name IN VARCHAR2, sql_id IN VARCHAR2, attribute_name IN VARCHAR2, attribute_value IN VARCHAR2 := NULL); DBMS_SQLTUNE.UPDATE_SQLSET ( sqlset_name IN VARCHAR2, sql_id IN VARCHAR2, attribute_name IN VARCHAR2, attribute_value IN NUMBER := NULL); Parameters Table 169-50 UPDATE_SQLSET Procedure Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set. sql_id Specifies the identifier of the SQL statement to be updated. plan_hash value Specifies the hash value of the execution plan for a SQL statement. Use this parameter when you want to update the attribute for a specific plan for a statement, but not all plans for the statement. attribute_name Specifies the name of the attribute to be modified. You can update the text field for MODULE , ACTION , PARSING_SCHEMA_NAME , and OTHER . The only numerical field that you can update is PRIORITY . If a statement has multiple plans, then the procedure changes the attribute value for all plans. attribute_value Specifies the new value of the attribute.