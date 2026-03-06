---
id: 19c__HTF.EM
name: HTF.EM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.EM

This function generates the <EM> and </EM> tags, which define text to be emphasized.

## Syntax

```sql
HTF.EM(
     ctext          IN       VARCHAR2,
     cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2 | IN | The text to emphasize. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

It performs the same task as the EMPHASIS Function . Syntax HTF.EM( ctext IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-24 EM Function Parameters Parameter Description ctext The text to emphasize. cattributes The other attributes to be included as-is in the tag. Examples This function generates <EM cattributes>ctext</EM>