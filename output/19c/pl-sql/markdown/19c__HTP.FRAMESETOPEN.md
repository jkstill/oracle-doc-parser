---
id: 19c__HTP.FRAMESETOPEN
name: HTP.FRAMESETOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FRAMESETOPEN

This procedure generates the <FRAMESET> tag which define a frameset section.

## Syntax

```sql
HTP.FRAMESETOPEN(
   crows          IN       VARCHAR2   DEFAULT NULL,
   ccols          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| crows | VARCHAR2 | IN | The value for the ROWS attribute. |
| ccols | VARCHAR2 | IN | The value for the COLS attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You mark the end of a frameset section by means of the FRAMESETCLOSE Procedure . Syntax HTP.FRAMESETOPEN( crows IN VARCHAR2 DEFAULT NULL, ccols IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-45 FRAMESETOPEN Procedure Parameters Parameter Description crows The value for the ROWS attribute. ccols The value for the COLS attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <FRAMESET ROWS=" crows " COLS=" ccols " cattributes >