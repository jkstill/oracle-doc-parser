---
id: 19c__DBMS_HM.GET_RUN_REPORT
name: DBMS_HM.GET_RUN_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HM
tags: [dbms_hm]
source_file: DBMS_HM.html
---

# DBMS_HM.GET_RUN_REPORT

This function returns the report for the specified checker run.

## Syntax

```sql
DBMS_HM.GET_RUN_REPORT (
    run_name      IN  VARCHAR2,
    type           IN  VARCHAR2 := 'TEXT',
    level          IN  VARCHAR2 := 'BASIC',) 
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| run_name | VARCHAR2 | IN | Name of the check's run |
| type | VARCHAR2 | IN | Report format type. Possible values are 'HTML' , 'XML' and 'TEXT' . Default report type is 'TEXT' . |
| level | VARCHAR2 | IN | Details of report, possible value are 'BASIC' and 'DETAIL' . Caution: Currently only 'BASIC' level is supported. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_HM.GET_RUN_REPORT ( run_name IN VARCHAR2, type IN VARCHAR2 := 'TEXT', level IN VARCHAR2 := 'BASIC',) RETURN CLOB; Parameters Table 82-2 GET_RUN_REPORT Function Parameters Parameter Description run_name Name of the check's run type Report format type. Possible values are 'HTML' , 'XML' and 'TEXT' . Default report type is 'TEXT' . level Details of report, possible value are 'BASIC' and 'DETAIL' . Caution: Currently only 'BASIC' level is supported.