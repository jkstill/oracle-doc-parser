---
id: 19c__DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR
name: DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR

This procedure converts the internal representation of a a minimum value, maximum value, or histogram end point actual value.

## Syntax

```sql
DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR (
   rawval     RAW, 
   resval OUT NVARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rawval | RAW | IN | The raw representation of a column minimum or maximum datatype-specific output parameters |
| resval | NVARCHAR2) | OUT | The converted, type-specific value |

## Usage Notes

The minval , maxval and eavals fields of the StatRec structure as filled in by GET_COLUMN_STATS or PREPARE_COLUMN_VALUES are appropriate values for input. Syntax DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR ( rawval RAW, resval OUT NVARCHAR2); Parameters Table 171-11 CONVERT_RAW_VALUE_NVARCHAR Procedure Parameters Parameter Description rawval The raw representation of a column minimum or maximum datatype-specific output parameters resval The converted, type-specific value Usage Notes No special privilege or role is needed to invoke this procedure.