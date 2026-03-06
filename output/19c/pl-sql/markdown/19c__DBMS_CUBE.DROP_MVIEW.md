---
id: 19c__DBMS_CUBE.DROP_MVIEW
name: DBMS_CUBE.DROP_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.DROP_MVIEW

This procedure drops a cube materialized view and all associated objects from the database. These objects include the dimension materialized views, cubes, cube dimensions, levels, hierarchies, and the analytic workspace.

## Syntax

```sql
DBMS_CUBE.DROP_MVIEW (
          mvowner        IN  VARCHAR2,
          mvname         IN  VARCHAR2,
          sam_parameters IN  CLOB  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mvowner | VARCHAR2 | IN | Owner of the cube materialized view |
| mvname | VARCHAR2 | IN | Name of the cube materialized view |
| sam_parameters | CLOB | IN | EXPORTXML : Exports the XML that drops the dimensional objects to a file, which you specify as dir/filename . Both the directory and the file name are case sensitive. dir : Name of a database directory. filename : The name of the file, typically given an XML filename extension. |

## Usage Notes

Syntax DBMS_CUBE.DROP_MVIEW ( mvowner IN VARCHAR2, mvname IN VARCHAR2, sam_parameters IN CLOB DEFAULT NULL); Parameters Table 44-9 DROP_MVIEW Procedure Parameters Parameter Description mvowner Owner of the cube materialized view mvname Name of the cube materialized view sam_parameters EXPORTXML : Exports the XML that drops the dimensional objects to a file, which you specify as dir/filename . Both the directory and the file name are case sensitive. dir : Name of a database directory. filename : The name of the file, typically given an XML filename extension. Usage Notes Use this procedure to drop a cube materialized view that you created using the CREATE_MVIEW and DERIVE_FROM_MVIEW functions. If you make modifications to the cubes or dimensions, then DROP_MVIEW may not be able to drop the cube materialized view. Some of the CUBEMVOPTION parameters used by the CREATE_MVIEW and DERIVE_FROM_MVIEW functions do not create a materialized view. Use Analytic Workspace Manager to drop the analytic workspace, cubes, and cube dimensions. If you use the EXPORTXML parameter, then you can use the XML document to drop the cube materialized view, after you re-create it. Use the IMPORT_XML procedure. See " Using SQL Aggregation Management " . Examples The current schema has four materialized views. CB$CAL_MONTH_SALES is a cube materialized view for the SALES table. CB$TIMES_DIM_D1_CAL_ROLLUP is a cube dimension materialized view for the TIMES_DIM dimension on the TIMES dimension table. The others are relational materialized views. SELECT mview_name FROM user_mviews; MVIEW_NAME ------------------------------ CB$CAL_MONTH_SALES CB$TIMES_DIM_D1_CAL_ROLLUP CAL_MONTH_SALES_MV FWEEK_PSCAT_SALES_MV The following command drops both CB$CAL_MONTH_SALES and CB$TIMES_DIM_D1_CAL_ROLLUP . EXECUTE dbms_cube.drop_mview('SH', 'CB$CAL_MONTH_SALES'); Dropped cube organized materialized view "SH"."CAL_MONTH_SALES" including container analytic workspace "SH"."CAL_MONTH_SALES_AW" at 20130213 16:31:40.056. This query against the data dictionary confirms that the materialized views have been dropped. SELECT mview_name FROM user_mviews; MVIEW_NAME ------------------------------ CAL_MONTH_SALES_MV FWEEK_PSCAT_SALES_MV