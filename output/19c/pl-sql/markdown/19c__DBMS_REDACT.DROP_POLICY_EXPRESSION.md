---
id: 19c__DBMS_REDACT.DROP_POLICY_EXPRESSION
name: DBMS_REDACT.DROP_POLICY_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDACT
tags: [dbms_redact]
source_file: DBMS_REDACT.html
---

# DBMS_REDACT.DROP_POLICY_EXPRESSION

This procedure drops a named policy expression.

## Syntax

```sql
DBMS_REDACT.DROP_POLICY_EXPRESSION (
   policy_expression_name       IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_expression_name | VARCHAR2) | IN | Name of the policy expression |

## Usage Notes

Syntax DBMS_REDACT.DROP_POLICY_EXPRESSION ( policy_expression_name IN VARCHAR2); Parameters Table 137-12 DROP_POLICY_EXPRESSION Procedure Parameters Parameter Description policy_expression_name Name of the policy expression Exceptions ORA–28082 - The parameter parameter is invalid. ORA-28092 - The parameter parameter with value value has an error. Usage Notes You can find existing Data Redaction policy expressions by querying the REDACTION_EXPRESSIONS data dictionary view. Example BEGIN DBMS_REDACT.DROP_POLICY_EXPRESSION( policy_expression_name => 'oe_redact_pol'); END;