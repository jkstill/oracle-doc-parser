---
id: 19c__OWA_TEXT.PRINT_MULTI
name: OWA_TEXT.PRINT_MULTI
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.PRINT_MULTI

This procedure uses the PRINT Procedures or the PRN Procedures to print the "rows" field of the OWA_TEXT . MULTI_LINE DATA TYPE .

## Syntax

```sql
OWA_TEXT.PRINT_MULTI(
   mline       IN       multi_line);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mline | multi_line) | IN | The multi_line datatype to print. |

## Usage Notes

Syntax OWA_TEXT.PRINT_MULTI( mline IN multi_line); Parameters Table 229-4 PRINT_MULTI Procedure Parameters Parameter Description mline The multi_line datatype to print. Return Values The contents of the multi_line .