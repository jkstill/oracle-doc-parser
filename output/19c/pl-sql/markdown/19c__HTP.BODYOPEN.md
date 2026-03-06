---
id: 19c__HTP.BODYOPEN
name: HTP.BODYOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BODYOPEN

This procedure generates the <BODY> tag which marks the beginning of the body section of an HTML document.

## Syntax

```sql
HTP.BODYOPEN (
   cbackground    IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbackground | VARCHAR2 | IN | The value for the BACKGROUND attribute which specifies a graphic file to use for the background of the document. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You mark the end of a body section by means of the BODYCLOSE Procedure . Syntax HTP.BODYOPEN ( cbackground IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-12 BODYOPEN Procedure Parameters Parameter Description cbackground The value for the BACKGROUND attribute which specifies a graphic file to use for the background of the document. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BODY background=" cbackground" cattributes> so that HTP.BODYOPEN('/img/background.gif'); generates: <BODY background="/img/background.gif">