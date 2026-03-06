---
id: 19c__DBMS_LOGMNR.COLUMN_PRESENT
name: DBMS_LOGMNR.COLUMN_PRESENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGMNR
tags: [dbms_logmnr]
source_file: DBMS_LOGMNR.html
---

# DBMS_LOGMNR.COLUMN_PRESENT

This function is designed to be used in conjunction with the MINE_VALUE function.

## Syntax

```sql
DBMS_LOGMNR.COLUMN_PRESENT (
     sql_redo_undo      IN  RAW,
     column_name        IN  VARCHAR2 default '') RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_redo_undo | RAW | IN | Specifies either the REDO_VALUE or the UNDO_VALUE column in the V$LOGMNR_CONTENTS view from which to extract data values. See the Usage Notes for more information. |
| column_name | VARCHAR2 | IN | Specifies the fully qualified name ( schema.table.column ) of the column for which this function will return information. In a CDB, the column name is specified as follows: container_name:schema.table.column |

**Returns:** `NUMBER`

## Usage Notes

If the MINE_VALUE function returns a NULL value, it can mean either: The specified column is not present in the redo or undo portion of the data. The specified column is present and has a NULL value. To distinguish between these two cases, use the COLUMN_PRESENT function, which returns a 1 if the column is present in the redo or undo portion of the data. Otherwise, it returns a 0 . Syntax DBMS_LOGMNR.COLUMN_PRESENT ( sql_redo_undo IN RAW, column_name IN VARCHAR2 default '') RETURN NUMBER; Parameters Table 101-6 COLUMN_PRESENT Function Parameters Parameter Description sql_redo_undo Specifies either the REDO_VALUE or the UNDO_VALUE column in the V$LOGMNR_CONTENTS view from which to extract data values. See the Usage Notes for more information. column_name Specifies the fully qualified name ( schema.table.column ) of the column for which this function will return information. In a CDB, the column name is specified as follows: container_name:schema.table.column Return Values Table 101-7 describes the return values for the COLUMN_PRESENT function. The COLUMN_PRESENT function returns 1 if the self-describing record (the first parameter) contains the column specified in the second parameter. This can be used to determine the meaning of NULL values returned by the DBMS_LOGMNR.MINE_VALUE function. Table 101-7 Return Values for COLUMN_PRESENT Function Return Description 0 Specified column is not present in this row of V$LOGMNR_CONTENTS . 1 Column is present in this row of V$LOGMNR_CONTENTS . Exceptions Table 101-8 COLUMN_PRESENT Function Exceptions Exception Description ORA-01323 Currently, a LogMiner dictionary is not associated with the LogMiner session. You must specify a LogMiner dictionary for the LogMiner session. ORA-00904 Value specified for the column_name parameter is not a fully qualified column name.