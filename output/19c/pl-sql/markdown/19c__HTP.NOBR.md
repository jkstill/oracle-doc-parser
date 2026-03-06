---
id: 19c__HTP.NOBR
name: HTP.NOBR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.NOBR

This procedure generates the <NOBR> and </NOBR> tags which turn off line-breaking in a section of text.

## Syntax

```sql
HTP.NOBR(
ctext        IN        VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The text that is to be rendered on one line. |

## Usage Notes

Syntax HTP.NOBR( ctext IN VARCHAR2); Parameters Table 221-63 NOBR Procedure Parameters Parameter Description ctext The text that is to be rendered on one line. Examples This procedure generates <NOBR> ctext </NOBR>