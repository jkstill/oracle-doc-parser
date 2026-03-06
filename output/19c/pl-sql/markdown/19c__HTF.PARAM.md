---
id: 19c__HTF.PARAM
name: HTF.PARAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PARAM

This function generates the <PARAM> tag which specifies parameter values for Java applets.

## Syntax

```sql
HTF.PARAM(
   cname          IN       VARCHAR2
   cvalue         IN       VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2) | IN | The value for the VALUE attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

The values can reference HTML variables. To invoke a Java applet from a Web page, use APPLETOPEN Function to begin the invocation. Use one PARAM Function for each desired name-value pair, and use APPLETCLOSE Function to end the applet invocation. Syntax HTF.PARAM( cname IN VARCHAR2 cvalue IN VARCHAR2) RETURN VARCHAR2; Parameters Table 220-68 PARAM Function Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. Examples This function generates <PARAM NAME=cname VALUE="cvalue">