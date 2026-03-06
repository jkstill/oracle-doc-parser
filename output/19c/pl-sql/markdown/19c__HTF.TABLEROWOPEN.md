---
id: 19c__HTF.TABLEROWOPEN
name: HTF.TABLEROWOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.TABLEROWOPEN

This function generates the <TR> tag which marks the beginning of a new row in an HTML table.

## Syntax

```sql
HTF.TABLEROWOPEN(
   calign         IN       VARCHAR2   DEFAULT NULL,
   cvalign        IN       VARCHAR2   DEFAULT NULL,
   cdp            IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cvalign | VARCHAR2 | IN | The value for the VALIGN attribute. |
| cdp | VARCHAR2 | IN | The value for the DP attribute. |
| cnowrap | VARCHAR2 | IN | If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a new row, use the TABLEROWCLOSE Function . Syntax HTF.TABLEROWOPEN( calign IN VARCHAR2 DEFAULT NULL, cvalign IN VARCHAR2 DEFAULT NULL, cdp IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-86 TABLEROWOPEN Function Parameters Parameter Description calign The value for the ALIGN attribute. cvalign The value for the VALIGN attribute. cdp The value for the DP attribute. cnowrap If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This function generates <<TR ALIGN="calign" VALIGN="cvalign" DP="cdp" NOWRAP cattributes>