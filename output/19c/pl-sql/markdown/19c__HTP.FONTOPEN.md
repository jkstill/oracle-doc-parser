---
id: 19c__HTP.FONTOPEN
name: HTP.FONTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FONTOPEN

This procedure generates the <FONT> which marks the beginning of section of text with the specified font characteristics.

## Syntax

```sql
HTP.FONTOPEN(
   ccolor         IN       VARCHAR2   DEFAULT NULL,
   cface          IN       VARCHAR2   DEFAULT NULL,
   csize          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ccolor | VARCHAR2 | IN | The value for the COLOR attribute. |
| cface | VARCHAR2 | IN | The value for the FACE attribute |
| csize | VARCHAR2 | IN | The value for the SIZE attribute |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You mark the end of the section text by means of the FONTCLOSE Procedure . Syntax HTP.FONTOPEN( ccolor IN VARCHAR2 DEFAULT NULL, cface IN VARCHAR2 DEFAULT NULL, csize IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-27 FONTOPEN Procedure Parameters Parameter Description ccolor The value for the COLOR attribute. cface The value for the FACE attribute csize The value for the SIZE attribute cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <FONT COLOR=" ccolor " FACE=" cface " SIZE=" csize " cattributes >