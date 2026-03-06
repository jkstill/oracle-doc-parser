---
id: 19c__UTL_RPADV.STOP_MONITORING
name: UTL_RPADV.STOP_MONITORING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.STOP_MONITORING

This procedure stops a monitoring job that was submitted by the current user.

## Syntax

```sql
UTL_RPADV.STOP_MONITORING(
   purge IN BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| purge | BOOLEAN | IN | If TRUE , then the procedure purges information about the monitoring job from the result tables. If FALSE , then the procedure retains information about the monitoring job in the result tables. |

## Usage Notes

Syntax UTL_RPADV.STOP_MONITORING( purge IN BOOLEAN DEFAULT FALSE); Parameters Table 275-22 STOP_MONITORING Procedure Parameters Parameter Description purge If TRUE , then the procedure purges information about the monitoring job from the result tables. If FALSE , then the procedure retains information about the monitoring job in the result tables.