---
id: 19c__DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP
name: DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HEAT_MAP
tags: [dbms_heat_map]
source_file: DBMS_HEAT_MAP.html
---

# DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP

This table function returns the minimum, maximum and average access times for all the segments in the tablespace.

## Syntax

```sql
DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP (
    tablespace_name      IN VARCHAR2)
  RETURN hm_tablespace_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2) | IN | Name of the tablespace |

**Returns:** `hm_tablespace_table`

## Usage Notes

Syntax DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP ( tablespace_name IN VARCHAR2) RETURN hm_tablespace_table PIPELINED; Parameters Table 80-10 TABLESPACE_HEAT_MAP Procedure Parameters Parameter Description tablespace_name Name of the tablespace Return Values Table 80-11 TABLESPACE_HEAT_MAP Procedure Return Values (Output Parameters ) Parameter Description segment_count Total number of segments in the tablespace allocated_bytes Space used by the segments in the tablespace min_writetime Oldest write time for the segment max_writetime Latest write time for the segment avg_writetime Average write time for the segment min_readtime Oldest read time for the segment max_readtime Latest read time for the segment avg_writetime Average write time for the segment min_lookuptime Oldest index lookup time for the segment max_lookuptime Latest index lookup time for the segment avg_lookuptime Average index lookup time for the segment min_ftstime Oldest full table scan time for the segment max_ftstime Latest full table scan time for the segment avg_ftstime Average full table scan time for the segment