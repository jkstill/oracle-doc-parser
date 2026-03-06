---
id: 19c__DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY
name: DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY

This function returns oldest timestamp where statistics history is available. Users cannot restore statistics to a timestamp older than this one.

## Syntax

```sql
DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY
 RETURN TIMESTAMP WITH TIMEZONE;
```

**Returns:** `TIMESTAMP`

## Usage Notes

Syntax DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY RETURN TIMESTAMP WITH TIMEZONE; Usage Notes No special privilege or role is needed to invoke this procedure.