---
id: 19c__HTF.FORMFILE
name: HTF.FORMFILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMFILE

This function generates the <INPUT> tag with TYPE="file" which inserts a file form element. This is used for file uploading for a given page.

## Syntax

```sql
HTF.FORMFILE(
   cname          IN       VARCHAR2,
   caccept        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| caccept | VARCHAR2 | IN | A comma-delimited list of MIME types for upload. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.FORMFILE( cname IN VARCHAR2, caccept IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-31 FORMFILE Function Parameters Parameter Description cname The value for the NAME attribute. caccept A comma-delimited list of MIME types for upload. cattributes The other attributes to be included as-is in the tag. Examples This function generates <INPUT TYPE="file" NAME="cname" ACCEPT="caccept" cattributes>