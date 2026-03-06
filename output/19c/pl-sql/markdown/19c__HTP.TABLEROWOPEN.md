---
id: 19c__HTP.TABLEROWOPEN
name: HTP.TABLEROWOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.TABLEROWOPEN

This procedure generates the <TR> tag which marks the beginning of a new row in an HTML table.

## Syntax

```sql
HTP.TABLEROWOPEN(
   calign         IN       VARCHAR2   DEFAULT NULL,
   cvalign        IN       VARCHAR2   DEFAULT NULL,
   cdp            IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cvalign | VARCHAR2 | IN | The value for the VALIGN attribute. |
| cdp | VARCHAR2 | IN | The value for the DP attribute. |
| cnowrap | VARCHAR2 | IN | If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To mark the end of a new row, use the TABLEROWCLOSE Procedure . Syntax HTP.TABLEROWOPEN( calign IN VARCHAR2 DEFAULT NULL, cvalign IN VARCHAR2 DEFAULT NULL, cdp IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-86 TABLEROWOPEN Procedure Parameters Parameter Description calign The value for the ALIGN attribute. cvalign The value for the VALIGN attribute. cdp The value for the DP attribute. cnowrap If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <<TR ALIGN=" calign " VALIGN=" cvalign " DP=" cdp " NOWRAP cattributes >