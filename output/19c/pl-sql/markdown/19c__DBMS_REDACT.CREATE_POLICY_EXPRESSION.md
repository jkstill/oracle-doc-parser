---
id: 19c__DBMS_REDACT.CREATE_POLICY_EXPRESSION
name: DBMS_REDACT.CREATE_POLICY_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.CREATE_POLICY_EXPRESSION

This procedure creates a named Oracle Data Redaction policy expression.

## Syntax

```sql
DBMS_REDACT.CREATE_POLICY_EXPRESSION (
   policy_expression_name          IN    VARCHAR2,
   expression                      IN    VARCHAR2,
   policy_expression_description   IN    VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_expression_name | VARCHAR2 | IN | Name of the policy expression |
| expression | VARCHAR2 | IN | Definition of the policy expression |
| policy_expression_description | VARCHAR2 | IN | Description of the policy expression |

## Usage Notes

Syntax DBMS_REDACT.CREATE_POLICY_EXPRESSION ( policy_expression_name IN VARCHAR2, expression IN VARCHAR2, policy_expression_description IN VARCHAR2 := NULL); Parameters Table 137-9 CREATE_POLICY_EXPRESSION Procedure Parameters Parameter Description policy_expression_name Name of the policy expression expression Definition of the policy expression policy_expression_description Description of the policy expression Exceptions ORA–28082 - The parameter parameter is invalid. ORA-28092 - The parameter parameter with value value has an error. Usage Notes See Operating Procedures for more information regarding function types and function parameters with related examples. After you create a policy expression, you can associate it with a redacted table or view column by running the DBMS_REDACT.APPLY_POLICY_EXPR_TO_COL procedure. To find existing redacted columns, query the REDACTION_COLUMNS data dictionary view. Example BEGIN DBMS_REDACT.CREATE_POLICY_EXPRESSION( policy_expression_name => 'oe_redact_pol', expression => 'SYS_CONTEXT(''USERENV'',''SESSION_USER'') = ''OE'''), policy_expression_description => 'Enables policy for user OE '); END;