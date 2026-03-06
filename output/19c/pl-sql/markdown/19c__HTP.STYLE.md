---
id: 19c__HTP.STYLE
name: HTP.STYLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.STYLE

This procedure generates the <STYLE> and </STYLE> tags which include a style sheet in a Web page.

## Syntax

```sql
HTP.STYLE(
   cstyle          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cstyle | VARCHAR2) | IN | The the style information to include. |

## Usage Notes

You can get more information about style sheets at http://www.w3.org . This feature is not compatible with browsers that support only HTML versions 2.0 or earlier. Such browsers will ignore this tag. HTP.STYLE( cstyle IN VARCHAR2); Parameters Table 221-79 STYLE Procedure Parameters Parameter Description cstyle The the style information to include. Examples This procedure generates <STYLE> cstyle </STYLE>