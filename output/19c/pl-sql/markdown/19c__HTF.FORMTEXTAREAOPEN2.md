---
id: 19c__HTF.FORMTEXTAREAOPEN2
name: HTF.FORMTEXTAREAOPEN2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMTEXTAREAOPEN2

This function generates the <TEXTAREA> which marks the beginning of a text area form element.

## Syntax

```sql
HTF.FORMTEXTAREAOPEN2(
   cname          IN       VARCHAR2,
   nrows          IN       INTEGER,
   ncolumns       IN       INTEGER,
   calign         IN       VARCHAR2   DEFAULT NULL,
   cwrap          IN       VARCHAR2   DEFAULT NULL,
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
| cwrap | VARCHAR2 | IN | The value for the WRAP attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

The same operation is performed by the FORMTEXTAREAOPEN Function except that in that case you cannot specify a wrap style. You mark the end of a text area form element by means of the FORMTEXTAREACLOSE Function . Syntax HTF.FORMTEXTAREAOPEN2( cname IN VARCHAR2, nrows IN INTEGER, ncolumns IN INTEGER, calign IN VARCHAR2 DEFAULT NULL, cwrap IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-45 FORMTEXTAREAOPEN2 Function Parameters Parameter Description cname The value for the NAME attribute. nrows The value for the ROWS attribute.This is an integer. ncolumns The value for the COLS attribute.This is an integer. calign The value for the ALIGN attribute. cwrap The value for the WRAP attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <TEXTAREA NAME="cname" ROWS="nrows" COLS="ncolumns" ALIGN="calign" WRAP = "cwrap" cattributes>