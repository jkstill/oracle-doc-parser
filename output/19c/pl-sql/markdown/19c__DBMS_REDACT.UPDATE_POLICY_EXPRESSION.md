---
id: 19c__DBMS_REDACT.UPDATE_POLICY_EXPRESSION
name: DBMS_REDACT.UPDATE_POLICY_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.UPDATE_POLICY_EXPRESSION

This procedure updates a named Oracle Data Redaction policy expression.

## Syntax

```sql
DBMS_REDACT.UPDATE_POLICY_EXPRESSION (
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

Syntax DBMS_REDACT.UPDATE_POLICY_EXPRESSION ( policy_expression_name IN VARCHAR2, expression IN VARCHAR2, policy_expression_description IN VARCHAR2 := NULL); Parameters Table 137-15 UPDATE_POLICY_EXPRESSION Procedure Parameters Parameter Description policy_expression_name Name of the policy expression expression Definition of the policy expression policy_expression_description Description of the policy expression Exceptions ORA–28082 - The parameter parameter is invalid. ORA-28092 - The parameter parameter with value value has an error. Usage Notes You can find existing policy expressions by querying the REDACTION_EXPRESSIONS data dictionary view. Example BEGIN DBMS_REDACT.UPDATE_POLICY_EXPRESSION( policy_expression_name => 'oe_redact_pol', expression => 'SYS_CONTEXT(''USERENV'',''SESSION_USER'') != ''OE'''), policy_expression_description => 'Disables policy for user OE '); END;