---
id: 19c__HTF.ISINDEX
name: HTF.ISINDEX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ISINDEX

This function creates a single entry field with a prompting text, such as " enter value, " then sends that value to the URL of the page or program.

## Syntax

```sql
HTF.ISINDEX(
   cprompt        IN       VARCHAR2    DEFAULT NULL,
   curl           IN       VARCHAR2    DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cprompt | VARCHAR2 | IN | The value for the PROMPT attribute. |
| curl | VARCHAR2 | IN | The value for the HREF attribute. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax HTF.ISINDEX( cprompt IN VARCHAR2 DEFAULT NULL, curl IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 220-52 ISINDEX Function Parameters Parameter Description cprompt The value for the PROMPT attribute. curl The value for the HREF attribute. Examples This function generates <ISINDEX PROMPT="cprompt" HREF="curl">