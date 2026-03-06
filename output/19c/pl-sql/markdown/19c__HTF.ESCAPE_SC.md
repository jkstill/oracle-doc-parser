---
id: 19c__HTF.ESCAPE_SC
name: HTF.ESCAPE_SC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ESCAPE_SC

This function replaces characters that have special meaning in HTML with their escape sequences.

## Syntax

```sql
HTF.ESCAPE_SC(
     ctext          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text string to convert. |

**Returns:** `UNKNOWN`

## Usage Notes

The following characters are converted: & to &amp; " to &quot: < to &lt; > to &gt; This function performs the same operation as HTP. PRINTS Procedure and HTP. PS Procedure . Syntax HTF.ESCAPE_SC( ctext IN VARCHAR2); Parameters Table 220-26 ESCAPE_SC Function Parameters Parameter Description ctext The text string to convert.