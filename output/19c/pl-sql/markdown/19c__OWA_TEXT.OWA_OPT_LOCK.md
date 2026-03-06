---
id: 19c__OWA_TEXT.OWA_OPT_LOCK
name: OWA_TEXT.OWA_OPT_LOCK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_TEXT
tags: [owa_text]
source_file: OWA_TEXT.html
---

# OWA_TEXT.OWA_OPT_LOCK

There are three OWA_OPT_LOCK lock types.

## Syntax

```sql
TYPE multi_line IS RECORD (
   rows           vc_arr,
   num_rows       INTEGER,
   partial_row    BOOLEAN);
```

## Usage Notes

MULTI_LINE DATA TYPE ROW_LIST DATA TYPE VC_ARR DATA TYPE TYPE multi_line IS RECORD ( rows vc_arr, num_rows INTEGER, partial_row BOOLEAN); TYPE row_list IS RECORD ( rows int_arr, num_rows INTEGER); int_arr IS DEFINED AS: TYPE int_arr IS TABLE OF INTEGER INDEX BY BINARY_INTEGER; TYPE vc_arr IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;