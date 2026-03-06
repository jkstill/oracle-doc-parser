---
id: 19c__DBMS_AUTO_REPORT.START_REPORT_CAPTURE
name: DBMS_AUTO_REPORT.START_REPORT_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_REPORT
tags: [dbms_auto_report]
source_file: DBMS_AUTO_REPORT.html
---

# DBMS_AUTO_REPORT.START_REPORT_CAPTURE

This procedure captures SQL monitor data of any newly monitored SQLs every minute since the last run of the capture cycle, and stores it in AWR.

## Syntax

```sql
DBMS_AUTO_REPORT.START_REPORT_CAPTURE;
```

## Usage Notes

Every capture cycle attempts to capture data for SQLs that are not currently executing or queued. This is a complete capture since data of all newly monitored SQLs is captured. It continues to run every minute until it is explicitly ended with the FINISH_REPORT_CAPTURE Procedure . In the case of a RAC system, the capture will start on each node of the cluster. Syntax DBMS_AUTO_REPORT.START_REPORT_CAPTURE;