---
id: 19c__HTF.FORMSELECTOPEN
name: HTF.FORMSELECTOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMSELECTOPEN

This function generates the <SELECT> tags which begins a Select form element.

## Syntax

```sql
HTF.FORMSELECTOPEN(
  cname        IN    VARCHAR2,
  cprompt      IN    VARCHAR2   DEFAULT NULL,
  nsize        IN    INTEGER    DEFAULT NULL,
  cattributes  IN    VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cprompt | VARCHAR2 | IN | The string preceding the list box. |
| nsize | INTEGER | IN | The value for the SIZE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

A Select form element is a listbox where the user selects one or more values. You mark the end of Select form element by means of the FORMSELECTCLOSE Function .The values are inserted using FORMSELECTOPTION Function . Syntax HTF.FORMSELECTOPEN( cname IN VARCHAR2, cprompt IN VARCHAR2 DEFAULT NULL, nsize IN INTEGER DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-38 FORMSELECTOPEN Function Parameters Parameter Description cname The value for the NAME attribute. cprompt The string preceding the list box. nsize The value for the SIZE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates cprompt <SELECT NAME="cname" SIZE="nsize" cattributes> </SELECT> so that HTF.FORMSELECTOPEN('greatest_player'; 'Pick the greatest player:'); HTF.FORMSELECTOPTION('Messier'); HTF.FORMSELECTOPTION('Howe'); HTF.FORMSELECTOPTION('Gretzky');. HTF.FORMSELECTCLOSE; generates Pick the greatest player: <SELECT NAME="greatest_player"> <OPTION>Messier <OPTION>Howe <OPTION>Gretzky </SELECT>