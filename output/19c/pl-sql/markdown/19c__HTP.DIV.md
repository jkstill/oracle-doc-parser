---
id: 19c__HTP.DIV
name: HTP.DIV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.DIV

This procedure generates the <DIV> tag which creates document divisions.

## Syntax

```sql
HTP.DIV (
   calign         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.DIV ( calign IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-20 DIV Procedure Parameters Parameter Description calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <DIV ALIGN=" calign " cattributes >