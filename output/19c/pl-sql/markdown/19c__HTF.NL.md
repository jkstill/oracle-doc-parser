---
id: 19c__HTF.NL
name: HTF.NL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.NL

This function generates the <BR> tag which begins a new line of text.

## Syntax

```sql
HTF.NL(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

It performs the same operation as the BR Function . Syntax HTF.NL( cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-64 NL Function Parameters Parameter Description cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BR CLEAR="cclear" cattributes>