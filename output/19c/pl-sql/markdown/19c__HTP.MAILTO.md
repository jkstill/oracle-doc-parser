---
id: 19c__HTP.MAILTO
name: HTP.MAILTO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.MAILTO

This procedure generates the <A> tag with the HREF set to 'mailto' prepended to the mail address argument.

## Syntax

```sql
HTP.MAILTO(
   caddress       IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| caddress | VARCHAR2 | IN | The email address of the recipient. |
| ctext | VARCHAR2 | IN | The clickable portion of the link. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.MAILTO( caddress IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-59 MAILTO Procedure Parameters Parameter Description caddress The email address of the recipient. ctext The clickable portion of the link. cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <A HREF="mailto: caddress " NAME=" cname " cattributes > ctext </A> so that HTP.mailto('pres@white_house.gov','Send Email to the President'); generates: <A HREF="mailto:pres@white_house.gov">Send Email to the President</A>