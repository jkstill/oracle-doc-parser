---
id: 19c__DBMS_RULE_ADM.CREATE_RULE
name: DBMS_RULE_ADM.CREATE_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.CREATE_RULE

This procedure creates a rule.

## Syntax

```sql
DBMS_RULE_ADM.CREATE_RULE(
   rule_name           IN  VARCHAR2,
   condition           IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2        DEFAULT NULL,
   action_context      IN  SYS.RE$NV_LIST  DEFAULT NULL,
   rule_comment        IN  VARCHAR2        DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule you are creating, specified as [ schema_name .] rule_name . For example, to create a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. |
| condition | VARCHAR2 | IN | The condition to be associated with the rule. A condition evaluates to TRUE or FALSE and can be any condition allowed in the WHERE clause of a SELECT statement. For example, the following is a valid rule condition: department_id = 30 Ensure that the proper case is used for text in rule conditions. Note: Do not include the word "WHERE" in the condition. |
| evaluation_context | VARCHAR2 | IN | An optional evaluation context name in the form [ schema_name .] evaluation_context_name , which is associated with the rule. If the schema is not specified, then the current user is the default. If evaluation_context is not specified, then the rule inherits the evaluation context from its rule set. |
| action_context | SYS.RE$NV_LIST | IN | The action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. |
| rule_comment | VARCHAR2 | IN | An optional description of the rule |

## Usage Notes

Syntax DBMS_RULE_ADM.CREATE_RULE( rule_name IN VARCHAR2, condition IN VARCHAR2, evaluation_context IN VARCHAR2 DEFAULT NULL, action_context IN SYS.RE$NV_LIST DEFAULT NULL, rule_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 150-6 CREATE_RULE Procedure Parameters Parameter Description rule_name The name of the rule you are creating, specified as [ schema_name .] rule_name . For example, to create a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. condition The condition to be associated with the rule. A condition evaluates to TRUE or FALSE and can be any condition allowed in the WHERE clause of a SELECT statement. For example, the following is a valid rule condition: department_id = 30 Ensure that the proper case is used for text in rule conditions. Note: Do not include the word "WHERE" in the condition. evaluation_context An optional evaluation context name in the form [ schema_name .] evaluation_context_name , which is associated with the rule. If the schema is not specified, then the current user is the default. If evaluation_context is not specified, then the rule inherits the evaluation context from its rule set. action_context The action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. rule_comment An optional description of the rule Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the rule being created and have the CREATE_RULE_OBJ system privilege Have CREATE _ ANY _ RULE system privilege If an evaluation context is specified, then the rule owner must meet at least one of the following requirements: Have EXECUTE_ON_EVALUATION_CONTEXT privilege on the evaluation context Have EXECUTE_ANY_EVALUATION_CONTEXT system privilege, and the owner of the evaluation context must not be SYS . Be the evaluation context owner Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context. See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package