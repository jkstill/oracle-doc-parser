---
id: 19c__ALL_EVALUATION_CONTEXT_VARS
name: ALL_EVALUATION_CONTEXT_VARS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_EVALUATION_CONTEXT_VARS.html
---

# ALL_EVALUATION_CONTEXT_VARS

ALL_EVALUATION_CONTEXT_VARS describes the variables in the rule evaluation contexts accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVALUATION_CONTEXT_OWNER | VARCHAR2(128) | Owner of the evaluation context |
| EVALUATION_CONTEXT_NAME | VARCHAR2(128) | Name of the evaluation context |
| VARIABLE_NAME | VARCHAR2(128) | Name of a variable in the evaluation context |
| VARIABLE_TYPE | VARCHAR2(4000) | Datatype of the variable |
| VARIABLE_VALUE_FUNCTION | VARCHAR2(4000) | Function used to retrieve the value of the variable; NULL for variables that are not implicit |
| VARIABLE_METHOD_FUNCTION | VARCHAR2(228) | Function used to retrieve the result of method invocation on the variable. Such a function can speed up evaluation, if there are many simple rules that invoke the method on the variable. |

## Usage Notes

Related Views DBA_EVALUATION_CONTEXT_VARS describes the variables in all rule evaluation contexts in the database. USER_EVALUATION_CONTEXT_VARS describes the variables in the rule evaluation contexts owned by the current user. This view does not display the EVALUATION_CONTEXT_OWNER column. See Also: " DBA_EVALUATION_CONTEXT_VARS " " USER_EVALUATION_CONTEXT_VARS " See Also: " DBA_EVALUATION_CONTEXT_VARS " " USER_EVALUATION_CONTEXT_VARS "