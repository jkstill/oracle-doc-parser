---
id: 19c__HTP.PREOPEN
name: HTP.PREOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PREOPEN

This procedure generates the <PRE> tag which marks the beginning of a section of preformatted text in the body of the HTML page.

## Syntax

```sql
HTP.PREOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwidth         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwidth | VARCHAR2 | IN | The value for the WIDTH attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

To mark the end of a section of preformatted text in the body of the HTML page, use the PRECLOSE Procedure . Syntax HTP.PREOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwidth IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-68 PREOPEN Procedure Parameters Parameter Description cclear The value for the CLEAR attribute. cwidth The value for the WIDTH attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <PRE CLEAR=" cclear " WIDTH=" cwidth " cattributes >