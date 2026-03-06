---
id: 19c__DBMS_SQL.DEFINE_COLUMN_ROWID
name: DBMS_SQL.DEFINE_COLUMN_ROWID
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_COLUMN_ROWID

This procedure defines a column of type ROWID to be selected from the given cursor. This procedure is only used with SELECT cursors.

## Syntax

```sql
DBMS_SQL.DEFINE_COLUMN_ROWID (
   c              IN INTEGER,
   position       IN INTEGER,
   column         IN ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the row being defined to be selected |
| position | INTEGER | IN | Relative position of the column in the row being defined.The first column in a statement has position 1. |
| column | ROWID) | IN | Value of the column being defined. The type of this value determines the type for the column being defined. |

## Usage Notes

The column being defined is identified by its relative position in the SELECT list of the statement in the given cursor. The type of the COLUMN value determines the type of the column being defined. See also the DEFINE_COLUMN Procedures , DEFINE_COLUMN_CHAR Procedure , DEFINE_COLUMN_LONG Procedure and DEFINE_COLUMN_RAW Procedure . Syntax DBMS_SQL.DEFINE_COLUMN_ROWID ( c IN INTEGER, position IN INTEGER, column IN ROWID); Pragmas pragma restrict_references(define_column,RNDS,WNDS); Parameters Table 162-19 DEFINE_COLUMN_ROWID Procedure Parameters Parameter Description c ID number of the cursor for the row being defined to be selected position Relative position of the column in the row being defined.The first column in a statement has position 1. column Value of the column being defined. The type of this value determines the type for the column being defined.