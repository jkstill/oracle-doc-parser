---
id: 19c__DBMS_SYNC_REFRESH.ALTER_REFRESH_STATS_RETENTION
name: DBMS_SYNC_REFRESH.ALTER_REFRESH_STATS_RETENTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.ALTER_REFRESH_STATS_RETENTION

This procedure alters the refresh history retention value, specified in days. It is intended for use in conjunction with PURGE_REFRESH_HISTORY . It also requires the SYSDBA privilege in addition to the privilege to execute it.

## Syntax

```sql
DBMS_SYNC_REFRESH.ALTER_REFRESH_STATS_RETENTION (
   retention   IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| retention | NUMBER) | IN | The retention time in days. The refresh history will be retained for at least these many number of days. The valid range is 1 to 365,000. You can use the following values for special purposes: -1 - Refresh history is never purged by PREPARE_REFRESH . 0 - Old refresh history is never saved. PREPARE_REFRESH will delete all refresh history. NULL - Change refresh history retention to default value. |

## Usage Notes

Syntax DBMS_SYNC_REFRESH.ALTER_REFRESH_STATS_RETENTION ( retention IN NUMBER); Parameters Table 173-3 ALTER_REFRESH_STATS_RETENTION Procedure Parameters Parameter Description retention The retention time in days. The refresh history will be retained for at least these many number of days. The valid range is 1 to 365,000. You can use the following values for special purposes: -1 - Refresh history is never purged by PREPARE_REFRESH . 0 - Old refresh history is never saved. PREPARE_REFRESH will delete all refresh history. NULL - Change refresh history retention to default value.