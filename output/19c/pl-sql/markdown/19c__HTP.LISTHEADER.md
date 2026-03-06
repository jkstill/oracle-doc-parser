---
id: 19c__HTP.LISTHEADER
name: HTP.LISTHEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.LISTHEADER

This procedure generates the <LH> and </LH> tags which print an HTML tag at the beginning of the list.

## Syntax

```sql
HTP.LISTHEADER(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to place between <LH> and </LH> . |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.LISTHEADER( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-57 LISTHEADER Procedure Parameters Parameter Description ctext The text to place between <LH> and </LH> . cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <LH cattributes > ctext </LH>