---
id: 19c__HTF.TITLE
name: HTF.TITLE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.TITLE

This function generates the <TITLE> and </TITLE> tags which specify the text to display in the titlebar of the browser window.

## Syntax

```sql
HTF.TITLE(
   ctitle          IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctitle | VARCHAR2) | IN | The text to display in the titlebar of the browser window. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.TITLE( ctitle IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-88 TITLE Function Parameters Parameter Description ctitle The text to display in the titlebar of the browser window. Examples This function generates <TITLE>ctitle</TITLE>