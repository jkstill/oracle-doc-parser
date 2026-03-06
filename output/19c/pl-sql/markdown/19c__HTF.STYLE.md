---
id: 19c__HTF.STYLE
name: HTF.STYLE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.STYLE

This function generates the <STYLE> and </STYLE> tags which include a style sheet in a Web page.

## Syntax

```sql
HTF.STYLE(
   cstyle          IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cstyle | VARCHAR2) | IN | The style information to include. |

**Returns:** `VARCHAR2`

## Usage Notes

You can get more information about style sheets at http://www.w3.org. This feature is not compatible with browsers that support only HTML versions 2.0 or earlier. Such browsers will ignore this tag. Syntax HTF.STYLE( cstyle IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-79 STYLE Function Parameters Parameter Description cstyle The style information to include. Examples This function generates <STYLE>cstyle</STYLE>