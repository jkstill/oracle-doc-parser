---
id: 19c__OWA_TEXT.NEW_ROW_LIST
name: OWA_TEXT.NEW_ROW_LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.NEW_ROW_LIST

This function or procedure creates a new OWA_TEX.ROW_LIST DATA TYPE .

## Syntax

```sql
OWA_TEXT.NEW_ROW_LIST 
  RETURN ROW_LIST;

OWA_TEXT.NEW_ROW_LIST(
  rlist    OUT     row_list);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rlist | row_list) | OUT | This is an output parameter containing the new row_list datatype |

**Returns:** `ROW_LIST`

## Usage Notes

The function version uses no parameters and returns a new empty row_list . The procedure version creates the row_list datatype as an output parameter. Syntax OWA_TEXT.NEW_ROW_LIST RETURN ROW_LIST; OWA_TEXT.NEW_ROW_LIST( rlist OUT row_list); Parameters Table 229-3 NEW_ROW_LIST Procedure Parameters Parameter Description rlist This is an output parameter containing the new row_list datatype Return Values The function version returns the new row_list datatype.