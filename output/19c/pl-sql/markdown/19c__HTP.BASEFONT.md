---
id: 19c__HTP.BASEFONT
name: HTP.BASEFONT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BASEFONT

This procedure generates the <BASEFONT> tag which specifies the base font size for a Web page.

## Syntax

```sql
HTP.BASEFONT (
   nsize    IN    INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nsize | INTEGER) | IN | The value for the SIZE attribute. |

## Usage Notes

Syntax HTP.BASEFONT ( nsize IN INTEGER); Parameters Table 221-8 BASEFONT Procedure Parameters Parameter Description nsize The value for the SIZE attribute. Examples This procedure generates <BASEFONT SIZE=" nsize ">