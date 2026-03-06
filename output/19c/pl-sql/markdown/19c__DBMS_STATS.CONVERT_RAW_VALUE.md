---
id: 19c__DBMS_STATS.CONVERT_RAW_VALUE
name: DBMS_STATS.CONVERT_RAW_VALUE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CONVERT_RAW_VALUE

This procedure converts the internal representation of a minimum value, maximum value, or histogram endpoint actual value into a datatype-specific value.

## Syntax

```sql
DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT BINARY_FLOAT);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT BINARY_DOUBLE);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT DATE);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT NUMBER);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rawval | RAW | IN | Raw representation of a column minimum, maximum, histogram end point actual value |
| resval | BINARY_FLOAT) | OUT | Converted, type-specific value |

## Usage Notes

The minval , maxval , and eavals fields of the StatRec structure as filled in by GET_COLUMN_STATS or PREPARE_COLUMN_VALUES are appropriate values for input. Syntax DBMS_STATS.CONVERT_RAW_VALUE ( rawval RAW, resval OUT BINARY_FLOAT); DBMS_STATS.CONVERT_RAW_VALUE ( rawval RAW, resval OUT BINARY_DOUBLE); DBMS_STATS.CONVERT_RAW_VALUE ( rawval RAW, resval OUT DATE); DBMS_STATS.CONVERT_RAW_VALUE ( rawval RAW, resval OUT NUMBER); DBMS_STATS.CONVERT_RAW_VALUE ( rawval RAW, resval OUT VARCHAR2); Parameters Table 171-10 CONVERT_RAW_VALUE Procedure Parameters Parameter Description rawval Raw representation of a column minimum, maximum, histogram end point actual value resval Converted, type-specific value Usage Notes No special privilege or role is needed to invoke this procedure.