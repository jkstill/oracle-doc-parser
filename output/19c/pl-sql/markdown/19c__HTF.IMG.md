---
id: 19c__HTF.IMG
name: HTF.IMG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.IMG

This function generates the <IMG> tag which directs the browser to load an image onto the HTML page.

## Syntax

```sql
HTF.IMG(
   curl           IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   calt           IN       VARCHAR2   DEFAULT NULL,
   cismap         IN       VARCHAR2   DEFAULT NULL,
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
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The IMG2 Function performs the same operation but additionally uses the cusemap parameter. Syntax HTF.IMG( curl IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, calt IN VARCHAR2 DEFAULT NULL, cismap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-50 IMG Function Parameters Parameter Description curl The value for the SRC attribute. calign The value for the ALIGN attribute. calt The value for the ALT attribute which specifies alternative text to display if the browser does not support images. cismap If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. cattributes The other attributes to be included as-is in the tag. Examples This function generates <IMG SRC="curl" ALIGN="calign" ALT="calt" ISMAP cattributes>