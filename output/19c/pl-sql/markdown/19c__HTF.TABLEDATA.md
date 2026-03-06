---
id: 19c__HTF.TABLEDATA
name: HTF.TABLEDATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.TABLEDATA

This function generates the <TD> and </TD> tags which insert data into a cell of an HTML table.

## Syntax

```sql
HTF.TABLEDATA(
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cdp            IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   crowspan       IN       VARCHAR2   DEFAULT NULL,
   ccolspan       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The data for the cell in the table. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cdp | VARCHAR2 | IN | The value for the DP attribute. |
| cnowrap | VARCHAR2 | IN | If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. |
| ccolspan | VARCHAR2 | IN | The value for the COLSPAN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.TABLEDATA( cvalue IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, cdp IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, crowspan IN VARCHAR2 DEFAULT NULL, ccolspan IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-83 TABLEDATA Function Parameters Parameter Description cvalue The data for the cell in the table. calign The value for the ALIGN attribute. cdp The value for the DP attribute. cnowrap If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. ccolspan The value for the COLSPAN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <TD ALIGN="calign" DP="cdp" ROWSPAN="crowspan" COLSPAN="ccolspan" NOWRAP cattributes>cvalue</TD>