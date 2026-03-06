---
id: 19c__HTF.FORMIMAGE
name: HTF.FORMIMAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMIMAGE

This function generates the <INPUT> tag with TYPE="image" which creates an image field that the user clicks to submit the form immediately.

## Syntax

```sql
HTF.FORMIMAGE(
   cname          IN       VARCHAR2,
   csrc           IN       VARCHAR2,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute that specifies the image file. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The coordinates of the selected point are measured in pixels, and returned (along with other contents of the form) in two name/value pairs. The x coordinate is submitted under the name of the field with .x appended, and the y coordinate with .y appended. Any VALUE attribute is ignored. Syntax HTF.FORMIMAGE( cname IN VARCHAR2, csrc IN VARCHAR2, calign IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-33 FORMIMAGE Function Parameters Parameter Description cname The value for the NAME attribute. csrc The value for the SRC attribute that specifies the image file. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="image" NAME="cname" SRC="csrc" ALIGN="calign" cattributes>