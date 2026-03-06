---
id: 19c__DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE
name: DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_REPORT
tags: [dbms_auto_report]
source_file: DBMS_AUTO_REPORT.html
---

# DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE

This procedure ends the complete capture of SQL monitor data that was started with the START_REPORT_CAPTURE procedure.

## Syntax

```sql
DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE;
```

## Usage Notes

After calling this subprogram, capture of data continues every minute except that it is not captured for all active SQLs but only for those deemed important, namely the top 5 SQLs (by elapsed time, or elapsed time*DOP in case of PQ) whose monitoring has completed. Syntax DBMS_AUTO_REPORT.FINISH_REPORT_CAPTURE;