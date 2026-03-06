---
id: 19c__HTF.ANCHOR
name: HTF.ANCHOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ANCHOR

Like the ANCHOR2 function, this function generates the <A> and </A> HTML tags which specify the source or destination of a hypertext link.

## Syntax

```sql
HTF.ANCHOR (
   curl           IN       VARCHAR2,
   ctext          IN       VARCHAR2,
   cname          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the HREF attribute. |
| ctext | VARCHAR2 | IN | The string that goes between the <A> and </A> tags. |
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The difference between these subprograms is that the ANCHOR2 Function provides a target and therefore can be used for a frame. Syntax HTF.ANCHOR ( curl IN VARCHAR2, ctext IN VARCHAR2, cname IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-3 ANCHOR Function Parameters Parameter Description curl The value for the HREF attribute. ctext The string that goes between the <A> and </A> tags. cname The value for the NAME attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <A HREF="curl" NAME="cname" cattributes>ctext</A> Usage Notes This tag accepts several attributes, but either HREF or NAME is required. HREF specifies to where to link. NAME allows this tag to be a target of a hypertext link.