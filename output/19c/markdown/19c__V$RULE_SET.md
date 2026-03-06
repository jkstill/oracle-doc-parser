---
id: 19c__V$RULE_SET
name: V$RULE_SET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RULE_SET.html
---

# V$RULE_SET

V$RULE_SET displays rule set statistics. This view has a row for every rule set loaded into shared memory.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) |  |
| NAME | VARCHAR2(128) |  |
| CPU_TIME | NUMBER |  |
| ELAPSED_TIME | NUMBER |  |
| FIRST_LOAD_TIME | DATE |  |
| LAST_LOAD_TIME | DATE |  |
| LAST_LOADING_TIME | NUMBER |  |
| SHARABLE_MEM | NUMBER |  |
| RELOADS | NUMBER |  |
| INVALIDATIONS | NUMBER |  |
| EVALUATIONS | NUMBER |  |
| FIRST_HIT_EVALUATIONS | NUMBER |  |
| SIMPLE_RULES_ONLY_EVALUATIONS | NUMBER |  |
| SQL_FREE_EVALUATIONS | NUMBER |  |
| SQL_EXECUTIONS | NUMBER |  |
| CONDITIONS_PROCESSED | NUMBER |  |
| TRUE_RULES | NUMBER |  |
| MAYBE_RULES | NUMBER |  |
| VARIABLE_VALUE_FUNCTION_CALLS | NUMBER |  |
| VARIABLE_METHOD_FUNCTION_CALLS | NUMBER |  |
| EVALUATION_FUNCTION_CALLS | NUMBER |  |
| RESULT_CACHE_HITS | NUMBER |  |
| IS_RESULT_CACHE | VARCHAR2(3) |  |
| RESULT_CACHE_ELEMENTS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: Querying the V$RULE_SET view may have a negative impact on performance if a database has a large library cache. Note: Querying the V$RULE_SET view may have a negative impact on performance if a database has a large library cache. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT procedure