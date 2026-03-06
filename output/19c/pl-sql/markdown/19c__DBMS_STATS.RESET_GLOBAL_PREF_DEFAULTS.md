---
id: 19c__DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS
name: DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS

This procedures sets global preference, such as CASCADE , ESTIMATE_PERCENT and GRANULARITY , to default values.

## Syntax

```sql
DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS;
```

## Usage Notes

This reverses the global preferences set by the SET_GLOBAL_PREFS Procedure . Syntax DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS; Usage Notes To invoke this procedure you need the ANALYZE ANY privilege and the ANALYZE ANY DICTIONARY privilege.