---
id: 19c__HTF.FORMHIDDEN
name: HTF.FORMHIDDEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMHIDDEN

This function generates the <INPUT> tag with TYPE="hidden", which inserts a hidden form element.

## Syntax

```sql
HTF.FORMHIDDEN(
   cname          IN       VARCHAR2,
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

This element is not seen by the user. It submits additional values to the script. Syntax HTF.FORMHIDDEN( cname IN VARCHAR2, cvalue IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-32 FORMHIDDEN Function Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="hidden" NAME="cname" VALUE="cvalue" cattributes>