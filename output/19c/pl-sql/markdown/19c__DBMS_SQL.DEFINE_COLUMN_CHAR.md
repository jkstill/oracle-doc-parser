---
id: 19c__DBMS_SQL.DEFINE_COLUMN_CHAR
name: DBMS_SQL.DEFINE_COLUMN_CHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_COLUMN_CHAR

This procedure defines a column with CHAR data to be selected from the given cursor. This procedure is only used with SELECT cursors.

## Syntax

```sql
DBMS_SQL.DEFINE_COLUMN_CHAR (
   c              IN INTEGER,
   position       IN INTEGER,
   column         IN CHAR CHARACTER SET ANY_CS,
   column_size    IN INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the row being defined to be selected |
| position | INTEGER | IN | Relative position of the column in the row being defined.The first column in a statement has position 1. |
| column | CHAR | IN | Value of the column being defined. The type of this value determines the type for the column being defined. |
| column_size | INTEGER) | IN | Maximum expected size of the column value in characters for columns of type CHAR . |

## Usage Notes

The column being defined is identified by its relative position in the SELECT list of the statement in the given cursor. The type of the COLUMN value determines the type of the column being defined. See also the DEFINE_COLUMN Procedures , DEFINE_COLUMN_LONG Procedure , DEFINE_COLUMN_RAW Procedure and DEFINE_COLUMN_ROWID Procedure . Syntax DBMS_SQL.DEFINE_COLUMN_CHAR ( c IN INTEGER, position IN INTEGER, column IN CHAR CHARACTER SET ANY_CS, column_size IN INTEGER); Pragmas pragma restrict_references(define_column,RNDS,WNDS); Parameters Table 162-16 DEFINE_COLUMN_CHAR Procedure Parameters Parameter Description c ID number of the cursor for the row being defined to be selected position Relative position of the column in the row being defined.The first column in a statement has position 1. column Value of the column being defined. The type of this value determines the type for the column being defined. column_size Maximum expected size of the column value in characters for columns of type CHAR .