---
id: 19c__DBMS_SQL.DEFINE_COLUMN
name: DBMS_SQL.DEFINE_COLUMN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_COLUMN

This procedure defines a column to be selected from the given cursor. This procedure is only used with SELECT cursors.

## Syntax

```sql
DBMS_SQL.DEFINE_COLUMN (
   c              IN INTEGER,
   position       IN INTEGER,
   column         IN <datatype>);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the row being defined to be selected |
| position | INTEGER | IN | Relative position of the column in the row being defined.The first column in a statement has position 1. |
| column | IN | IN | Value of the column being defined. The type of this value determines the type for the column being defined. |
| column_size |  |  | Maximum expected size of the column value in bytes for columns of type VARCHAR2 . |

## Usage Notes

The column being defined is identified by its relative position in the SELECT list of the statement in the given cursor. The type of the COLUMN value determines the type of the column being defined. See also the DEFINE_COLUMN_CHAR Procedure , DEFINE_COLUMN_LONG Procedure , DEFINE_COLUMN_RAW Procedure and DEFINE_COLUMN_ROWID Procedure . Syntax DBMS_SQL.DEFINE_COLUMN ( c IN INTEGER, position IN INTEGER, column IN <datatype>); Where < datatype > can be any one of the following types: BINARY_DOUBLE BINARY_FLOAT BFILE BLOB CLOB CHARACTER SET ANY_CS DATE DSINTERVAL_UNCONSTRAINED NUMBER TIME_UNCONSTRAINED TIME_TZ_UNCONSTRAINED TIMESTAMP_LTZ_UNCONSTRAINED TIMESTAMP_TZ_UNCONSTRAINED TIMESTAMP_UNCONSTRAINED UROWID YMINTERVAL_UNCONSTRAINED user-defined object types collections (VARRAYs and nested tables) REFs Opaque types Note that DEFINE_COLUMN is overloaded to accept different datatypes. The following syntax is also supported for the DEFINE_COLUMN procedure: DBMS_SQL.DEFINE_COLUMN ( c IN INTEGER, position IN INTEGER, column IN VARCHAR2 CHARACTER SET ANY_CS, column_size IN INTEGER); Pragmas pragma restrict_references(define_column,RNDS,WNDS); Parameters Table 162-15 DEFINE_COLUMN Procedure Parameters Parameter Description c ID number of the cursor for the row being defined to be selected position Relative position of the column in the row being defined.The first column in a statement has position 1. column Value of the column being defined. The type of this value determines the type for the column being defined. column_size Maximum expected size of the column value in bytes for columns of type VARCHAR2 . Usage Notes When using character length semantics the maximum number of bytes that can be returned for a column value of type VARCHAR2 is calculated as: column_size * maximum character byte size for the current character set. For example, specifying the column_size as 10 means that a maximum of 30 (10*3) bytes can be returned when using character length semantics with a UTF8 character set regardless of the number of characters this represents.