---
id: 19c__HTP.TABLEOPEN
name: HTP.TABLEOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.TABLEOPEN

This procedure generates the <TABLE> tag which marks the beginning of an HTML table.

## Syntax

```sql
HTP.TABLEOPEN(
   cborder        IN       VARCHAR2   DEFAULT NULL
   calign         IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| border |  |  | The value for the BORDER attribute. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cnowrap | VARCHAR2 | IN | If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To define the end of an HTML table, use the TABLECLOSE Procedure . Syntax HTP.TABLEOPEN( cborder IN VARCHAR2 DEFAULT NULL calign IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-85 TABLEOPEN Procedure Parameters Parameter Description border The value for the BORDER attribute. calign The value for the ALIGN attribute. cnowrap If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <TABLE " cborder " NOWRAP ALIGN=" calign " CLEAR=" cclear " cattributes >