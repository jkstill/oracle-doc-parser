---
id: 19c__DBMS_MVIEW.REFRESH_ALL_MVIEWS
name: DBMS_MVIEW.REFRESH_ALL_MVIEWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MVIEW
tags: [dbms_mview]
source_file: DBMS_MVIEW.html
---

# DBMS_MVIEW.REFRESH_ALL_MVIEWS

This procedure refreshes all materialized views that have certain properties

## Syntax

```sql
DBMS_MVIEW.REFRESH_ALL_MVIEWS (
   number_of_failures     OUT   BINARY_INTEGER,
   method                 IN    VARCHAR2         := NULL,
   rollback_seg           IN    VARCHAR2         := NULL,
   refresh_after_errors   IN    BOOLEAN          := false,
   atomic_refresh         IN    BOOLEAN          := true,
   out_of_place           IN    BOOLEAN          := false);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| number_of_failures | BINARY_INTEGER | OUT | Returns the number of failures that occurred during processing |
| method | VARCHAR2 | IN | A single refresh method indicating the type of refresh to perform for each materialized view that is refreshed. F or f indicates fast refresh, ? indicates force refresh, C or c indicates complete refresh, and A or a indicates always refresh. A and C are equivalent. If no method is specified, a materialized view is refreshed according to its default refresh method. P or p refreshes by recomputing the rows in the materialized view affected by changed partitions in the detail tables. |
| rollback_seg | VARCHAR2 | IN | Name of the materialized view site rollback segment to use while refreshing materialized views |
| refresh_after_errors | BOOLEAN | IN | If this parameter is true , an updatable materialized view continues to refresh even if there are outstanding conflicts logged in the DEFERROR view for the materialized view's master table or master materialized view. If this parameter is true and atomic_refresh is false , this procedure continues to refresh other materialized views if it fails while refreshing a materialized view. |
| atomic_refresh | BOOLEAN | IN | If this parameter is set to true , then the refreshed materialized views are refreshed in a single transaction. All of the refreshed materialized views are updated to a single point in time. If the refresh fails for any of the materialized views, none of the materialized views are updated. If this parameter is set to false , then each of the materialized views is refreshed non-atomically in separate transactions. |
| out_of_place | BOOLEAN | IN | If true , then it performs an out-of-place refresh. The default is false . This parameter uses the four methods of refresh ( F , P , C , ? ). So, for example, if you specify F and out_of_place = true , then an out-of-place fast refresh will be attempted. Similarly, if you specify P and out_of_place = true , then out-of-place PCT refresh will be attempted. |

## Usage Notes

All materialized views with the following properties are refreshed: The materialized view has not been refreshed since the most recent change to a master table or master materialized view on which it depends. The materialized view and all of the master tables or master materialized views on which it depends are local. The materialized view is in the view DBA_MVIEWS . This procedure is intended for use with data warehouses. Syntax DBMS_MVIEW.REFRESH_ALL_MVIEWS ( number_of_failures OUT BINARY_INTEGER, method IN VARCHAR2 := NULL, rollback_seg IN VARCHAR2 := NULL, refresh_after_errors IN BOOLEAN := false, atomic_refresh IN BOOLEAN := true, out_of_place IN BOOLEAN := false); Parameters Table 113-11 REFRESH_ALL_MVIEWS Procedure Parameters Parameter Description number_of_failures Returns the number of failures that occurred during processing method A single refresh method indicating the type of refresh to perform for each materialized view that is refreshed. F or f indicates fast refresh, ? indicates force refresh, C or c indicates complete refresh, and A or a indicates always refresh. A and C are equivalent. If no method is specified, a materialized view is refreshed according to its default refresh method. P or p refreshes by recomputing the rows in the materialized view affected by changed partitions in the detail tables. rollback_seg Name of the materialized view site rollback segment to use while refreshing materialized views refresh_after_errors If this parameter is true , an updatable materialized view continues to refresh even if there are outstanding conflicts logged in the DEFERROR view for the materialized view's master table or master materialized view. If this parameter is true and atomic_refresh is false , this procedure continues to refresh other materialized views if it fails while refreshing a materialized view. atomic_refresh If this parameter is set to true , then the refreshed materialized views are refreshed in a single transaction. All of the refreshed materialized views are updated to a single point in time. If the refresh fails for any of the materialized views, none of the materialized views are updated. If this parameter is set to false , then each of the materialized views is refreshed non-atomically in separate transactions. out_of_place If true , then it performs an out-of-place refresh. The default is false . This parameter uses the four methods of refresh ( F , P , C , ? ). So, for example, if you specify F and out_of_place = true , then an out-of-place fast refresh will be attempted. Similarly, if you specify P and out_of_place = true , then out-of-place PCT refresh will be attempted.