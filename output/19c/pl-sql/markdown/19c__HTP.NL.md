---
id: 19c__HTP.NL
name: HTP.NL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.NL

This procedure generates the <BR> tag which begins a new line of text.

## Syntax

```sql
HTP.NL(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

It performs the same operation as the BR Procedure . Syntax HTP.NL( cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-62 NL Procedure Parameters Parameter Description cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BR CLEAR=" cclear " cattributes >