---
id: 19c__HTP.TITLE
name: HTP.TITLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.TITLE

This procedure generates the <TITLE> and </TITLE> tags which specify the text to display in the titlebar of the browser window.

## Syntax

```sql
HTP.TITLE(
   ctitle          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctitle | VARCHAR2) | IN | The text to display in the titlebar of the browser window. |

## Usage Notes

Syntax HTP.TITLE( ctitle IN VARCHAR2); Parameters Table 221-88 TITLE Procedure Parameters Parameter Description ctitle The text to display in the titlebar of the browser window. Examples This procedure generates <TITLE> ctitle </TITLE>