---
id: 19c__DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL
name: DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_REPORT
tags: [dbms_auto_report]
source_file: DBMS_AUTO_REPORT.html
---

# DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL

This procedure obtains the stored report for a given report ID in the specified format such as XML or HTML.

## Syntax

```sql
DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL (
   rid              IN NUMBER    DEFAULT NULL,
   type             IN VARCHAR2  DEFAULT 'XML',
   base_path        IN VARCHAR2  DEFAULT NULL)
 RETURNS CLOB
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rid | NUMBER | IN | ID of the stored report which returned by the function |
| type | VARCHAR2 | IN | Desired format of the report. Values can be 'XML' , 'TEXT' , ' HTML' , 'EM' or 'ACTIVE' . The last two options generate a report in the same format called active HTML. Default value is 'XML' . |
| base_path | VARCHAR2 | IN | Unused/Non-operative |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_AUTO_REPORT.REPORT_REPOSITORY_DETAIL ( rid IN NUMBER DEFAULT NULL, type IN VARCHAR2 DEFAULT 'XML', base_path IN VARCHAR2 DEFAULT NULL) RETURNS CLOB Parameters Table 31-2 REPORT_REPOSITORY_DETAIL Function Parameters Parameter Description rid ID of the stored report which returned by the function type Desired format of the report. Values can be 'XML' , 'TEXT' , ' HTML' , 'EM' or 'ACTIVE' . The last two options generate a report in the same format called active HTML. Default value is 'XML' . base_path Unused/Non-operative Return Values The persisted report for the given record ID