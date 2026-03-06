---
id: 19c__HTP.EM
name: HTP.EM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.EM

This procedure generates the <EM> and </EM> tags, which define text to be emphasized.

## Syntax

```sql
HTP.EM(
     ctext          IN       VARCHAR2,
     cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to emphasize. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

It performs the same task as the EMPHASIS Procedure . Syntax HTP.EM( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-24 EM Procedure Parameters Parameter Description ctext The text to emphasize. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <EM cattributes > ctext </EM>