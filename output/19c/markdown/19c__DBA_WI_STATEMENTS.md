---
id: 19c__DBA_WI_STATEMENTS
name: DBA_WI_STATEMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_WI_STATEMENTS.html
---

# DBA_WI_STATEMENTS

Each row in DBA_WI_STATEMENTS describes a statement (SQL or PL/SQL) that is part of the template with identifier TEMPLATE_ID , which has been found in the workload that is related to the Workload Intelligence job whose identifier is equal to JOB_ID .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_ID | NUMBER | The identifier of the job in the workload of which the given statement has been found |
| TEMPLATE_ID | NUMBER | The identifier of the template in the given job to which the current statement belongs |
| SEQUENCE_NUMBER | NUMBER | A number that indicates the order of the current statement in the given template |
| SQL_TEXT | CLOB | The SQL text associated with the current statement. Note that although multiple SQL statements can be classified to the same template, only one row is stored that represents them all. This row corresponds to the first instance of the given template that is found during parsing of the workload. |

## Usage Notes

A template may consist of multiple statements, for example, if it represents a transaction. In this case, there is one row in this view for every one of these statements. These statements are ordered, based on the order defined by the corresponding transaction. Column SEQUENCE_NUMBER is used to describe this order.