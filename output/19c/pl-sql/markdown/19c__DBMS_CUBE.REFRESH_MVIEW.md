---
id: 19c__DBMS_CUBE.REFRESH_MVIEW
name: DBMS_CUBE.REFRESH_MVIEW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.REFRESH_MVIEW

This procedure refreshes the data in a cube materialized view.

## Syntax

```sql
DBMS_CUBE.REFRESH_MVIEW (
          mvowner              IN  VARCHAR2,
          mvname               IN  VARCHAR2,
          method               IN  VARCHAR2       DEFAULT NULL,
          refresh_after_errors IN  BOOLEAN        DEFAULT FALSE,
          parallelism          IN  BINARY_INTEGER DEFAULT 0,
          atomic_refresh       IN  BOOLEAN        DEFAULT FALSE,
          scheduler_job        IN  VARCHAR2       DEFAULT NULL,
          sam_parameters       IN  CLOB           DEFAULT NULL,
          nested               IN  BOOLEAN        DEFAULT FALSE );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mvowner | VARCHAR2 | IN | Owner of the cube materialized view. |
| mvname | VARCHAR2 | IN | Name of the cube materialized view. |
| method | VARCHAR2 | IN | A full or a fast (partial) refresh. In a fast refresh, only changed rows are inserted in the cube and the affected areas of the cube are re-aggregated. You can specify a method for each cube in sequential order, or a single method to apply to all cubes. If you list more cubes than methods, then the last method applies to the additional cubes. C : Complete refresh clears all dimension values before loading. (Default) F : Fast refresh of a cube materialized view, which performs an incremental refresh and re-aggregation of only changed rows in the source table. ? : Fast refresh if possible, and otherwise a complete refresh. P : Recomputes rows in a cube materialized view that are affected by changed partitions in the detail tables. S : Fast solve of a compressed cube. A fast solve reloads all the detail data and re-aggregates only the changed values. See the " Usage Notes " for the BUILD procedure for additional details. |
| refresh_after_errors | BOOLEAN | IN | TRUE to roll back just the cube or dimension with errors, and then continue building the other objects. FALSE to roll back all objects in the build. |
| parallelism | BINARY_INTEGER | IN | Number of parallel processes to allocate to this job. See the " Usage Notes " for the BUILD procedure for additional details. |
| atomic_refresh | BOOLEAN | IN | TRUE prevents users from accessing intermediate results during a build. It freezes the current state of an analytic workspace at the beginning of the build to provide current sessions with consistent data. This option thaws the analytic workspace at the end of the build to give new sessions access to the refreshed data. If an error occurs during the build, then all objects are rolled back to the frozen state. FALSE enables users to access intermediate results during an build. |
| scheduler_job | VARCHAR2 | IN | Any text identifier for the job, which will appear in the log table. The string does not need to be unique. |
| sam_parameters | CLOB | IN | None. |
| nested | BOOLEAN | IN | TRUE performs nested refresh operations for the specified set of cube materialized views. Nested refresh operations refresh all the depending materialized views and the specified set of materialized views based on a dependency order to ensure the nested materialized views are truly fresh with respect to the underlying base tables. All objects must reside in a single analytic workspace. |

## Usage Notes

Syntax DBMS_CUBE.REFRESH_MVIEW ( mvowner IN VARCHAR2, mvname IN VARCHAR2, method IN VARCHAR2 DEFAULT NULL, refresh_after_errors IN BOOLEAN DEFAULT FALSE, parallelism IN BINARY_INTEGER DEFAULT 0, atomic_refresh IN BOOLEAN DEFAULT FALSE, scheduler_job IN VARCHAR2 DEFAULT NULL, sam_parameters IN CLOB DEFAULT NULL, nested IN BOOLEAN DEFAULT FALSE ); Parameters Table 44-13 REFRESH_MVIEW Procedure Parameters Parameter Description mvowner Owner of the cube materialized view. mvname Name of the cube materialized view. method A full or a fast (partial) refresh. In a fast refresh, only changed rows are inserted in the cube and the affected areas of the cube are re-aggregated. You can specify a method for each cube in sequential order, or a single method to apply to all cubes. If you list more cubes than methods, then the last method applies to the additional cubes. C : Complete refresh clears all dimension values before loading. (Default) F : Fast refresh of a cube materialized view, which performs an incremental refresh and re-aggregation of only changed rows in the source table. ? : Fast refresh if possible, and otherwise a complete refresh. P : Recomputes rows in a cube materialized view that are affected by changed partitions in the detail tables. S : Fast solve of a compressed cube. A fast solve reloads all the detail data and re-aggregates only the changed values. See the " Usage Notes " for the BUILD procedure for additional details. refresh_after_errors TRUE to roll back just the cube or dimension with errors, and then continue building the other objects. FALSE to roll back all objects in the build. parallelism Number of parallel processes to allocate to this job. See the " Usage Notes " for the BUILD procedure for additional details. atomic_refresh TRUE prevents users from accessing intermediate results during a build. It freezes the current state of an analytic workspace at the beginning of the build to provide current sessions with consistent data. This option thaws the analytic workspace at the end of the build to give new sessions access to the refreshed data. If an error occurs during the build, then all objects are rolled back to the frozen state. FALSE enables users to access intermediate results during an build. scheduler_job Any text identifier for the job, which will appear in the log table. The string does not need to be unique. sam_parameters None. nested TRUE performs nested refresh operations for the specified set of cube materialized views. Nested refresh operations refresh all the depending materialized views and the specified set of materialized views based on a dependency order to ensure the nested materialized views are truly fresh with respect to the underlying base tables. All objects must reside in a single analytic workspace. Usage Notes REFRESH_MVIEW changes mvname to the name of the cube, then passes the cube name and all parameters to the BUILD procedure. Thus, you can use the BUILD procedure to refresh a cube materialized view. See the " BUILD Procedure " for additional information about the parameters. Examples The following example uses the default settings to refresh a cube materialized view named CB$FWEEK_PSCAT_SALES . SET serverout ON format wrapped EXECUTE dbms_cube.refresh_mview('SH', 'CB$FWEEK_PSCAT_SALES'); The next example changes the refresh method to use fast refresh if possible, continue refreshing after an error, and use two parallel processes. EXECUTE dbms_cube.refresh_mview('SH', 'CB$FWEEK_PSCAT_SALES', '?', TRUE, 2); After successfully refreshing the cube materialized view, REFRESH_MVIEW returns a message like the following: Completed refresh of cube mview "SH"."CB$FWEEK_PSCAT_SALES" at 20130212 15:04:46.370.