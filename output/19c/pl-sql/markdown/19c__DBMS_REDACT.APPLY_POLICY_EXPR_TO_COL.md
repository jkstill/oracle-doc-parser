---
id: 19c__DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL
name: DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL

This procedure associates a named Oracle Data Redaction policy expression with a redacted column from a table or view.

## Syntax

```sql
DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL (
   object_schema                IN VARCHAR2 := NULL,
   object_name                  IN VARCHAR2,
   column_name                  IN VARCHAR2, 
   policy_expression_name       IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Name of the schema that contains the redacted column |
| object_name | VARCHAR2 | IN | Name of the object (table or view) that contains the redacted column |
| column_name | VARCHAR2 | IN | Name of the redacted column to which the policy expression is applied |
| policy_expression_name | VARCHAR2 | IN | Name of the policy expression |

## Usage Notes

Syntax DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL ( object_schema IN VARCHAR2 := NULL, object_name IN VARCHAR2, column_name IN VARCHAR2, policy_expression_name IN VARCHAR2 := NULL); Parameters Table 137-8 APPLY_POLICY_EXPR_TO_COL Procedure Parameters Parameter Description object_schema Name of the schema that contains the redacted column object_name Name of the object (table or view) that contains the redacted column column_name Name of the redacted column to which the policy expression is applied policy_expression_name Name of the policy expression Exceptions ORA-28068 - The object object does not have a Data Redaction policy. ORA–28082 - The parameter parameter is invalid. ORA-28092 - The parameter parameter with value value has an error. Usage Notes You can find existing Data Redaction policy expressions by querying the REDACTION_EXPRESSIONS data dictionary view. To find columns that have been redacted, query the REDACTION_COLUMNS data dictionary view. Example BEGIN DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL( object_schema => 'OE', object_name => 'CUSTOMERS', column_name => 'INCOME_LEVEL', policy_expression_name => 'oe_redact_pol'); END;