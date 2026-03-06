---
id: 19c__HTF.DLISTTERM
name: HTF.DLISTTERM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.DLISTTERM

This function generates the <DT> tag which defines a term in a definition list <DL> .

## Syntax

```sql
HTF.DLISTTERM (
   ctext          IN       VARCHAR2   DEFAULT NULL,
   cclear         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The term. |
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.DLISTTERM ( ctext IN VARCHAR2 DEFAULT NULL, cclear IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-23 DLISTTERM Function Parameters Parameter Description ctext The term. cclear The value for the CLEAR attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <DT CLEAR="cclear" cattributes>ctext