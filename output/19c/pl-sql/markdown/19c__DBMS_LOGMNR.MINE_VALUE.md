---
id: 19c__DBMS_LOGMNR.MINE_VALUE
name: DBMS_LOGMNR.MINE_VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR
tags: [dbms_logmnr]
source_file: DBMS_LOGMNR.html
---

# DBMS_LOGMNR.MINE_VALUE

This function facilitates queries based on a column's data value.

## Syntax

```sql
DBMS_LOGMNR.MINE_VALUE (
     sql_redo_undo      IN  RAW,
     column_name        IN  VARCHAR2 default '') RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_redo_undo | RAW | IN | Specifies either the REDO_VALUE or the UNDO_VALUE column in the V$LOGMNR_CONTENTS view from which to extract data values. See the Usage Notes for more information. |
| column_name | VARCHAR2 | IN | Specifies the fully qualified name ( schema.table.column ) of the column for which this function will return information. In a CDB, the column name is specified as follows: container_name:schema.table.column |

**Returns:** `VARCHAR2`

## Usage Notes

This function takes two arguments. The first one specifies whether to mine the redo ( REDO_VALUE ) or undo ( UNDO_VALUE ) portion of the data. The second argument is a string that specifies the fully qualified name of the column to be mined. The MINE_VALUE function always returns a string that can be converted back to the original datatype. Syntax DBMS_LOGMNR.MINE_VALUE ( sql_redo_undo IN RAW, column_name IN VARCHAR2 default '') RETURN VARCHAR2; Parameters Table 101-10 MINE_VALUE Function Parameters Parameter Description sql_redo_undo Specifies either the REDO_VALUE or the UNDO_VALUE column in the V$LOGMNR_CONTENTS view from which to extract data values. See the Usage Notes for more information. column_name Specifies the fully qualified name ( schema.table.column ) of the column for which this function will return information. In a CDB, the column name is specified as follows: container_name:schema.table.column Return Values Table 101-11 Return Values for MINE_VALUE Function Return Description NULL The column is not contained within the self-describing record, or the column value is NULL . To distinguish between the two different null possibilities, use the DBMS_LOGMNR.COLUMN_PRESENT function. NON-NULL The column is contained within the self-describing record; the value is returned in string format. Exceptions Table 101-12 MINE_VALUE Function Exceptions Exception Description ORA-01323 Invalid state. Currently, a LogMiner dictionary is not associated with the LogMiner session. You must specify a LogMiner dictionary for the LogMiner session. ORA-00904 Invalid identifier. The value specified for the column_name parameter was not a fully qualified column name.