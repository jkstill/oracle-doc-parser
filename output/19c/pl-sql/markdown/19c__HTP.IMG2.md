---
id: 19c__HTP.IMG2
name: HTP.IMG2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.IMG2

This procedure generates the <IMG> tag, which directs the browser to load an image onto the HTML page.

## Syntax

```sql
HTP.IMG2(
   curl           IN       VARCHAR2   DEFAULT NULL,
   calign         IN       VARCHAR2   DEFAULT NULL,
   calt           IN       VARCHAR2   DEFAULT NULL,
   cismap         IN       VARCHAR2  DEFAULT NULL,
   cusemap        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
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

## Usage Notes

The IMG Procedure performs the same operation but does not use the cusemap parameter. Syntax HTP.IMG2( curl IN VARCHAR2 DEFAULT NULL, calign IN VARCHAR2 DEFAULT NULL, calt IN VARCHAR2 DEFAULT NULL, cismap IN VARCHAR2 DEFAULT NULL, cusemap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-49 IMG2 Procedure Parameters Parameter Description curl The value for the SRC attribute. calign The value for the ALIGN attribute. calt The value for the ALT attribute which specifies alternative text to display if the browser does not support images. cismap If the value for this parameter is not NULL , the ISMAP attribute is added to the tag. The attribute indicates that the image is an imagemap. cusemap The value for the USEMAP attribute which specifies a client-side image map. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <IMG SRC=" curl " ALIGN=" calign " ALT=" calt " ISMAP USEMAP=" cusemap " cattributes >