---
id: 19c__OWA_TEXT.STREAM2MULTI
name: OWA_TEXT.STREAM2MULTI
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.STREAM2MULTI

This procedure converts a string to a multi_line datatype.

## Syntax

```sql
OWA_TEXT.STREAM2MULTI(
   stream         IN       VARCHAR2
   mline          OUT      multi_line);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stream | VARCHAR2 | IN | The string to convert. |
| mline | multi_line) | OUT | The stream in OWA_TEXT.MULTI_LINE DATA TYPE format |

## Usage Notes

Syntax OWA_TEXT.STREAM2MULTI( stream IN VARCHAR2 mline OUT multi_line); Parameters Table 229-6 STREAM2MULTI Procedure Parameters Parameter Description stream The string to convert. mline The stream in OWA_TEXT.MULTI_LINE DATA TYPE format