---
id: 19c__HTF.FORMTEXT
name: HTF.FORMTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMTEXT

This function generates the <INPUT> tag with TYPE="text" , which creates a field for a single line of text.

## Syntax

```sql
HTF.FORMTEXT(
   cname          IN       VARCHAR2,
   csize          IN       VARCHAR2   DEFAULT NULL,
   cmaxlength     IN       VARCHAR2   DEFAULT NULL,
   cvalue         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| csize | VARCHAR2 | IN | The value for the SIZE attribute. |
| cmaxlength | VARCHAR2 | IN | The value for the MAXLENGTH attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.FORMTEXT( cname IN VARCHAR2, csize IN VARCHAR2 DEFAULT NULL, cmaxlength IN VARCHAR2 DEFAULT NULL, cvalue IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-41 FORMTEXT Function Parameters Parameter Description cname The value for the NAME attribute. csize The value for the SIZE attribute. cmaxlength The value for the MAXLENGTH attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="text" NAME="cname" SIZE="csize" MAXLENGTH="cmaxlength" VALUE="cvalue" cattributes>