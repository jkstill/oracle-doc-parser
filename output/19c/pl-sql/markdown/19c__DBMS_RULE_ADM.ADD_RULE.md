---
id: 19c__DBMS_RULE_ADM.ADD_RULE
name: DBMS_RULE_ADM.ADD_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.ADD_RULE

This procedure adds the specified rule to the specified rule set.

## Syntax

```sql
DBMS_RULE_ADM.ADD_RULE(
   rule_name           IN  VARCHAR2,
   rule_set_name       IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2   DEFAULT NULL,
   rule_comment        IN  VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule you are adding to the rule set, specified as [ schema_name .] rule_name . For example, to add a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. |
| rule_set_name | VARCHAR2 | IN | The name of the rule set to which you are adding the rule, specified as [ schema_name .] rule_set_name . For example, to add the rule to a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. |
| evaluation_context | VARCHAR2 | IN | An evaluation context name in the form [ schema_name .] evaluation_context_name . If the schema is not specified, then the current user is the default. Only specify an evaluation context if the rule itself does not have an evaluation context and you do not want to use the rule set's evaluation context for the rule. |
| rule_comment | VARCHAR2 | IN | Optional description, which can contain the reason for adding the rule to the rule set |

## Usage Notes

Syntax DBMS_RULE_ADM.ADD_RULE( rule_name IN VARCHAR2, rule_set_name IN VARCHAR2, evaluation_context IN VARCHAR2 DEFAULT NULL, rule_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 150-2 ADD_RULE Procedure Parameters Parameter Description rule_name The name of the rule you are adding to the rule set, specified as [ schema_name .] rule_name . For example, to add a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. rule_set_name The name of the rule set to which you are adding the rule, specified as [ schema_name .] rule_set_name . For example, to add the rule to a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. evaluation_context An evaluation context name in the form [ schema_name .] evaluation_context_name . If the schema is not specified, then the current user is the default. Only specify an evaluation context if the rule itself does not have an evaluation context and you do not want to use the rule set's evaluation context for the rule. rule_comment Optional description, which can contain the reason for adding the rule to the rule set Usage Notes To run this procedure, a user must meet at least one of the following requirements: Have ALTER_ON_RULE_SET privilege on the rule set Have ALTER _ ANY _ RULE _ SET system privilege Be the owner of the rule set Also, the rule set owner must meet at least one of the following requirements: Have EXECUTE_ON_RULE privilege on the rule Have EXECUTE _ ANY _ RULE system privilege Be the rule owner If the rule has no evaluation context and no evaluation context is specified when you run this procedure, then the rule uses the evaluation context associated with the rule set. In such a case, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context. If an evaluation context is specified, then the rule set owner must meet at least one of the following requirements: Have EXECUTE_ON_EVALUATION_CONTEXT privilege on the evaluation context Have EXECUTE_ANY_EVALUATION_CONTEXT system privilege, and the owner of the evaluation context must not be SYS Be the evaluation context owner Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context.