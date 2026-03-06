---
id: 19c__HTF.ANCHOR2
name: HTF.ANCHOR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ANCHOR2

Like the ANCHOR function, this function generates the <A> and </A> HTML tags which specify the source or destination of a hypertext link.

## Syntax

```sql
HTF.ANCHOR2 (
   curl           IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2   DEFAULT NULL,
   ctarget        in       varchar2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the HREF attribute. |
| ctext | VARCHAR2 | IN | The string that goes between the <A> and </A> tags. |
| cname | VARCHAR2 | IN | The value for the NAME attribute |
| ctarget | varchar2 | in | The value for the TARGET attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag |

**Returns:** `VARCHAR2`

## Usage Notes

The difference between this and the ANCHOR function is that this function provides a target and therefore can be used for a frame. Syntax HTF.ANCHOR2 ( curl IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2 DEFAULT NULL, ctarget in varchar2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-4 ANCHOR2 Function Parameters Parameter Description curl The value for the HREF attribute. ctext The string that goes between the <A> and </A> tags. cname The value for the NAME attribute ctarget The value for the TARGET attribute. cattributes The other attributes to be included as-is in the tag Examples This function generates <A HREF="curl" NAME="cname" TARGET = "ctarget" cattributes>ctext</A>