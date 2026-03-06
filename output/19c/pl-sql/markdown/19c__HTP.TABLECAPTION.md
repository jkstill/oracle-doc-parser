---
id: 19c__HTP.TABLECAPTION
name: HTP.TABLECAPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.TABLECAPTION

This procedure generates the <CAPTION> and </CAPTION> tags which place a caption in an HTML table.

## Syntax

```sql
HTP.TABLECAPTION(
   ccaption       IN       VARCHAR2,
   calign         in       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext |  |  | The text for the caption. |
| calign | VARCHAR2 | in | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.TABLECAPTION( ccaption IN VARCHAR2, calign in VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-82 TABLECAPTION Procedure Parameters Parameter Description ctext The text for the caption. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <CAPTION ALIGN=" calign " cattributes > ccaption </CAPTION>