---
id: 19c__HTF.BASEFONT
name: HTF.BASEFONT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BASEFONT

This function generates the <BASEFONT> tag which specifies the base font size for a Web page.

## Syntax

```sql
HTF.BASEFONT (
   nsize    IN    INTEGER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nsize | INTEGER) | IN | The value for the SIZE attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.BASEFONT ( nsize IN INTEGER) RETURN VARCHAR2; Parameters Table 220-8 BASEFONT Function Parameters Parameter Description nsize The value for the SIZE attribute. Examples This function generates <BASEFONT SIZE="nsize">