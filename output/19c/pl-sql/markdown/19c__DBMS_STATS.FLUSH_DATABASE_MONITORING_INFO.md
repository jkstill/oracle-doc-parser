---
id: 19c__DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO
name: DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO

This procedure saves monitoring information for all tables in the dictionary. The database immediately updates corresponding entries in the *_TAB_MODIFICATIONS , *_TAB_STATISTICS and *_IND_STATISTICS views.

## Syntax

```sql
DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO;
```

## Usage Notes

Syntax DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO; Security Model The ANALYZE_ANY system privilege is required to run this procedure. Exceptions ORA-20000 : Insufficient privileges Usage Notes Starting in Oracle Database 12c Release 2 (12.2), you do not need to call FLUSH_DATABASE_MONITORING_ INFO to view the latest information in *_TAB_STATISTICS and *_IND_STATISTICS because these views show statistics cached in the SGA and stored on disk. Because the GATHER_*_STATS procedures internally save monitoring information to disk, it is not necessary to run this procedure before gathering statistics. See Also: Oracle Database SQL Tuning Guide to learn how to set optimizer statistics preferences See Also: Oracle Database SQL Tuning Guide to learn how to set optimizer statistics preferences