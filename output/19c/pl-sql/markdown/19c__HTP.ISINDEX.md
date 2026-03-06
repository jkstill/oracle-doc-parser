---
id: 19c__HTP.ISINDEX
name: HTP.ISINDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.ISINDEX

This procedure creates a single entry field with a prompting text, such as " enter value, " then sends that value to the URL of the page or program.

## Syntax

```sql
HTP.ISINDEX(
   cprompt        IN       VARCHAR2    DEFAULT NULL,
   curl           IN       VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cprompt | VARCHAR2 | IN | The value for the PROMPT attribute. |
| curl | VARCHAR2 | IN | The value for the HREF attribute. |

## Usage Notes

Syntax HTP.ISINDEX( cprompt IN VARCHAR2 DEFAULT NULL, curl IN VARCHAR2 DEFAULT NULL); Parameters Table 221-50 ISINDEX Procedure Parameters Parameter Description cprompt The value for the PROMPT attribute. curl The value for the HREF attribute. Examples This procedure generates <ISINDEX PROMPT=" cprompt " HREF=" curl ">