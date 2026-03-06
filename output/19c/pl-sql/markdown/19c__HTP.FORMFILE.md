---
id: 19c__HTP.FORMFILE
name: HTP.FORMFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMFILE

This procedure generates the <INPUT> tag with TYPE="file" which inserts a file form element. This is used for file uploading for a given page.

## Syntax

```sql
HTP.FORMFILE(
   cname          IN       VARCHAR2,
   caccept        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| caccept | VARCHAR2 | IN | A comma-delimited list of MIME types for upload. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.FORMFILE( cname IN VARCHAR2, caccept IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-30 FORMFILE Procedure Parameters Parameter Description cname The value for the NAME attribute. caccept A comma-delimited list of MIME types for upload. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <INPUT TYPE="file" NAME=" cname " ACCEPT=" caccept " cattributes >