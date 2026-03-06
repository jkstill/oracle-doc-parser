---
id: 19c__DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT
name: DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT

This procedure drops a rule evaluation context.

## Syntax

```sql
DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT(
   evaluation_context_name  IN  VARCHAR2,
   force                    IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| evaluation_context_name | VARCHAR2 | IN | The name of the evaluation context you are dropping, specified as [ schema_name .] evaluation_context_name . For example, to drop an evaluation context named dept_eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. |
| force | BOOLEAN | IN | If TRUE , then the procedure removes the rule evaluation context from all rules and rule sets that use it. If FALSE and no rules or rule sets use the rule evaluation context, then the procedure drops the rule evaluation context. If FALSE and one or more rules or rule sets use the rule evaluation context, then the procedure raises an exception. Caution: Setting force to TRUE can result in rules and rule sets that do not have an evaluation context. If neither a rule nor the rule set it is in has an evaluation context, and no evaluation context was specified for the rule by the ADD_RULE procedure, then the rule cannot be evaluated. |

## Usage Notes

Syntax DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT( evaluation_context_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 150-8 DROP_EVALUATION_CONTEXT Procedure Parameters Parameter Description evaluation_context_name The name of the evaluation context you are dropping, specified as [ schema_name .] evaluation_context_name . For example, to drop an evaluation context named dept_eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. force If TRUE , then the procedure removes the rule evaluation context from all rules and rule sets that use it. If FALSE and no rules or rule sets use the rule evaluation context, then the procedure drops the rule evaluation context. If FALSE and one or more rules or rule sets use the rule evaluation context, then the procedure raises an exception. Caution: Setting force to TRUE can result in rules and rule sets that do not have an evaluation context. If neither a rule nor the rule set it is in has an evaluation context, and no evaluation context was specified for the rule by the ADD_RULE procedure, then the rule cannot be evaluated. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the evaluation context Have DROP _ ANY _ EVALUATION _ CONTEXT system privilege