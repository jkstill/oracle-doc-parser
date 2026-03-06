---
id: 19c__HTF.FORMCHECKBOX
name: HTF.FORMCHECKBOX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMCHECKBOX

This function generates the <INPUT> tag with TYPE="checkbox" which inserts a checkbox element in a form.

## Syntax

```sql
HTF.FORMCHECKBOX(
   cname          IN       VARCHAR2,
   cvalue         IN       VARCHAR2   DEFAULT 'ON',
   cchecked       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2 | IN | The value for the VALUE attribute. |
| cchecked | VARCHAR2 | IN | If the value for this parameter is not NULL , the CHECKED attribute is added to the tag. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

A checkbox element is a button that the user toggles on or off. Syntax HTF.FORMCHECKBOX( cname IN VARCHAR2, cvalue IN VARCHAR2 DEFAULT 'ON', cchecked IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-30 FORMCHECKBOX Function Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cchecked If the value for this parameter is not NULL , the CHECKED attribute is added to the tag. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="checkbox" NAME="cname" VALUE="cvalue" CHECKED cattributes>