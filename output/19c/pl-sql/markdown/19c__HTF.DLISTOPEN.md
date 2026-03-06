---
id: 19c__HTF.DLISTOPEN
name: HTF.DLISTOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DLISTOPEN

This function generates the <DL> tag which starts a definition list. You end a definition list by means of the DLISTCLOSE Function.

## Syntax

```sql
HTF.DLISTOPEN (
   cclear         IN       VARCHAR2   DEFAULT NULL,
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

Syntax HTF.DLISTOPEN ( cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-22 DLISTOPEN Function Parameters Parameter Description cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Usage Notes A definition list looks like a glossary: it contains terms and definitions. Terms are inserted using the DLISTTERM Function and definitions are inserted using the DLISTDEF Function . Examples This function generates <DL CLEAR="cclear" cattributes>