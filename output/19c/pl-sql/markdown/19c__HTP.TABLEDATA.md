---
id: 19c__HTP.TABLEDATA
name: HTP.TABLEDATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.TABLEDATA

This procedure generates the <TD> and </TD> tags which insert data into a cell of an HTML table.

## Syntax

```sql
HTP.TABLEDATA(
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cdp            IN       VARCHAR2   DEFAULT NULL,
   cnowrap        IN       VARCHAR2   DEFAULT NULL,
   crowspan       IN       VARCHAR2   DEFAULT NULL,
   ccolspan       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
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

## Usage Notes

Syntax HTP.TABLEDATA( cvalue IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, cdp IN VARCHAR2 DEFAULT NULL, cnowrap IN VARCHAR2 DEFAULT NULL, crowspan IN VARCHAR2 DEFAULT NULL, ccolspan IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-83 TABLEDATA Procedure Parameters Parameter Description cvalue The data for the cell in the table. calign The value for the ALIGN attribute. cdp The value for the DP attribute. cnowrap If the value of this parameter is not NULL , the NOWRAP attribute is added to the tag. ccolspan The value for the COLSPAN attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <TD ALIGN=" calign " DP=" cdp " ROWSPAN=" crowspan " COLSPAN=" ccolspan " NOWRAP cattributes > cvalue </TD>