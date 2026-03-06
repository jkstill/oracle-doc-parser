---
id: 19c__HTF.LISTHEADER
name: HTF.LISTHEADER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LISTHEADER

This function generates the <LH> and </LH> tags which print an HTML tag at the beginning of the list.

## Syntax

```sql
HTF.LISTHEADER(
   ctext          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to place between <LH> and </LH> . |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.LISTHEADER( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-59 LISTHEADER Function Parameters Parameter Description ctext The text to place between <LH> and </LH> . cattributes The other attributes to be included as-is in the tag. Examples This function generates <LH cattributes>ctext</LH>