---
id: 19c__HTP.CENTER
name: HTP.CENTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.CENTER

This procedure generates the <CENTER> and </CENTER> tags which center a section of text within a Web page.

## Syntax

```sql
HTP.CENTER (
   ctext          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text that goes between the tags. |

## Usage Notes

Syntax HTP.CENTER ( ctext IN VARCHAR2); Parameters Table 221-15 CENTER Parameters Parameter Description ctext The text that goes between the tags. Examples This procedure generates <CENTER> ctext </CENTER>