---
id: 19c__ALL_EXPRESSION_STATISTICS
name: ALL_EXPRESSION_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_EXPRESSION_STATISTICS.html
---

# ALL_EXPRESSION_STATISTICS

ALL_EXPRESSION_STATISTICS provides expression usage tracking statistics for tables that are accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table contained in the expression |
| EXPRESSION_ID | NUMBER | Expression ID of the current expression |
| SNAPSHOT | VARCHAR2(10) | Type of snapshot for the expression: LATEST : Latest snapshot CUMULATIVE : Cumulative snapshot WINDOW : Window snapshot |
| EVALUATION_COUNT | NUMBER | Number of times the expression has been evaluated |
| FIXED_COST | NUMBER | Optimizer fixed cost of evaluating the expression |
| DYNAMIC_COST | NUMBER | Optimizer dynamic cost of evaluating the expression |
| EXPRESSION_TEXT | VARCHAR2(4000) | Text of the expression |
| CREATED | DATE | Time this expression is first evaluated |
| LAST_MODIFIED | DATE | Time this expression is last evaluated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_EXPRESSION_STATISTICS provides expression usage tracking statistics for all the tables in the database. USER_EXPRESSION_STATISTICS provides expression usage tracking statistics for tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_EXPRESSION_STATISTICS " " USER_EXPRESSION_STATISTICS " " V$EXP_STATS " See Also: " DBA_EXPRESSION_STATISTICS " " USER_EXPRESSION_STATISTICS " " V$EXP_STATS "