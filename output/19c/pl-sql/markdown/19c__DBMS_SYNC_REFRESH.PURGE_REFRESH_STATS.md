---
id: 19c__DBMS_SYNC_REFRESH.PURGE_REFRESH_STATS
name: DBMS_SYNC_REFRESH.PURGE_REFRESH_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.PURGE_REFRESH_STATS

This procedure purges the refresh history of sync refreshes that took place before the value specified by the BEFORE_TIMESTAMP parameter.

## Syntax

```sql
DBMS_SYNC_REFRESH.PURGE_REFRESH_STATS (
   before_timestamp IN TIMESTAMP WITH TIME ZONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| before_timestamp | TIMESTAMP | IN | Records of sync refreshes saved before this timestamp are purged. If NULL , it uses the purging policy used by automatic purge. The automatic purge deletes all history older than (current time - refresh - history retention). The refresh history retention value can be changed using ALTER_REFRESH_STATS_RETENTION . The default is 31 days. |

## Usage Notes

This procedure requires the SYSDBA privilege in addition to the privilege to execute it. Syntax DBMS_SYNC_REFRESH.PURGE_REFRESH_STATS ( before_timestamp IN TIMESTAMP WITH TIME ZONE); Parameters Table 173-11 PURGE_REFRESH_STATS Procedure Parameter Parameter Description before_timestamp Records of sync refreshes saved before this timestamp are purged. If NULL , it uses the purging policy used by automatic purge. The automatic purge deletes all history older than (current time - refresh - history retention). The refresh history retention value can be changed using ALTER_REFRESH_STATS_RETENTION . The default is 31 days.