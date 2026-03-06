---
id: 19c__HTP.IMG
name: HTP.IMG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.IMG

This procedure generates the <IMG> tag which directs the browser to load an image onto the HTML page.

## Syntax

```sql
HTP.IMG(
   curl           IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   calt           IN       VARCHAR2   DEFAULT NULL,
   cismap         IN       VARCHAR2  DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The value for the SRC attribute. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| calt | VARCHAR2 | IN | The value for the ALT attribute which specifies alternative text to display if the browser does not support images. |
| cismap | VARCHAR2 | IN | If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

The IMG2 Procedure performs the same operation but additionally uses the cusemap parameter. Syntax HTP.IMG( curl IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, calt IN VARCHAR2 DEFAULT NULL, cismap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-48 IMG Procedure Parameters Parameter Description curl The value for the SRC attribute. calign The value for the ALIGN attribute. calt The value for the ALT attribute which specifies alternative text to display if the browser does not support images. cismap If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <IMG SRC=" curl " ALIGN=" calign " ALT=" calt " ISMAP cattributes >