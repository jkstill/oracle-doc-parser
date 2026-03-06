---
id: 19c__HTF.FORMSUBMIT
name: HTF.FORMSUBMIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMSUBMIT

This function generates the <INPUT> tag with TYPE="submit" which creates a button that, when clicked, submits the form. If the button has a NAME attribute, the button contributes a name/value pair to the submitted data.

## Syntax

```sql
HTF.FORMSUBMIT(
   cname          IN       VARCHAR2   DEFAULT NULL,
   cvalue         IN       VARCHAR2   DEFAULT 'Submit',
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

Syntax HTF.FORMSUBMIT( cname IN VARCHAR2 DEFAULT NULL, cvalue IN VARCHAR2 DEFAULT 'Submit', cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-40 FORMSUBMIT Function Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="submit" NAME="cname" VALUE="cvalue" cattributes>