---
id: 19c__HTF.DLISTDEF
name: HTF.DLISTDEF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DLISTDEF

This function generates the <DD> tag, which inserts definitions of terms. Use this tag for a definition list <DL> . Terms are tagged <DT> and definitions are tagged <DD> .

## Syntax

```sql
HTF.DLISTDEF (
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The definition of the term. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DLISTDEF ( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-21 DLISTDEF Function Parameters Parameter Description ctext The definition of the term. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <DD CLEAR="cclear" cattributes>ctext