---
id: 19c__V$RULE_SET_AGGREGATE_STATS
name: V$RULE_SET_AGGREGATE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-RULE_SET_AGGREGATE_STATS.html
---

# V$RULE_SET_AGGREGATE_STATS

V$RULE_SET_AGGREGATE_STATS displays statistics aggregated over all evaluations on all rule sets. This view has a row for each type of statistic.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(80) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT procedure