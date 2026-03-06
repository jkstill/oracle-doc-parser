---
id: 19c__DBMS_RULE_ADM.ALTER_RULE
name: DBMS_RULE_ADM.ALTER_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.ALTER_RULE

This procedure changes one or more aspects of the specified rule.

## Syntax

```sql
DBMS_RULE_ADM.ALTER_RULE(
   rule_name                  IN  VARCHAR2,
   condition                  IN  VARCHAR2        DEFAULT NULL,
   evaluation_context         IN  VARCHAR2        DEFAULT NULL,
   remove_evaluation_context  IN  BOOLEAN         DEFAULT FALSE,
   action_context             IN  SYS.RE$NV_LIST  DEFAULT NULL,
   remove_action_context      IN  BOOLEAN         DEFAULT FALSE,
   rule_comment               IN  VARCHAR2        DEFAULT NULL,
   remove_rule_comment        IN  BOOLEAN         DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | The name of the rule you are altering, specified as [ schema_name .] rule_name . For example, to alter a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. |
| condition | VARCHAR2 | IN | The condition to be associated with the rule. If non- NULL , then the procedure replaces the existing condition of the rule with the specified condition. |
| evaluation_context | VARCHAR2 | IN | An evaluation context name in the form [ schema_name .] evaluation_context_name . If the schema is not specified, then the current user is the default. If non- NULL , then the procedure replaces the existing evaluation context of the rule with the specified evaluation context. |
| remove_evaluation_context | BOOLEAN | IN | If TRUE , then the procedure sets the evaluation context for the rule to NULL , which effectively removes the evaluation context from the rule. If FALSE , then the procedure retains any evaluation context for the specified rule. If the evaluation_context parameter is non- NULL , then this parameter should be set to FALSE . |
| action_context | SYS.RE$NV_LIST | IN | If non- NULL , then the procedure changes the action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. |
| remove_action_context | BOOLEAN | IN | If TRUE , then the procedure sets the action context for the rule to NULL , which effectively removes the action context from the rule. If FALSE , then the procedure retains any action context for the specified rule. If the action_context parameter is non- NULL , then this parameter should be set to FALSE . |
| rule_comment | VARCHAR2 | IN | If non- NULL , then the existing comment of the rule is replaced by the specified comment. |
| remove_rule_comment | BOOLEAN | IN | If TRUE , then the procedure sets the comment for the rule to NULL , which effectively removes the comment from the rule. If FALSE , then the procedure retains any comment for the specified rule. If the rule_comment parameter is non- NULL , then this parameter should be set to FALSE . |

## Usage Notes

Syntax DBMS_RULE_ADM.ALTER_RULE( rule_name IN VARCHAR2, condition IN VARCHAR2 DEFAULT NULL, evaluation_context IN VARCHAR2 DEFAULT NULL, remove_evaluation_context IN BOOLEAN DEFAULT FALSE, action_context IN SYS.RE$NV_LIST DEFAULT NULL, remove_action_context IN BOOLEAN DEFAULT FALSE, rule_comment IN VARCHAR2 DEFAULT NULL, remove_rule_comment IN BOOLEAN DEFAULT FALSE); Parameters Table 150-4 ALTER_RULE Procedure Parameters Parameter Description rule_name The name of the rule you are altering, specified as [ schema_name .] rule_name . For example, to alter a rule named all_a in the hr schema, enter hr.all_a for this parameter. If the schema is not specified, then the current user is the default. condition The condition to be associated with the rule. If non- NULL , then the procedure replaces the existing condition of the rule with the specified condition. evaluation_context An evaluation context name in the form [ schema_name .] evaluation_context_name . If the schema is not specified, then the current user is the default. If non- NULL , then the procedure replaces the existing evaluation context of the rule with the specified evaluation context. remove_evaluation_context If TRUE , then the procedure sets the evaluation context for the rule to NULL , which effectively removes the evaluation context from the rule. If FALSE , then the procedure retains any evaluation context for the specified rule. If the evaluation_context parameter is non- NULL , then this parameter should be set to FALSE . action_context If non- NULL , then the procedure changes the action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. remove_action_context If TRUE , then the procedure sets the action context for the rule to NULL , which effectively removes the action context from the rule. If FALSE , then the procedure retains any action context for the specified rule. If the action_context parameter is non- NULL , then this parameter should be set to FALSE . rule_comment If non- NULL , then the existing comment of the rule is replaced by the specified comment. remove_rule_comment If TRUE , then the procedure sets the comment for the rule to NULL , which effectively removes the comment from the rule. If FALSE , then the procedure retains any comment for the specified rule. If the rule_comment parameter is non- NULL , then this parameter should be set to FALSE . Usage Notes To run this procedure, a user must meet at least one of the following requirements: Have ALTER_ON_RULE privilege on the rule Have ALTER _ ANY _ RULE system privilege Be the owner of the rule being altered If an evaluation context is specified, then the rule owner must meet at least one of the following requirements: Have EXECUTE_ON_EVALUATION_CONTEXT privilege on the evaluation context Have EXECUTE_ANY_EVALUATION_CONTEXT system privilege, and the owner of the evaluation context must not be SYS Be the evaluation context owner Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context. See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package