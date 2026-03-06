---
id: 19c__HTP.FORMOPEN
name: HTP.FORMOPEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.FORMOPEN

This procedure generates the <FORM> tag which marks the beginning of a form section in an HTML document.

## Syntax

```sql
HTP.FORMOPEN(
   curl           IN       VARCHAR2,
   cmethod        IN       VARCHAR2   DEFAULT 'POST',
   ctarget        IN       VARCHAR2   DEFAULT NULL,
   cenctype       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The URL of the WRB or CGI script where the contents of the form is sent. This parameter is required. |
| cmethod | VARCHAR2 | IN | The value for the METHOD attribute. The value can be " GET " or " POST ". |
| ctarget | VARCHAR2 | IN | The value for the TARGET attribute. |
| cenctype | VARCHAR2 | IN | The value for the ENCTYPE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

You mark the end of the form section by means of the FORMCLOSE Procedure . Syntax HTP.FORMOPEN( curl IN VARCHAR2, cmethod IN VARCHAR2 DEFAULT 'POST', ctarget IN VARCHAR2 DEFAULT NULL, cenctype IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-29 FORMOPEN Procedure Parameters Parameter Description curl The URL of the WRB or CGI script where the contents of the form is sent. This parameter is required. cmethod The value for the METHOD attribute. The value can be " GET " or " POST ". ctarget The value for the TARGET attribute. cenctype The value for the ENCTYPE attribute. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <FORM ACTION=" curl " METHOD=" cmethod " TARGET=" ctarget " ENCTYPE=" cenctype " cattributes>