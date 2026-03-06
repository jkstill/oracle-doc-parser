---
id: 19c__HTF.MAILTO
name: HTF.MAILTO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.MAILTO

This function generates the <A> tag with the HREF set to 'mailto' prepended to the mail address argument.

## Syntax

```sql
HTF.MAILTO(
   caddress       IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| caddress | VARCHAR2 | IN | The email address of the recipient. |
| ctext | VARCHAR2 | IN | The clickable portion of the link. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.MAILTO( caddress IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-61 MAILTO Function Parameters Parameter Description caddress The email address of the recipient. ctext The clickable portion of the link. cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <A HREF="mailto:caddress" NAME="cname" cattributes>ctext</A> so that HTF.mailto('pres@white_house.gov','Send Email to the President'); generates: <A HREF="mailto:pres@white_house.gov">Send Email to the President</A>