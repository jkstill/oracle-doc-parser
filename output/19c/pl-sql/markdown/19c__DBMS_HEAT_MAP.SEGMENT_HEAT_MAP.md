---
id: 19c__DBMS_HEAT_MAP.SEGMENT_HEAT_MAP
name: DBMS_HEAT_MAP.SEGMENT_HEAT_MAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HEAT_MAP
tags: [dbms_heat_map]
source_file: DBMS_HEAT_MAP.html
---

# DBMS_HEAT_MAP.SEGMENT_HEAT_MAP

This procedure returns the heatmap attributes for the given segment.

## Syntax

```sql
DBMS_HEAT_MAP.SEGMENT_HEAT_MAP (
   tablespace_id          IN  NUMBER,
   header_file            IN  NUMBER,
   header_block           IN  NUMBER,
   segment_objd           IN  NUMBER,
   min_writetime          OUT DATE,
   max_writetime          OUT DATE,
   avg_writetime          OUT DATE,
   min_readtime           OUT DATE,
   max_readtime           OUT DATE,
   avg_readtime           OUT DATE,
   min_lookuptime         OUT DATE,
   max_lookuptime         OUT DATE,
   avg_lookuptime         OUT DATE,
   min_ftstime            OUT DATE,
   max_ftstime            OUT DATE,
   avg_ftstime            OUT DATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_id | NUMBER | IN | Tablespace containing the segment |
| header_file | NUMBER | IN | Segment header relative file number |
| header_block | NUMBER | IN | Segment header block number |
| segment_objd | NUMBER | IN | DATAOBJ of the segment |

## Usage Notes

Syntax DBMS_HEAT_MAP.SEGMENT_HEAT_MAP ( tablespace_id IN NUMBER, header_file IN NUMBER, header_block IN NUMBER, segment_objd IN NUMBER, min_writetime OUT DATE, max_writetime OUT DATE, avg_writetime OUT DATE, min_readtime OUT DATE, max_readtime OUT DATE, avg_readtime OUT DATE, min_lookuptime OUT DATE, max_lookuptime OUT DATE, avg_lookuptime OUT DATE, min_ftstime OUT DATE, max_ftstime OUT DATE, avg_ftstime OUT DATE); Parameters Table 80-8 SEGMENT_HEAT_MAP Procedure Parameters Parameter Description tablespace_id Tablespace containing the segment header_file Segment header relative file number header_block Segment header block number segment_objd DATAOBJ of the segment Return Values Table 80-9 SEGMENT_HEAT_MAP Procedure Return Values (Output Parameters ) Parameter Description min_writetime Oldest write time for the segment max_writetime Latest write time for the segment avg_writetime Average write time for the segment min_readtime Oldest read time for the segment max_readtime Latest read time for the segment avg_writetime Average write time for the segment min_lookuptime Oldest index lookup time for the segment max_lookuptime Latest index lookup time for the segment avg_lookuptime Average index lookup time for the segment min_ftstime Oldest full table scan time for the segment max_ftstime Latest full table scan time for the segment avg_ftstime Average full table scan time for the segment