---
id: 19c__HTP.PARAM
name: HTP.PARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PARAM

This procedure generates the <PARAM> tag which specifies parameter values for Java applets.

## Syntax

```sql
HTP.PARAM(
   cname          IN       VARCHAR2
   cvalue         IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2 | IN | The value for the NAME attribute. |
| cvalue | VARCHAR2) | IN | The value for the VALUE attribute. |

## Usage Notes

The values can reference HTML variables. To invoke a Java applet from a Web page, use APPLETOPEN Procedure to begin the invocation. Use one PARAM Procedure for each desired name-value pair, and use APPLETCLOSE Procedure to end the applet invocation. Syntax HTP.PARAM( cname IN VARCHAR2 cvalue IN VARCHAR2); Parameters Table 221-66 PARAM Procedure Parameters Parameter Description cname The value for the NAME attribute. cvalue The value for the VALUE attribute. Examples This procedure generates <PARAM NAME= cname VALUE=" cvalue" >