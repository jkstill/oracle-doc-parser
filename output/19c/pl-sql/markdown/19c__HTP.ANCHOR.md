---
id: 19c__HTP.ANCHOR
name: HTP.ANCHOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ANCHOR

Like the ANCHOR2 procedure, this procedure generates the <A> and </A> HTML tags which specify the source or destination of a hypertext link.

## Syntax

```sql
HTP.ANCHOR (
   curl           IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the HREF attribute. |
| ctext | VARCHAR2 | IN | The string that goes between the <A> and </A> tags. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

The difference between these subprograms is that the ANCHOR2 Procedure provides a target and therefore can be used for a frame. Syntax HTP.ANCHOR ( curl IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-3 ANCHOR Procedure Parameters Parameter Description curl The value for the HREF attribute. ctext The string that goes between the <A> and </A> tags. cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <A HREF=" curl " NAME=" cname " cattributes > ctext </A> Usage Notes This tag accepts several attributes, but either HREF or NAME is required. HREF specifies to where to link. NAME allows this tag to be a target of a hypertext link.