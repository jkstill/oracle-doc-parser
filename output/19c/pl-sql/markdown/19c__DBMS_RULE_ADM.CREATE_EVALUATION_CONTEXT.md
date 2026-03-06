---
id: 19c__DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT
name: DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT

This procedure creates a rule evaluation context. A rule evaluation context defines external data that can be referenced in rule conditions. The external data can either exist as variables or as table data.

## Syntax

```sql
DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT(
  evaluation_context_name      IN  VARCHAR2,
  table_aliases                IN  SYS.RE$TABLE_ALIAS_LIST    DEFAULT NULL,
  variable_types               IN  SYS.RE$VARIABLE_TYPE_LIST  DEFAULT NULL,
  evaluation_function          IN  VARCHAR2                   DEFAULT NULL,
  evaluation_context_comment   IN  VARCHAR2                   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| evaluation_context_name | VARCHAR2 | IN | The name of the evaluation context you are creating, specified as [ schema_name .] evaluation_context_name . For example, to create an evaluation context named dept_ eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. |
| table_aliases | SYS.RE$TABLE_ALIAS_LIST | IN | Table aliases that specify the tables in an evaluation context. The table aliases can be used to reference tables in rule conditions. |
| variable_types | SYS.RE$VARIABLE_TYPE_LIST | IN | A list of variables for the evaluation context |
| evaluation_function | VARCHAR2 | IN | An optional function that will be called to evaluate rules using the evaluation context. It must have the same form as the DBMS_RULE.EVALUATE procedure. If the schema is not specified, then the current user is the default. See " Usage Notes " for more information about the evaluation function. |
| evaluation_context_comment | VARCHAR2 | IN | An optional description of the rule evaluation context. |

## Usage Notes

Syntax DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT( evaluation_context_name IN VARCHAR2, table_aliases IN SYS.RE$TABLE_ALIAS_LIST DEFAULT NULL, variable_types IN SYS.RE$VARIABLE_TYPE_LIST DEFAULT NULL, evaluation_function IN VARCHAR2 DEFAULT NULL, evaluation_context_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 150-5 CREATE_EVALUATION_CONTEXT Procedure Parameters Parameter Description evaluation_context_name The name of the evaluation context you are creating, specified as [ schema_name .] evaluation_context_name . For example, to create an evaluation context named dept_ eval_context in the hr schema, enter hr.dept_eval_context for this parameter. If the schema is not specified, then the current user is the default. table_aliases Table aliases that specify the tables in an evaluation context. The table aliases can be used to reference tables in rule conditions. variable_types A list of variables for the evaluation context evaluation_function An optional function that will be called to evaluate rules using the evaluation context. It must have the same form as the DBMS_RULE.EVALUATE procedure. If the schema is not specified, then the current user is the default. See " Usage Notes " for more information about the evaluation function. evaluation_context_comment An optional description of the rule evaluation context. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the evaluation context being created and have CREATE_EVALUATION_CONTEXT_OBJ system privilege Have CREATE _ ANY _ EVALUATION _ CONTEXT system privilege See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package The evaluation function must have the following signature: FUNCTION evaluation_function_name( rule_set_name IN VARCHAR2, evaluation_context IN VARCHAR2, event_context IN SYS.RE$NV_LIST DEFAULT NULL, table_values IN SYS.RE$TABLE_VALUE_LIST DEFAULT NULL, column_values IN SYS.RE$COLUMN_VALUE_LIST DEFAULT NULL, variable_values IN SYS.RE$VARIABLE_VALUE_LIST DEFAULT NULL, attribute_values IN SYS.RE$ATTRIBUTE_VALUE_LIST DEFAULT NULL, stop_on_first_hit IN BOOLEAN DEFAULT FALSE, simple_rules_only IN BOOLEAN DEFAULT FALSE, true_rules OUT SYS.RE$RULE_HIT_LIST, maybe_rules OUT SYS.RE$RULE_HIT_LIST); RETURN BINARY_INTEGER; Note: Each parameter is required and must have the specified datatype. However, you can change the names of the parameters. The return value of the function must be one of the following: DBMS_RULE_ADM.EVALUATION_SUCCESS : The user specified evaluation function completed the rule set evaluation successfully. The rules engine returns the results of the evaluation obtained by the evaluation function to the rules engine client using the DBMS_RULE.EVALUATE procedure. DBMS_RULE_ADM.EVALUATION_CONTINUE : The rules engine evaluates the rule set as if there were no evaluation function. The evaluation function is not used, and any results returned by the evaluation function are ignored. DBMS_RULE_ADM.EVALUATION_FAILURE : The user specified evaluation function failed. Rule set evaluation stops, and an error is raised. See Also: Rule TYPEs for more information about the types used with the DBMS_RULE_ADM package Note: Each parameter is required and must have the specified datatype. However, you can change the names of the parameters.