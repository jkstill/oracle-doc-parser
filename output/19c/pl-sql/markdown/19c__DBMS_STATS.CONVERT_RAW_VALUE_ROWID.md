---
id: 19c__DBMS_STATS.CONVERT_RAW_VALUE_ROWID
name: DBMS_STATS.CONVERT_RAW_VALUE_ROWID
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CONVERT_RAW_VALUE_ROWID

This procedure converts the internal representation of a a minimum value, maximum value, or histogram end point actual value.

## Syntax

```sql
DBMS_STATS.CONVERT_RAW_VALUE_ROWID (
   rawval     RAW, 
   resval OUT ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rawval | RAW | IN | The raw representation of a column minimum or maximum datatype-specific output parameters |
| resval | ROWID) | OUT | The converted, type-specific value |

## Usage Notes

The minval , maxval and eavals fields of the StatRec structure as filled in by GET_COLUMN_STATS or PREPARE_COLUMN_VALUES are appropriate values for input. Syntax DBMS_STATS.CONVERT_RAW_VALUE_ROWID ( rawval RAW, resval OUT ROWID); Pragmas pragma restrict_references(convert_raw_value_rowid, WNDS, RNDS, WNPS, RNPS); Parameters Table 171-12 CONVERT_RAW_VALUE_ROWID Procedure Parameters Parameter Description rawval The raw representation of a column minimum or maximum datatype-specific output parameters resval The converted, type-specific value Usage Notes No special privilege or role is needed to invoke this procedure.