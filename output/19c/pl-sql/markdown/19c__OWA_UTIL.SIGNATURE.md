---
id: 19c__OWA_UTIL.SIGNATURE
name: OWA_UTIL.SIGNATURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.SIGNATURE

This procedure generates an HTML line followed by a signature line on the HTML document.

## Syntax

```sql
OWA_UTIL.SIGNATURE;

OWA_UTIL.SIGNATURE (
   cname        IN        VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2) | IN | The function or procedure whose source you want to show. |

## Usage Notes

If a parameter is specified, the procedure also generates a hypertext link to view the PL/SQL source for that procedure. The link calls the SHOWSOURCE Procedure . Syntax OWA_UTIL.SIGNATURE; OWA_UTIL.SIGNATURE ( cname IN VARCHAR2); Parameters Table 230-11 SIGNATURE Procedure Parameters Parameter Description cname The function or procedure whose source you want to show. Examples Without a parameter, the procedure generates a line that looks like the following: This page was produced by the PL/SQL Agent on August 9, 2001 09:30. With a parameter, the procedure generates a signature line in the HTML document that looks like the following: This page was produced by the PL/SQL Agent on 8/09/01 09:30 View PL/SQL Source