---
id: 19c__HTP.PARAGRAPH
name: HTP.PARAGRAPH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PARAGRAPH

You can use this procedure to add attributes to the <P> tag created by the PARA Procedure.

## Syntax

```sql
HTP.PARAGRAPH(
   calign         IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cnowrap | VARCHAR2 | IN | If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.PARAGRAPH( calign IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-65 PARAGRAPH Procedure Parameters Parameter Description calign The value for the ALIGN attribute. cnowrap If the value for this parameter is not NULL , the NOWRAP attribute is added to the tag. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <P ALIGN=" calign " NOWRAP CLEAR=" cclear " cattributes >