---
id: 19c__DBMS_SQL.COLUMN_VALUE_LONG
name: DBMS_SQL.COLUMN_VALUE_LONG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.COLUMN_VALUE_LONG

This procedure gets part of the value of a long column.

## Syntax

```sql
DBMS_SQL.COLUMN_VALUE_LONG (
   c            IN  INTEGER, 
   position     IN  INTEGER, 
   length       IN  INTEGER, 
   offset       IN  INTEGER,
   value        OUT VARCHAR2,
   value_length OUT INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | Cursor ID number of the cursor from which to get the value. |
| position | INTEGER | IN | Position of the column of which to get the value. |
| length | INTEGER | IN | Number of bytes of the long value to fetch. |
| offset | INTEGER | IN | Offset into the long field for start of fetch. |
| value | VARCHAR2 | OUT | Value of the column as a VARCHAR2 . |
| value_length | INTEGER) | OUT | Number of bytes actually returned in value. |

## Usage Notes

Syntax DBMS_SQL.COLUMN_VALUE_LONG ( c IN INTEGER, position IN INTEGER, length IN INTEGER, offset IN INTEGER, value OUT VARCHAR2, value_length OUT INTEGER); Pragmas pragma restrict_references(column_value_long,RNDS,WNDS); Parameters Table 162-13 COLUMN_VALUE_LONG Procedure Parameters Parameter Description c Cursor ID number of the cursor from which to get the value. position Position of the column of which to get the value. length Number of bytes of the long value to fetch. offset Offset into the long field for start of fetch. value Value of the column as a VARCHAR2 . value_length Number of bytes actually returned in value.