---
id: 19c__DBMS_REFRESH.CHANGE
name: DBMS_REFRESH.CHANGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.CHANGE

This procedure changes the refresh interval for a refresh group.

## Syntax

```sql
DBMS_REFRESH.CHANGE (
   name                  IN VARCHAR2,
   next_date             IN DATE           := NULL,
   interval              IN VARCHAR2       := NULL,
   implicit_destroy      IN BOOLEAN        := NULL,
   rollback_seg          IN VARCHAR2       := NULL,
   push_deferred_rpc     IN BOOLEAN        := NULL,
   refresh_after_errors  IN BOOLEAN        := NULL,
   purge_option          IN BINARY_INTEGER := NULL,
   parallelism           IN BINARY_INTEGER := NULL,
   heap_size             IN BINARY_INTEGER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the refresh group for which you want to alter the refresh interval. |
| next_date | DATE | IN | Next date that you want a refresh to occur. By default, this date remains unchanged. |
| interval | VARCHAR2 | IN | Function used to calculate the next time to refresh the materialized views in the refresh group. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. By default, the interval remains unchanged. |
| implicit_destroy | BOOLEAN | IN | Allows you to reset the value of the implicit_destroy flag. If this flag is set, then Oracle automatically deletes the group if it no longer contains any members. By default, this flag remains unchanged. |
| rollback_seg | VARCHAR2 | IN | Allows you to change the rollback segment used. By default, the rollback segment remains unchanged. To reset this parameter to use the default rollback segment, specify NULL , including the quotes. Specifying NULL without quotes indicates that you do not want to change the rollback segment currently being used. |
| push_deferred_rpc | BOOLEAN | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| refresh_after_errors | BOOLEAN | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| purge_option | BINARY_INTEGER | IN | Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. |
| parallelism | BINARY_INTEGER | IN | 0 specifies serial propagation. n > 1 specifies parallel propagation with n parallel processes. 1 specifies parallel propagation using only one parallel process. |
| heap_size | BINARY_INTEGER | IN | Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance. Note: Do not set this parameter unless directed to do so by Oracle Support Services. |

## Usage Notes

Syntax DBMS_REFRESH.CHANGE ( name IN VARCHAR2, next_date IN DATE := NULL, interval IN VARCHAR2 := NULL, implicit_destroy IN BOOLEAN := NULL, rollback_seg IN VARCHAR2 := NULL, push_deferred_rpc IN BOOLEAN := NULL, refresh_after_errors IN BOOLEAN := NULL, purge_option IN BINARY_INTEGER := NULL, parallelism IN BINARY_INTEGER := NULL, heap_size IN BINARY_INTEGER := NULL); Parameters Table 139-3 CHANGE Procedure Parameters Parameter Description name Name of the refresh group for which you want to alter the refresh interval. next_date Next date that you want a refresh to occur. By default, this date remains unchanged. interval Function used to calculate the next time to refresh the materialized views in the refresh group. This interval is evaluated immediately before the refresh. Thus, select an interval that is greater than the time it takes to perform a refresh. By default, the interval remains unchanged. implicit_destroy Allows you to reset the value of the implicit_destroy flag. If this flag is set, then Oracle automatically deletes the group if it no longer contains any members. By default, this flag remains unchanged. rollback_seg Allows you to change the rollback segment used. By default, the rollback segment remains unchanged. To reset this parameter to use the default rollback segment, specify NULL , including the quotes. Specifying NULL without quotes indicates that you do not want to change the rollback segment currently being used. push_deferred_rpc Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. refresh_after_errors Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. purge_option Starting with Oracle Database 12 c Release 2 (12.2), this parameter is ignored. parallelism 0 specifies serial propagation. n > 1 specifies parallel propagation with n parallel processes. 1 specifies parallel propagation using only one parallel process. heap_size Maximum number of transactions to be examined simultaneously for parallel propagation scheduling. Oracle automatically calculates the default setting for optimal performance. Note: Do not set this parameter unless directed to do so by Oracle Support Services. Note: Do not set this parameter unless directed to do so by Oracle Support Services.