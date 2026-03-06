---
id: 19c__HTF.PREOPEN
name: HTF.PREOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PREOPEN

This function generates the <PRE> tag which marks the beginning of a section of preformatted text in the body of the HTML page.

## Syntax

```sql
HTF.PREOPEN(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cwidth         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cwidth | VARCHAR2 | IN | The value for the WIDTH attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a section of preformatted text in the body of the HTML page, use the PRECLOSE Function . Syntax HTF.PREOPEN( cclear IN VARCHAR2 DEFAULT NULL, cwidth IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-70 PREOPEN Function Parameters Parameter Description cclear The value for the CLEAR attribute. cwidth The value for the WIDTH attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <PRE CLEAR="cclear" WIDTH="cwidth" cattributes>