---
id: 19c__HTF.IMG2
name: HTF.IMG2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.IMG2

This function generates the <IMG> tag, which directs the browser to load an image onto the HTML page.

## Syntax

```sql
HTF.IMG2(
   curl           IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   calt           IN       VARCHAR2   DEFAULT NULL,
   cismap         IN       VARCHAR2   DEFAULT NULL,
   cusemap        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the SRC attribute. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| calt | VARCHAR2 | IN | The value for the ALT attribute which specifies alternative text to display if the browser does not support images. |
| cismap | VARCHAR2 | IN | If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. |
| cusemap | VARCHAR2 | IN | The value for the USEMAP attribute which specifies a client-side image map. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The IMG Function performs the same operation but does not use the cusemap parameter. Syntax HTF.IMG2( curl IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, calt IN VARCHAR2 DEFAULT NULL, cismap IN VARCHAR2 DEFAULT NULL, cusemap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-51 IMG2 Function Parameters Parameter Description curl The value for the SRC attribute. calign The value for the ALIGN attribute. calt The value for the ALT attribute which specifies alternative text to display if the browser does not support images. cismap If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. cusemap The value for the USEMAP attribute which specifies a client-side image map. cattributes The other attributes to be included as-is in the tag. Examples This function generates <IMG SRC="curl" ALIGN="calign" ALT="calt" ISMAP USEMAP="cusemap" cattributes>