---
id: 19c__HTP.BASE
name: HTP.BASE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.BASE

This procedure generates the <BASE> tag which records the URL of the document.

## Syntax

```sql
HTP.BASE (
   ctarget        IN       VARCHAR2   DEFAULT NULL,
   cattributes    IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctarget | VARCHAR2 | IN | The value for the TARGET attribute which establishes a window name to which all links in this document are targeted. |
| cattributes | VARCHAR2 | IN | The other attributes to be included as-is in the tag. |

## Usage Notes

Syntax HTP.BASE ( ctarget IN VARCHAR2 DEFAULT NULL, cattributes IN VARCHAR2 DEFAULT NULL); Parameters Table 221-7 BASE Procedure Parameters Parameter Description ctarget The value for the TARGET attribute which establishes a window name to which all links in this document are targeted. cattributes The other attributes to be included as-is in the tag. Examples This procedure generates <BASE HREF="<current URL>" TARGET=" ctarget " cattributes >