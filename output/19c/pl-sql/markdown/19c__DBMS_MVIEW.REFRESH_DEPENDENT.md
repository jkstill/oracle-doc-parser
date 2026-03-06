---
id: 19c__DBMS_MVIEW.REFRESH_DEPENDENT
name: DBMS_MVIEW.REFRESH_DEPENDENT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.REFRESH_DEPENDENT

This procedure refreshes all materialized views that have certain properties.

## Syntax

```sql
DBMS_MVIEW.REFRESH_DEPENDENT (
   number_of_failures     OUT    BINARY_INTEGER,
   { list                 IN     VARCHAR2,
   | tab                  IN     DBMS_UTILITY.UNCL_ARRAY,}
   method                 IN     VARCHAR2    := NULL,
   rollback_seg           IN     VARCHAR2    := NULL,
   refresh_after_errors   IN     BOOLEAN     := false,
   atomic_refresh         IN     BOOLEAN     := true,
   nested                 IN     BOOLEAN     := false,
   out_of_place           IN     BOOLEAN     := false);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| number_of_failures | BINARY_INTEGER | OUT | Returns the number of failures that occurred during processing |
| list | tab |  |  | Comma-delimited list of master tables or master materialized views on which materialized views can depend. (Synonyms are not supported.) These tables and the materialized views that depend on them can be located in different schemas. However, all of the tables and materialized views must be in your local database. Alternatively, you may pass in a PL/SQL index-by table of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a table. |
| method | VARCHAR2 | IN | A string of refresh methods indicating how to refresh the dependent materialized views. All of the materialized views that depend on a particular table are refreshed according to the refresh method associated with that table. F or f indicates fast refresh, ? indicates force refresh, C or c indicates complete refresh, and A or a indicates always refresh. A and C are equivalent. P or p refreshes by recomputing the rows in the materialized view affected by changed partitions in the detail tables. If a table does not have a corresponding refresh method (that is, if more tables are specified than refresh methods), then any materialized view that depends on that table is refreshed according to its default refresh method. For example, the following EXECUTE statement within SQL*Plus: DBMS_MVIEW.REFRESH_DEPENDENT ('employees,deptartments,hr.regions','cf'); performs a complete refresh of the materialized views that depend on the employees table, a fast refresh of the materialized views that depend on the departments table, and a default refresh of the materialized views that depend on the hr.regions table. |
| rollback_seg | VARCHAR2 | IN | Name of the materialized view site rollback segment to use while refreshing materialized views |
| refresh_after_errors | BOOLEAN | IN | If this parameter is true , an updatable materialized view continues to refresh even if there are outstanding conflicts logged in the DEFERROR view for the materialized view's master table or master materialized view. If this parameter is true and atomic_refresh is false , this procedure continues to refresh other materialized views if it fails while refreshing a materialized view. |
| atomic_refresh | BOOLEAN | IN | If this parameter is set to true , then the refreshed materialized views are refreshed in a single transaction. All of the refreshed materialized views are updated to a single point in time. If the refresh fails for any of the materialized views, none of the materialized views are updated. If this parameter is set to false , then each of the materialized views is refreshed non-atomically in separate transactions. |
| nested | BOOLEAN | IN | If true , then perform nested refresh operations for the specified set of tables. Nested refresh operations refresh all the depending materialized views of the specified set of tables based on a dependency order to ensure the nested materialized views are truly fresh with respect to the underlying base tables. |
| out_of_place | BOOLEAN | IN | If true , then it performs an out-of-place refresh. The default is false . This parameter uses the four methods of refresh ( F , P , C , ? ). So, for example, if you specify F and out_of_place = true , then an out-of-place fast refresh will be attempted. Similarly, if you specify P and out_of_place = true , then out-of-place PCT refresh will be attempted. |

## Usage Notes

Materialized views with the following properties are refreshed: The materialized view depends on a master table or master materialized view in the list of specified masters. The materialized view has not been refreshed since the most recent change to a master table or master materialized view on which it depends. The materialized view and all of the master tables or master materialized views on which it depends are local. The materialized view is in the view DBA_MVIEWS . This procedure is intended for use with data warehouses. Syntax DBMS_MVIEW.REFRESH_DEPENDENT ( number_of_failures OUT BINARY_INTEGER, { list IN VARCHAR2, | tab IN DBMS_UTILITY.UNCL_ARRAY,} method IN VARCHAR2 := NULL, rollback_seg IN VARCHAR2 := NULL, refresh_after_errors IN BOOLEAN := false, atomic_refresh IN BOOLEAN := true, nested IN BOOLEAN := false, out_of_place IN BOOLEAN := false); Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Parameters Table 113-12 REFRESH_DEPENDENT Procedure Parameters Parameter Description number_of_failures Returns the number of failures that occurred during processing list | tab Comma-delimited list of master tables or master materialized views on which materialized views can depend. (Synonyms are not supported.) These tables and the materialized views that depend on them can be located in different schemas. However, all of the tables and materialized views must be in your local database. Alternatively, you may pass in a PL/SQL index-by table of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a table. method A string of refresh methods indicating how to refresh the dependent materialized views. All of the materialized views that depend on a particular table are refreshed according to the refresh method associated with that table. F or f indicates fast refresh, ? indicates force refresh, C or c indicates complete refresh, and A or a indicates always refresh. A and C are equivalent. P or p refreshes by recomputing the rows in the materialized view affected by changed partitions in the detail tables. If a table does not have a corresponding refresh method (that is, if more tables are specified than refresh methods), then any materialized view that depends on that table is refreshed according to its default refresh method. For example, the following EXECUTE statement within SQL*Plus: DBMS_MVIEW.REFRESH_DEPENDENT ('employees,deptartments,hr.regions','cf'); performs a complete refresh of the materialized views that depend on the employees table, a fast refresh of the materialized views that depend on the departments table, and a default refresh of the materialized views that depend on the hr.regions table. rollback_seg Name of the materialized view site rollback segment to use while refreshing materialized views refresh_after_errors If this parameter is true , an updatable materialized view continues to refresh even if there are outstanding conflicts logged in the DEFERROR view for the materialized view's master table or master materialized view. If this parameter is true and atomic_refresh is false , this procedure continues to refresh other materialized views if it fails while refreshing a materialized view. atomic_refresh If this parameter is set to true , then the refreshed materialized views are refreshed in a single transaction. All of the refreshed materialized views are updated to a single point in time. If the refresh fails for any of the materialized views, none of the materialized views are updated. If this parameter is set to false , then each of the materialized views is refreshed non-atomically in separate transactions. nested If true , then perform nested refresh operations for the specified set of tables. Nested refresh operations refresh all the depending materialized views of the specified set of tables based on a dependency order to ensure the nested materialized views are truly fresh with respect to the underlying base tables. out_of_place If true , then it performs an out-of-place refresh. The default is false . This parameter uses the four methods of refresh ( F , P , C , ? ). So, for example, if you specify F and out_of_place = true , then an out-of-place fast refresh will be attempted. Similarly, if you specify P and out_of_place = true , then out-of-place PCT refresh will be attempted.