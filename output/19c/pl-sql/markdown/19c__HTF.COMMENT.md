---
id: 19c__HTF.COMMENT
name: HTF.COMMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.COMMENT

This function generates the comment tags.

## Syntax

```sql
HTF.COMMENT (
   ctext          IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctext | VARCHAR2) | IN | The comment. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.COMMENT ( ctext IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-18 COMMENT Function Parameters Parameter Description ctext The comment. Examples This function generates <!-- ctext -->