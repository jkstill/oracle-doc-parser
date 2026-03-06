---
id: 19c__HTF.FORMOPEN
name: HTF.FORMOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.FORMOPEN

This function generates the <FORM> tag which marks the beginning of a form section in an HTML document.

## Syntax

```sql
HTF.FORMOPEN(
   curl           IN       VARCHAR2,
   cmethod        IN       VARCHAR2   DEFAULT 'POST',
   ctarget        IN       VARCHAR2   DEFAULT NULL,
   cenctype       IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The URL of the Web Request Broker or CGI script where the contents of the form is sent. This parameter is required. |
| cmethod | VARCHAR2 | IN | The value for the METHOD attribute. The value can be " GET " or " POST ". |
| ctarget | VARCHAR2 | IN | The value for the TARGET attribute. |
| cenctype | VARCHAR2 | IN | The value for the ENCTYPE attribute. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

**Returns:** `VARCHAR2`

## Usage Notes

You mark the end of the form section by means of the FORMCLOSE Function . Syntax HTF.FORMOPEN( curl IN VARCHAR2, cmethod IN VARCHAR2 DEFAULT 'POST', ctarget IN VARCHAR2 DEFAULT NULL, cenctype IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-34 FORMOPEN Function Parameters Parameter Description curl The URL of the Web Request Broker or CGI script where the contents of the form is sent. This parameter is required. cmethod The value for the METHOD attribute. The value can be " GET " or " POST ". ctarget The value for the TARGET attribute. cenctype The value for the ENCTYPE attribute. cattributes The other attributes to be included as-is in the tag. Examples This function generates <FORM ACTION="curl" METHOD="cmethod" TARGET="ctarget" ENCTYPE="cenctype" cattributes>