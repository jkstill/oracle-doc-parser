---
id: 19c__DBMS_SQL.DESCRIBE_COLUMNS2
name: DBMS_SQL.DESCRIBE_COLUMNS2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DESCRIBE_COLUMNS2

This procedure describes the specified column. This is an alternative to DESCRIBE_COLUMNS Procedure.

## Syntax

```sql
DBMS_SQL.DESCRIBE_COLUMNS2 ( 
   c              IN  INTEGER, 
   col_cnt        OUT INTEGER, 
   desc_t         OUT DESC_TAB2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the columns being described. |
| col_cnt | INTEGER | OUT | Number of columns in the select list of the query. |
| desc_t | DESC_TAB2) | OUT | Describe table to fill in with the description of each of the columns of the query. This table is indexed from one to the number of elements in the select list of the query. |

## Usage Notes

Syntax DBMS_SQL.DESCRIBE_COLUMNS2 ( c IN INTEGER, col_cnt OUT INTEGER, desc_t OUT DESC_TAB2); Pragmas PRAGMA RESTRICT_REFERENCES(describe_columns2,WNDS); Parameters Table 162-21 DESCRIBE_COLUMNS2 Procedure Parameters Parameter Description c ID number of the cursor for the columns being described. col_cnt Number of columns in the select list of the query. desc_t Describe table to fill in with the description of each of the columns of the query. This table is indexed from one to the number of elements in the select list of the query.