---
id: 19c__DBMS_SQL.DESCRIBE_COLUMNS
name: DBMS_SQL.DESCRIBE_COLUMNS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DESCRIBE_COLUMNS

This procedure describes the columns for a cursor opened and parsed through DBMS_SQL .

## Syntax

```sql
DBMS_SQL.DESCRIBE_COLUMNS ( 
   c              IN  INTEGER, 
   col_cnt        OUT INTEGER, 
   desc_t         OUT DESC_TAB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the columns being described |
| col_cnt | INTEGER | OUT | Number of columns in the select list of the query |
| desc_t | DESC_TAB) | OUT | Describe table to fill in with the description of each of the columns of the query |

## Usage Notes

Syntax DBMS_SQL.DESCRIBE_COLUMNS ( c IN INTEGER, col_cnt OUT INTEGER, desc_t OUT DESC_TAB); Parameters Table 162-20 DESCRIBE_COLUMNS Procedure Parameters Parameter Description c ID number of the cursor for the columns being described col_cnt Number of columns in the select list of the query desc_t Describe table to fill in with the description of each of the columns of the query