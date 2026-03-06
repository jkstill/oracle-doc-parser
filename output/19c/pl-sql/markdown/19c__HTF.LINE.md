---
id: 19c__HTF.LINE
name: HTF.LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LINE

This function generates the <HR> tag, which generates a line in the HTML document.

## Syntax

```sql
HTF.LINE(
   cclear         IN       VARCHAR2   DEFAULT NULL,
   csrc           IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cclear | VARCHAR2 | IN | The value for the CLEAR attribute. |
| csrc | VARCHAR2 | IN | The value for the SRC attribute which specifies a custom image as the source of the line. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

This subprogram performs the same operation as the HR Function . Syntax HTF.LINE( cclear IN VARCHAR2 DEFAULT NULL, csrc IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-56 LINE Function Parameters Parameter Description cclear The value for the CLEAR attribute. csrc The value for the SRC attribute which specifies a custom image as the source of the line. cattributes The other attributes to be included as-is in the tag. Examples This function generates <HR CLEAR="cclear" SRC="csrc" cattributes>