---
id: 19c__HTF.BASE
name: HTF.BASE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BASE

This function generates the <BASE> tag which records the URL of the document.

## Syntax

```sql
HTF.BASE (
   ctarget        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctarget | VARCHAR2 | IN | The value for the TARGET attribute which establishes a window name to which all links in this document are targeted. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.BASE ( ctarget IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-7 BASE Function Parameters Parameter Description ctarget The value for the TARGET attribute which establishes a window name to which all links in this document are targeted. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BASE HREF="<current URL>" TARGET="ctarget" cattributes>