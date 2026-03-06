---
id: 19c__HTF.FORMTEXTAREA
name: HTF.FORMTEXTAREA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMTEXTAREA

This function generates the <TEXTAREA> tag, which creates a text field that has no predefined text in the text area. This field enables entering several lines of text.

## Syntax

```sql
HTF.FORMTEXTAREA(
   cname          IN       VARCHAR2,
   nrows          IN       INTEGER,
   ncolumns       IN       INTEGER,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| nrows | INTEGER | IN | The value for the ROWS attribute.This is an integer. |
| ncolumns | INTEGER | IN | The value for the COLS attribute.This is an integer. |
| calign | VARCHAR2 | IN | The value for the ALIGN attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The same operation is performed by the FORMTEXTAREA2 Function which in addition has the cwrap parameter that lets you specify a wrap style. Syntax HTF.FORMTEXTAREA( cname IN VARCHAR2, nrows IN INTEGER, ncolumns IN INTEGER, calign IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-42 FORMTEXTAREA Function Parameters Parameter Description cname The value for the NAME attribute. nrows The value for the ROWS attribute.This is an integer. ncolumns The value for the COLS attribute.This is an integer. calign The value for the ALIGN attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <TEXTAREA NAME="cname" ROWS="nrows" COLS="ncolumns" ALIGN="calign" cattributes></TEXTAREA>