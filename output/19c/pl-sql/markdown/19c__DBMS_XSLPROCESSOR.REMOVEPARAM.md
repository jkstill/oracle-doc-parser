---
id: 19c__DBMS_XSLPROCESSOR.REMOVEPARAM
name: DBMS_XSLPROCESSOR.REMOVEPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.REMOVEPARAM

This procedure removes a top level stylesheet parameter.

## Syntax

```sql
DBMS_XSLPROCESSOR.REMOVEPARAM(
   ss     IN  Stylesheet,
   name   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ss | Stylesheet | IN | Stylesheet instance |
| name | VARCHAR2) | IN | Name of the parameter |

## Usage Notes

Syntax DBMS_XSLPROCESSOR.REMOVEPARAM( ss IN Stylesheet, name IN VARCHAR2); Parameters Table 216-8 REMOVEPARAM Procedure Parameters Parameter Description ss Stylesheet instance name Name of the parameter