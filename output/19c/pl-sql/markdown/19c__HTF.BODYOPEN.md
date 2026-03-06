---
id: 19c__HTF.BODYOPEN
name: HTF.BODYOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.BODYOPEN

This function generates the <BODY> tag which marks the beginning of the body section of an HTML document.

## Syntax

```sql
HTF.BODYOPEN (
   cbackground    IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbackground | VARCHAR2 | IN | The value for the BACKGROUND attribute which specifies a graphic file to use for the background of the document. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

You mark the end of a body section by means of the BODYCLOSE Function . Syntax HTF.BODYOPEN ( cbackground IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-12 BODYOPEN Function Parameters Parameter Description cbackground The value for the BACKGROUND attribute which specifies a graphic file to use for the background of the document. cattributes The other attributes to be included as-is in the tag. Examples This function generates <BODY background="cbackground" cattributes> so that HTF.BODYOPEN('/img/background.gif') RETURN VARCHAR2; generates: <BODY background="/img/background.gif">