---
id: 19c__HTP.DFN
name: HTP.DFN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DFN

This procedure generates the <DFN> and </DFN> tags which direct the browser to mark the text in italics or however "definition" is described stylistically.

## Syntax

```sql
HTP.DFN (
   ctext          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text to render in italics. |

## Usage Notes

Syntax HTP.DFN ( ctext IN VARCHAR2); Parameters Table 221-19 DFN Procedure Parameters Parameter Description ctext The text to render in italics. Examples This procedure generates <DFN> ctext </DFN>