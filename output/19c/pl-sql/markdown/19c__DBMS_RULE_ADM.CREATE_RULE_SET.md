---
id: 19c__DBMS_RULE_ADM.CREATE_RULE_SET
name: DBMS_RULE_ADM.CREATE_RULE_SET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.CREATE_RULE_SET

This procedure creates a rule set.

## Syntax

```sql
DBMS_RULE_ADM.CREATE_RULE_SET(
   rule_set_name       IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2  DEFAULT NULL,
   rule_set_comment    IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_set_name | VARCHAR2 | IN | The name of the rule set you are creating, specified as [ schema_name .] rule_set_name . For example, to create a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. |
| evaluation_context | VARCHAR2 | IN | An optional evaluation context name in the form [ schema_name .] evaluation_context_name , which applies to all rules in the rule set that are not associated with an evaluation context explicitly. If the schema is not specified, then the current user is the default. |
| rule_set_comment | VARCHAR2 | IN | An optional description of the rule set |

## Usage Notes

Syntax DBMS_RULE_ADM.CREATE_RULE_SET( rule_set_name IN VARCHAR2, evaluation_context IN VARCHAR2 DEFAULT NULL, rule_set_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 150-7 CREATE_RULE_SET Procedure Parameters Parameter Description rule_set_name The name of the rule set you are creating, specified as [ schema_name .] rule_set_name . For example, to create a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. evaluation_context An optional evaluation context name in the form [ schema_name .] evaluation_context_name , which applies to all rules in the rule set that are not associated with an evaluation context explicitly. If the schema is not specified, then the current user is the default. rule_set_comment An optional description of the rule set Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the rule set being created and have CREATE_RULE_SET_OBJ system privilege Have CREATE _ ANY _ RULE _ SET system privilege If an evaluation context is specified, then the rule set owner must meet at least one of the following requirements: Have EXECUTE_ON_EVALUATION_CONTEXT privilege on the evaluation context Have EXECUTE_ANY_EVALUATION_CONTEXT system privilege, and the owner of the evaluation context must not be SYS Be the evaluation context owner