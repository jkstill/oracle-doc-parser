---
id: 19c__DBMS_STATS.ALTER_STATS_HISTORY_RETENTION
name: DBMS_STATS.ALTER_STATS_HISTORY_RETENTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.ALTER_STATS_HISTORY_RETENTION

This procedure changes the statistics history retention value.

## Syntax

```sql
DBMS_STATS.ALTER_STATS_HISTORY_RETENTION (
   retention       IN     NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| retention | NUMBER) | IN | The retention time in days. The statistics history will be retained for at least these many number of days.The valid range is [1,365000]. Also you can use the following values for special purposes: -1: Statistics history is never purged by automatic purge 0: Old statistics are never saved. The automatic purge will delete all statistics history NULL : Change statistics history retention to default value |

## Usage Notes

Statistics history retention is used by both the automatic purge and PURGE_STATS Procedure . Syntax DBMS_STATS.ALTER_STATS_HISTORY_RETENTION ( retention IN NUMBER); Parameters Table 171-4 ALTER_STATS_HISTORY_RETENTION Procedure Parameters Parameter Description retention The retention time in days. The statistics history will be retained for at least these many number of days.The valid range is [1,365000]. Also you can use the following values for special purposes: -1: Statistics history is never purged by automatic purge 0: Old statistics are never saved. The automatic purge will delete all statistics history NULL : Change statistics history retention to default value Usage Notes To run this procedure, you must have the SYSDBA or both ANALYZE ANY DICTIONARY and ANALYZE ANY system privilege. Exceptions ORA-20000 : Insufficient privileges