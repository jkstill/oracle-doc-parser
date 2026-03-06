---
id: 19c__HTP.ESCAPE_SC
name: HTP.ESCAPE_SC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ESCAPE_SC

This procedure replaces characters that have special meaning in HTML with their escape sequences.

## Syntax

```sql
HTP.ESCAPE_SC(
     ctext          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text string to convert. |

## Usage Notes

The following characters are converted: & to &amp; " to &quot: < to &lt; > to &gt; This procedure performs the same operation as PRINTS Procedure s and PS Procedure . Syntax HTP.ESCAPE_SC( ctext IN VARCHAR2); Parameters Table 221-26 ESCAPE_SC Procedure Parameters Parameter Description ctext The text string to convert.