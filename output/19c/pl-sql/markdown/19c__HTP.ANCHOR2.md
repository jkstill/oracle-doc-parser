---
id: 19c__HTP.ANCHOR2
name: HTP.ANCHOR2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ANCHOR2

Like the ANCHOR procedure, this procedure generates the <A> and </A> HTML tags which specify the source or destination of a hypertext link.

## Syntax

```sql
HTP.ANCHOR2 (
   curl           IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2   DEFAULT NULL,
   ctarget        in       varchar2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the HREF attribute. |
| ctext | VARCHAR2 | IN | The string that goes between the <A> and </A> tags. |
| cname | VARCHAR2 | IN | The value for the NAME attribute |
| ctarget | varchar2 | in | The value for the TARGET attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

## Usage Notes

The difference between this procedure and the ANCHOR procedure is that this procedure provides a target and therefore can be used for a frame. Syntax HTP.ANCHOR2 ( curl IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2 DEFAULT NULL, ctarget in varchar2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-4 ANCHOR2 Procedure Parameters Parameter Description curl The value for the HREF attribute. ctext The string that goes between the <A> and </A> tags. cname The value for the NAME attribute ctarget The value for the TARGET attribute. cattributes The other attributes to be included as-is in the tag Examples This procedure generates <A HREF=" curl " NAME=" cname " TARGET = " ctarget " cattributes > ctext </A>