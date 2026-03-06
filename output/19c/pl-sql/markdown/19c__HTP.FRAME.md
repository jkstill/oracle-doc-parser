---
id: 19c__HTP.FRAME
name: HTP.FRAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FRAME

This procedure generates the <FRAME> tag which begins the characteristics of a frame created by a <FRAMESET> tag.

## Syntax

```sql
HTP.FRAME(
   csrc           IN       VARCHAR2,
   cname          IN       VARCHAR2   DEFAULT NULL,
   cmarginwidth   IN       VARCHAR2   DEFAULT NULL,
   cmarginheight  IN       VARCHAR2   DEFAULT NULL,
   cscrolling     IN       VARCHAR2   DEFAULT NULL,
   cnoresize      IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| csrc | VARCHAR2 | IN | The URL to display in the frame. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cmarginwidth | VARCHAR2 | IN | The value for the MARGINWIDTH attribute. |
| cscrolling | VARCHAR2 | IN | The value for the SCROLLING attribute. |
| cnoresize | VARCHAR2 | IN | If the value for this parameter is not NULL , the NORESIZE attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.FRAME( csrc IN VARCHAR2, cname IN VARCHAR2 DEFAULT NULL, cmarginwidth IN VARCHAR2 DEFAULT NULL, cmarginheight IN VARCHAR2 DEFAULT NULL, cscrolling IN VARCHAR2 DEFAULT NULL, cnoresize IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-44 FRAME Procedure Parameters Parameter Description csrc The URL to display in the frame. cname The value for the NAME attribute. cmarginwidth The value for the MARGINWIDTH attribute. cscrolling The value for the SCROLLING attribute. cnoresize If the value for this parameter is not NULL , the NORESIZE attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <FRAME SRC=" csrc " NAME=" cname " MARGINWIDTH=" cmarginwidth " MARGINHEIGHT=" cmarginheight " SCROLLING=" cscrolling " NORESIZE cattributes >