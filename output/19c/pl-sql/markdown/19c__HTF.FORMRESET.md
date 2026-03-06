---
id: 19c__HTF.FORMRESET
name: HTF.FORMRESET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMRESET

This function generates the <INPUT> tag with TYPE="reset" which creates a button that, when selected, resets the form fields to their initial values.

## Syntax

```sql
HTF.FORMRESET(
   cvalue         IN       VARCHAR2   DEFAULT 'Reset',
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.FORMRESET( cvalue IN VARCHAR2 DEFAULT 'Reset', cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-37 FORMRESET Function Parameters Parameter Description cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="reset" VALUE="cvalue" cattributes>