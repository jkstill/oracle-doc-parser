---
id: 19c__DBMS_STATS
name: DBMS_STATS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS

The DBMS_STATS package defines a RECORD type.

## Syntax

```sql
TYPE STATREC IS RECORD (
  epc    NUMBER,
  minval RAW(2000),
  maxval RAW(2000),
  bkvals NUMARRAY,
  novals NUMARRAY,
  chvals CHARARRAY,
  eavals RAWARRAY,
  rpcnts NUMARRAY,
  eavs   NUMBER);
```

## Usage Notes

RECORD Types STAT_REC Record Type Syntax TYPE STATREC IS RECORD ( epc NUMBER, minval RAW(2000), maxval RAW(2000), bkvals NUMARRAY, novals NUMARRAY, chvals CHARARRAY, eavals RAWARRAY, rpcnts NUMARRAY, eavs NUMBER); Fields of the Record type COMPARISON_TYPE (STAT_REC Attributes) Table 171-2 STAT_REC Attributes Field Description epc Number of buckets in histogram minval Minimum value maxval Maximum value bkvals Array of bucket numbers novals Array of normalized end point values chvals Array of dumped end point values eavals Array of end point actual values rpcnts Array of end point value frequencies eavs A number indicating whether actual end point values are needed in the histogram. If using the PREPARE_COLUMN_VALUES Procedures , this field will be automatically filled.