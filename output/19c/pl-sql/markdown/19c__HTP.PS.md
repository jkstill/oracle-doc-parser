---
id: 19c__HTP.PS
name: HTP.PS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PS

This procedure generates a string and replaces certain characters with the corresponding escape sequence.

## Syntax

```sql
HTP.PS (
   ctext      IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The string where to perform character substitution. |

## Usage Notes

This procedure replaces the following characters with the corresponding escape sequence. < to &lt; > to &gt; " to &quot; & to &amp; If not replaced, the special characters are interpreted as HTML control characters and produce garbled output. This procedure and the PRINTS Procedure perform the same operation as the PRN Procedures but with character substitution. Syntax HTP.PS ( ctext IN VARCHAR2); Parameters Table 221-72 PS Procedure Parameters Parameter Description ctext The string where to perform character substitution. Usage Notes This procedure does not have an HTF function equivalent (see Operational Notes for the HTF implementation).