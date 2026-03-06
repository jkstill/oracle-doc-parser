---
id: 19c__DBMS_REFRESH.MAKE
name: DBMS_REFRESH.MAKE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.MAKE

This procedure specifies the members of a refresh group and the time interval used to determine when to refresh the members of this group.

## Syntax

```sql
DBMS_REFRESH.MAKE (
   name                  IN    VARCHAR2
   { list                IN    VARCHAR2,
   | tab                 IN    DBMS_UTILITY.UNCL_ARRAY,}
   next_date             IN    DATE,
   interval              IN    VARCHAR2,
   implicit_destroy      IN    BOOLEAN         := FALSE,
   lax                   IN    BOOLEAN         := FALSE,
   job                   IN    BINARY_INTEGER  := 0,
   rollback_seg          IN    VARCHAR2        := NULL,
   push_deferred_rpc     IN    BOOLEAN         := TRUE,
   refresh_after_errors  IN    BOOLEAN         := FALSE
   purge_option          IN    BINARY_INTEGER  := NULL,
   parallelism           IN    BINARY_INTEGER  := NULL,
   heap_size             IN    BINARY_INTEGER  := NULL
   job_name              IN    VARCHAR2        := NULL,
   auto_commit           IN    BOOLEAN         := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Unique name used to identify the refresh group, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. Refresh groups must follow the same naming conventions as tables. |
| list | VARCHAR2 | IN | Comma-delimited list of materialized views that you want to refresh. Synonyms are not supported. These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| tab | DBMS_UTILITY.UNCL_ARRAY | IN | Instead of a comma-delimited list, you can supply a PL/SQL associative array of names of materialized views that you want to refresh using the data type DBMS_UTILITY.UNCL_ARRAY . If the table contains the names of n materialized views, then the first materialized view should be in position 1 and the n + 1 position should be set to NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| next_date | DATE | IN | Next date that you want a refresh to occur. |
| interval | VARCHAR2 | IN | Function used to calculate the next time to refresh the materialized views in the group. This field is used with the next_date value. For example, if you specify NEXT_DAY(SYSDATE+1, "MONDAY") as your interval, and if your next_date evaluates to Monday, then Oracle refreshes the materialized views every Monday. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. |
| implicit_destroy | BOOLEAN | IN | Set this to TRUE to delete the refresh group automatically when it no longer contains any members. Oracle checks this flag only when you call the SUBTRACT procedure. That is, setting this flag still enables you to create an empty refresh group. |
| lax | BOOLEAN | IN | A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from an existing group to a new refresh group, then you must set this to TRUE to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to MAKE generates an error message. |
| job | BINARY_INTEGER | IN | Needed by the Import utility. Use the default value, 0. |
| rollback_seg | VARCHAR2 | IN | Name of the rollback segment to use while refreshing materialized views. The default, NULL , uses the default rollback segment. |
| push_deferred_rpc | BOOLEAN | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| refresh_after_errors | BOOLEAN | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| purge_option | BINARY_INTEGER | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| parallelism | BINARY_INTEGER | IN | 0 specifies serial propagation. n > 1 specifies parallel propagation with n parallel processes. 1 specifies parallel propagation using only one parallel process. |
| heap_size | BINARY_INTEGER | IN | Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance. Note: Do not set this parameter unless directed to do so by Oracle Support Services. |
| job_name | VARCHAR2 | IN | This parameter is needed by the import utility. User should use the default value, NULL . |
| auto_commit | BOOLEAN | IN | Supported values are NULL , TRUE , and FALSE . NULL —allows the user to continue using DBMS_JOB . TRUE —commit statement will be automatically issued after the job of the refresh group are created by DBMS_REFRESH.MAKE . FALSE —user must issue a commit statement to finish the transaction after calling DBMS_REFRESH.MAKE . The default value is NULL . |

## Usage Notes

Syntax DBMS_REFRESH.MAKE ( name IN VARCHAR2 { list IN VARCHAR2, | tab IN DBMS_UTILITY.UNCL_ARRAY,} next_date IN DATE, interval IN VARCHAR2, implicit_destroy IN BOOLEAN := FALSE, lax IN BOOLEAN := FALSE, job IN BINARY_INTEGER := 0, rollback_seg IN VARCHAR2 := NULL, push_deferred_rpc IN BOOLEAN := TRUE, refresh_after_errors IN BOOLEAN := FALSE purge_option IN BINARY_INTEGER := NULL, parallelism IN BINARY_INTEGER := NULL, heap_size IN BINARY_INTEGER := NULL job_name IN VARCHAR2 := NULL, auto_commit IN BOOLEAN := NULL); Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Parameters Table 139-5 MAKE Procedure Parameters Parameter Description name Unique name used to identify the refresh group, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. Refresh groups must follow the same naming conventions as tables. list Comma-delimited list of materialized views that you want to refresh. Synonyms are not supported. These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. tab Instead of a comma-delimited list, you can supply a PL/SQL associative array of names of materialized views that you want to refresh using the data type DBMS_UTILITY.UNCL_ARRAY . If the table contains the names of n materialized views, then the first materialized view should be in position 1 and the n + 1 position should be set to NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. next_date Next date that you want a refresh to occur. interval Function used to calculate the next time to refresh the materialized views in the group. This field is used with the next_date value. For example, if you specify NEXT_DAY(SYSDATE+1, "MONDAY") as your interval, and if your next_date evaluates to Monday, then Oracle refreshes the materialized views every Monday. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. implicit_destroy Set this to TRUE to delete the refresh group automatically when it no longer contains any members. Oracle checks this flag only when you call the SUBTRACT procedure. That is, setting this flag still enables you to create an empty refresh group. lax A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from an existing group to a new refresh group, then you must set this to TRUE to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to MAKE generates an error message. job Needed by the Import utility. Use the default value, 0. rollback_seg Name of the rollback segment to use while refreshing materialized views. The default, NULL , uses the default rollback segment. push_deferred_rpc Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. refresh_after_errors Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. purge_option Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. parallelism 0 specifies serial propagation. n > 1 specifies parallel propagation with n parallel processes. 1 specifies parallel propagation using only one parallel process. heap_size Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance. Note: Do not set this parameter unless directed to do so by Oracle Support Services. job_name This parameter is needed by the import utility. User should use the default value, NULL . auto_commit Supported values are NULL , TRUE , and FALSE . NULL —allows the user to continue using DBMS_JOB . TRUE —commit statement will be automatically issued after the job of the refresh group are created by DBMS_REFRESH.MAKE . FALSE —user must issue a commit statement to finish the transaction after calling DBMS_REFRESH.MAKE . The default value is NULL . Note: Do not set this parameter unless directed to do so by Oracle Support Services. Usage Notes Import utility and export utility need CREATE JOB privilege if DBMS_SCHEDULER jobs are used.