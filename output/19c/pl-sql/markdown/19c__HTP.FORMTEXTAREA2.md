---
id: 19c__HTP.FORMTEXTAREA2
name: HTP.FORMTEXTAREA2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMTEXTAREA2

This procedure generates the <TEXTAREA> tag, which creates a text field that has no predefined text in the text area. This field enables entering several lines of text.

## Syntax

```sql
HTP.FORMTEXTAREA2(
   cname          IN       VARCHAR2,
   nrows          IN       INTEGER,
   ncolumns       IN       INTEGER,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| nrows | INTEGER | IN | The value for the ROWS attribute.This is an integer. |
| ncolumns | INTEGER | IN | The value for the COLS attribute.This is an integer. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

The same operation is performed by the FORMTEXTAREA Procedure except that in that case you cannot specify a wrap style. Syntax HTP.FORMTEXTAREA2( cname IN VARCHAR2, nrows IN INTEGER, ncolumns IN INTEGER, calign IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-41 FORMTEXTAREA2 Procedure Parameters Parameter Description cname The value for the NAME attribute. nrows The value for the ROWS attribute.This is an integer. ncolumns The value for the COLS attribute.This is an integer. calign The value for the ALIGN attribute. cwrap The value for the WRAP attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <TEXTAREA NAME=" cname " ROWS=" nrows" COLS=" ncolumns" ALIGN=" calign " WRAP=" cwrap " cattributes ></TEXTAREA>