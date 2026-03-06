---
id: 19c__DBMS_STATS.PURGE_STATS
name: DBMS_STATS.PURGE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.PURGE_STATS

This procedure purges old versions of statistics saved in the dictionary.

## Syntax

```sql
DBMS_STATS.PURGE_STATS( 
    before_timestamp       TIMESTAMP WITH TIME ZONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| before_timestamp | TIMESTAMP | IN | Versions of statistics saved before this timestamp are purged. If NULL , it uses the purging policy used by automatic purge. The automatic purge deletes all history older than the older of (current time - statistics history retention) and (time of recent analyze in the system - 1). The statistics history retention value can be changed using ALTER_STATS_HISTORY_RETENTION Procedure.The default is 31 days. |

## Usage Notes

To run this procedure, you must have the SYSDBA or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privilege. Syntax DBMS_STATS.PURGE_STATS( before_timestamp TIMESTAMP WITH TIME ZONE); Parameters Table 171-96 PURGE_STATS Procedure Parameters Parameter Description before_timestamp Versions of statistics saved before this timestamp are purged. If NULL , it uses the purging policy used by automatic purge. The automatic purge deletes all history older than the older of (current time - statistics history retention) and (time of recent analyze in the system - 1). The statistics history retention value can be changed using ALTER_STATS_HISTORY_RETENTION Procedure.The default is 31 days. Exceptions ORA-20000 : Object does not exist or insufficient privileges ORA-20001 : Invalid or inconsistent values Usage Notes To invoke this procedure you need the ANALYZE ANY privilege and the ANALYZE ANY DICTIONARY privilege.