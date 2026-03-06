---
id: 19c__DBMS_UTILITY.EXPAND_SQL_TEXT
name: DBMS_UTILITY.EXPAND_SQL_TEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.EXPAND_SQL_TEXT

This procedure recursively replaces any view references in the input SQL query with the corresponding view subquery.

## Syntax

```sql
DBMS_UTILITY.EXPAND_SQL_TEXT (
   input_sql_text     IN           CLOB,
   output_sql_text    OUT NOCOPY   CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| input_sql_text | CLOB | IN | Input SQL query text |
| output_sql_text | NOCOPY | OUT | View-expanded query text |

## Usage Notes

Syntax DBMS_UTILITY.EXPAND_SQL_TEXT ( input_sql_text IN CLOB, output_sql_text OUT NOCOPY CLOB); Parameters Table 187-18 EXPAND_SQL_TEXT Procedure Parameters Parameter Description input_sql_text Input SQL query text output_sql_text View-expanded query text Exceptions Table 187-19 EXPAND_SQL_TEXT Procedure Exceptions Exception Description ORA-00942 Current user does not have select privileges on all the views and tables recursively referenced in the input_sql_text ORA-24251 input_sql_text is not a SELECT statement ORA-00900 Input is not valid ORA-29477 Input LOB size exceeds maximum size of 4GB -1 Usage Notes The expanded and merged SQL statement text is copied to output_sql_text on successful completion. The resulting query text only contains references to underlying tables and is semantically equivalent with some caveats: If there are invoker rights functions called from any of the views, they may be called as a different user in the resulting query text if the view owner is different from the user who will eventually compile/run the expanded SQL text. The VPD policy expands differently if there is a function supplied to generate the dynamic WHERE clause. This function would return differently, for example, if the userid caused the expansion to be different. If there are references to remote objects, results are undetermined.