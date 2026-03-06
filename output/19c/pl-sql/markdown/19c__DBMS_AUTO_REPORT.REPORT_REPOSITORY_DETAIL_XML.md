---
id: 19c__DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML
name: DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_REPORT
tags: [dbms_auto_report]
source_file: DBMS_AUTO_REPORT.html
---

# DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML

This procedure obtains the stored XML report for a given report ID.

## Syntax

```sql
DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML (
   rid              IN NUMBER    DEFAULT NULL,
   base_path        IN VARCHAR2  DEFAULT NULL)
 RETURNS XMLTYPE
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rid | NUMBER | IN | ID of the stored report which returned by the function |
| base_path | VARCHAR2 | IN | Unused/Non-operative |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL_XML ( rid IN NUMBER DEFAULT NULL, base_path IN VARCHAR2 DEFAULT NULL) RETURNS XMLTYPE Parameters Table 31-3 REPORT_REPOSITORY_DETAIL_XML Function Parameters Parameter Description rid ID of the stored report which returned by the function base_path Unused/Non-operative Return Values The persisted XML report for the given record ID