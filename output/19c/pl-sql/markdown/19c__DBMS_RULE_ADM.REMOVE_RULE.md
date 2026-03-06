---
id: 19c__DBMS_RULE_ADM.REMOVE_RULE
name: DBMS_RULE_ADM.REMOVE_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.REMOVE_RULE

This procedure removes the specified rule from the specified rule set.

## Syntax

```sql
DBMS_RULE_ADM.REMOVE_RULE(
   rule_name                IN  VARCHAR2,
   rule_set_name            IN  VARCHAR2,
   evaluation_context       IN  VARCHAR2  DEFAULT NULL,
   all_evaluation_contexts  IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule you are removing from the rule set, specified as [ schema_name .] rule_name . For example, to remove a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. |
| rule_set_name | VARCHAR2 | IN | The name of the rule set from which you are removing the rule, specified as [ schema_name .] rule_set_name . For example, to remove the rule from a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. |
| evaluation_context_name |  |  | The name of the evaluation context associated with the rule you are removing, specified as [ schema_name .] evaluation_context_name . For example, to specify an evaluation context named dept_eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. If an evaluation context was specified for the rule you are removing when you added the rule to the rule set using the ADD_RULE procedure, then specify the same evaluation context. If you added the same rule more than once with different evaluation contexts, then specify the rule with the evaluation context you want to remove. If you specify an evaluation context that is not associated with the rule, then the procedure raises an error. Specify NULL if you did not specify an evaluation context when you added the rule to the rule set. If you specify NULL and there are one or more evaluation contexts associated with the rule, then the procedure raises an error. |
| all_evaluation_contexts | BOOLEAN | IN | If TRUE , then the procedure removes the rule from the rule set with all of its associated evaluation contexts. If FALSE , then the procedure only removes the rule with the specified evaluation context. This parameter is relevant only if the same rule is added more than once to the rule set with different evaluation contexts. |

## Usage Notes

Syntax DBMS_RULE_ADM.REMOVE_RULE( rule_name IN VARCHAR2, rule_set_name IN VARCHAR2, evaluation_context IN VARCHAR2 DEFAULT NULL, all_evaluation_contexts IN BOOLEAN DEFAULT FALSE); Parameters Table 150-15 REMOVE_RULE Procedure Parameters Parameter Description rule_name The name of the rule you are removing from the rule set, specified as [ schema_name .] rule_name . For example, to remove a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. rule_set_name The name of the rule set from which you are removing the rule, specified as [ schema_name .] rule_set_name . For example, to remove the rule from a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. evaluation_context_name The name of the evaluation context associated with the rule you are removing, specified as [ schema_name .] evaluation_context_name . For example, to specify an evaluation context named dept_eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. If an evaluation context was specified for the rule you are removing when you added the rule to the rule set using the ADD_RULE procedure, then specify the same evaluation context. If you added the same rule more than once with different evaluation contexts, then specify the rule with the evaluation context you want to remove. If you specify an evaluation context that is not associated with the rule, then the procedure raises an error. Specify NULL if you did not specify an evaluation context when you added the rule to the rule set. If you specify NULL and there are one or more evaluation contexts associated with the rule, then the procedure raises an error. all_evaluation_contexts If TRUE , then the procedure removes the rule from the rule set with all of its associated evaluation contexts. If FALSE , then the procedure only removes the rule with the specified evaluation context. This parameter is relevant only if the same rule is added more than once to the rule set with different evaluation contexts. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Have ALTER_ON_RULE_SET privilege on the rule set Have ALTER _ ANY _ RULE _ SET system privilege Be the owner of the rule set Note: This procedure does not drop a rule from the database. To drop a rule from the database, use the DROP_RULE procedure. Note: This procedure does not drop a rule from the database. To drop a rule from the database, use the DROP_RULE procedure.