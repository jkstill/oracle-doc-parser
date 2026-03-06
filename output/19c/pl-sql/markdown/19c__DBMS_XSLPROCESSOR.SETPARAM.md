---
id: 19c__DBMS_XSLPROCESSOR.SETPARAM
name: DBMS_XSLPROCESSOR.SETPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.SETPARAM

This procedure sets a top level parameter in the stylesheet.

## Syntax

```sql
DBMS_XSLPROCESSOR.SETPARAM(
   ss      IN   Stylesheet,
   name    IN   VARCHAR2,
   value   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ss | Stylesheet | IN | Stylesheet instance |
| name | VARCHAR2 | IN | Name of the parameter |
| value | VARCHAR2) | IN | Value of the parameter |

## Usage Notes

The parameter value must be a valid XPath expression. Literal string values must be quoted. Syntax DBMS_XSLPROCESSOR.SETPARAM( ss IN Stylesheet, name IN VARCHAR2, value IN VARCHAR2); Parameters Table 216-13 SETPARAM Procedure Parameters Parameter Description ss Stylesheet instance name Name of the parameter value Value of the parameter