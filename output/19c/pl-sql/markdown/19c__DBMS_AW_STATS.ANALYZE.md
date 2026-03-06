---
id: 19c__DBMS_AW_STATS.ANALYZE
name: DBMS_AW_STATS.ANALYZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AW_STATS
tags: [dbms_aw_stats]
source_file: DBMS_AW_STATS.html
---

# DBMS_AW_STATS.ANALYZE

This procedure generates optimizer statistics on a cube or a cube dimension.

## Syntax

```sql
DBMS_AW_STATS.ANALYZE
     (inname       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| inname | VARCHAR2) | IN | The qualified name of a cube or a dimension. For a cube, the format of a qualified name is owner.cube_name . For a dimension, the format is owner.dimension_name . |

## Usage Notes

These statistics are used to generate some execution plans, as described in " Using DBMS_AW_STATS " . For a cube, the statistics are for all of the measures and calculated measures associated with the cube. These statistics include: The average length of data values The length of the largest data value The minimum value The number of distinct values The number of null values For a dimension, the statistics are for the dimension and its attributes, levels, and hierarchies. These statistics include: The average length of a value The length of the largest value The minimum value The maximum value Syntax DBMS_AW_STATS.ANALYZE (inname IN VARCHAR2); Parameters Table 33-2 ANALYZE Procedure Parameters Parameter Description inname The qualified name of a cube or a dimension. For a cube, the format of a qualified name is owner.cube_name . For a dimension, the format is owner.dimension_name . Usage Notes Always analyze the dimensions first, then the cube. After analyzing a dimension, analyze all cubes that use that dimension. Example This sample script generates optimizer statistics on UNITS_CUBE and its dimensions. BEGIN DBMS_AW_STATS.ANALYZE('time'); DBMS_AW_STATS.ANALYZE('customer'); DBMS_AW_STATS.ANALYZE('product'); DBMS_AW_STATS.ANALYZE('channel'); DBMS_AW_STATS.ANALYZE('units_cube'); END; / The following statements create and display an execution plan for a SELECT statement that joins columns from UNITS_CUBE_VIEW , CUSTOMER_PRIMARY_VIEW , and the ACCOUNTS table: EXPLAIN PLAN FOR SELECT cu.long_description customer, a.city city, a.zip_pc zip, cu.level_name "LEVEL", round(f.sales) sales /* From dimension views and cube view */ FROM time_calendar_view t, product_primary_view p, customer_view cu, channel_view ch, units_cube_view f, account a /* Create level filters instead of GROUP BY */ WHERE t.long_description = '2004' AND p.level_name ='TOTAL' AND cu.customer_account_id like 'COMP%' AND ch.level_name = 'TOTAL' /* Join dimension views to cube view */ AND t.dim_key = f.TIME AND p.dim_key = f.product AND cu.dim_key = f.customer AND ch.dim_key = f.channel AND a.account_id = cu.customer_account_id ORDER BY zip; SQL> SELECT plan_table_output FROM TABLE(dbms_xplan.display()); PLAN_TABLE_OUTPUT ------------------------------------------------------------------------------------------------- Plan hash value: 3890178023 ----------------------------------------------------------------------------------------------- | Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time | ----------------------------------------------------------------------------------------------- | 0 | SELECT STATEMENT | | 1 | 89 | 6 (34)| 00:00:01 | | 1 | SORT ORDER BY | | 1 | 89 | 6 (34)| 00:00:01 | |* 2 | HASH JOIN | | 1 | 89 | 5 (20)| 00:00:01 | | 3 | JOINED CUBE SCAN PARTIAL OUTER| | | | | | | 4 | CUBE ACCESS | UNITS_CUBE | | | | | | 5 | CUBE ACCESS | CHANNEL | | | | | | 6 | CUBE ACCESS | CUSTOMER | | | | | | 7 | CUBE ACCESS | PRODUCT | | | | | |* 8 | CUBE ACCESS | TIME | 1 | 55 | 2 (0)| 00:00:01 | |* 9 | TABLE ACCESS FULL | ACCOUNT | 3 | 102 | 2 (0)| 00:00:01 | ----------------------------------------------------------------------------------------------- Predicate Information (identified by operation id): --------------------------------------------------- 2 - access("A"."ACCOUNT_ID"=SYS_OP_ATG(VALUE(KOKBF$),39,40,2)) 8 - filter(SYS_OP_ATG(VALUE(KOKBF$),16,17,2)='2004' AND SYS_OP_ATG(VALUE(KOKBF$),39,40,2) LIKE 'COMP%' AND SYS_OP_ATG(VALUE(KOKBF$),47,48,2)='TOTAL' AND SYS_OP_ATG(VALUE(KOKBF$),25,26,2)='TOTAL') 9 - filter("A"."ACCOUNT_ID" LIKE 'COMP%') Note ----- - dynamic statistics used for this statement 30 rows selected.