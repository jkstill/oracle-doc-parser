---
id: 19c__OWA_TEXT.PRINT_ROW_LIST
name: OWA_TEXT.PRINT_ROW_LIST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.PRINT_ROW_LIST

This procedure uses the PRINT Procedures or the PRN Procedures to print the "rows" field of the OWA_TEXT . ROW_LIST DATA TYPE .

## Syntax

```sql
OWA_TEXT.PRINT_ROW_LIST(
   rlist       IN       multi_line);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rlist | multi_line) | IN | The row_list datatype to print. |

## Usage Notes

Syntax OWA_TEXT.PRINT_ROW_LIST( rlist IN multi_line); Parameters Table 229-5 PRINT_ROW_LIST Procedure Parameters Parameter Description rlist The row_list datatype to print. Return Values The contents of the row_list .