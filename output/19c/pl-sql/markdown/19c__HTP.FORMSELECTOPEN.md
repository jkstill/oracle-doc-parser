---
id: 19c__HTP.FORMSELECTOPEN
name: HTP.FORMSELECTOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMSELECTOPEN

This procedure generates the <SELECT> tags which creates a Select form element.

## Syntax

```sql
FORMSELECTOPEN(
   cname          IN       VARCHAR2,
   cprompt        IN       VARCHAR2   DEFAULT NULL,
   nsize          IN       INTEGER    DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cprompt | VARCHAR2 | IN | The string preceding the list box. |
| nsize | INTEGER | IN | The value for the SIZE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

A Select form element is a listbox where the user selects one or more values. You mark the end of Select form element by means of the FORMSELECTCLOSE Procedure .The values are inserted using FORMSELECTOPTION Procedure . Syntax FORMSELECTOPEN( cname IN VARCHAR2, cprompt IN VARCHAR2 DEFAULT NULL, nsize IN INTEGER DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-36 FORMSELECTOPEN Procedure Parameters Parameter Description cname The value for the NAME attribute. cprompt The string preceding the list box. nsize The value for the SIZE attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates cprompt <SELECT NAME=" cname" SIZE= "nsize " cattributes > </SELECT> so that HTP.FORMSELECTOPEN('greatest_player'; 'Pick the greatest player:'); HTP.FORMSELECTOPTION('Messier'); HTP.FORMSELECTOPTION('Howe'); HTP.FORMSELECTOPTION('Gretzky');. HTP.FORMSELECTCLOSE; generates Pick the greatest player: <SELECT NAME="greatest_player"> <OPTION>Messier <OPTION>Howe <OPTION>Gretzky </SELECT>