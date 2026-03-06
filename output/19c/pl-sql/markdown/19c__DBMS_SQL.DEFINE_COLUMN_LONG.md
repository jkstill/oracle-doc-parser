---
id: 19c__DBMS_SQL.DEFINE_COLUMN_LONG
name: DBMS_SQL.DEFINE_COLUMN_LONG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_COLUMN_LONG

This procedure defines a LONG column for a SELECT cursor. The column being defined is identified by its relative position in the SELECT list of the statement for the given cursor. The type of the COLUMN value determines the type of the column being defined.

## Syntax

```sql
DBMS_SQL.DEFINE_COLUMN_LONG (
   c              IN INTEGER,
   position       IN INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor for the row being defined to be selected. |
| position | INTEGER) | IN | Relative position of the column in the row being defined. The first column in a statement has position 1. |

## Usage Notes

See also the DEFINE_COLUMN Procedures , DEFINE_COLUMN_CHAR Procedure , DEFINE_COLUMN_RAW Procedure and DEFINE_COLUMN_ROWID Procedure . Syntax DBMS_SQL.DEFINE_COLUMN_LONG ( c IN INTEGER, position IN INTEGER); Parameters Table 162-17 DEFINE_COLUMN_LONG Procedure Parameters Parameter Description c ID number of the cursor for the row being defined to be selected. position Relative position of the column in the row being defined. The first column in a statement has position 1.