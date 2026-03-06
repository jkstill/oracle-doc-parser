---
id: 19c__HTP.PRINTS
name: HTP.PRINTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PRINTS

This procedure generates a string and replaces certain characters with a corresponding escape sequence.

## Syntax

```sql
HTP.PRINTS (
   ctext      IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The string where to perform character substitution. |

## Usage Notes

The following characters are replaced with the corresponding escape sequence. < to &lt; > to &gt; " to &quot; & to &amp; If not replaced, the special characters are interpreted as HTML control characters and produce garbled output. This procedure an the PS Procedure perform the same operation as the PRN Procedures but with character substitution. Syntax HTP.PRINTS ( ctext IN VARCHAR2); Parameters Table 221-70 PRINTS Procedure Parameters Parameter Description ctext The string where to perform character substitution. Usage Notes This procedure does not have an HTF function equivalent (see Operational Notes for the HTF implementation).