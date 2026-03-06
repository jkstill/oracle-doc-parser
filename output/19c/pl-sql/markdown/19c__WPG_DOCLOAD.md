---
id: 19c__WPG_DOCLOAD
name: WPG_DOCLOAD
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: WPG_DOCLOAD
tags: [wpg_docload]
source_file: WPG_DOCLOAD.html
---

# WPG_DOCLOAD

WPG_DOCLOAD defines several constants to use when specifying parameter values.

## Syntax

```sql
name_col_len CONSTANT pls_integer := 64;
```

## Usage Notes

The WPG_DOCLOAD constants are listed below: NAME_COL_LEN MIMET_COL_LEN MAX_DOCTABLE_NAME_LEN NAME_COL_LEN The NAME column in your document table must be the same as the value of name_col_len . name_col_len CONSTANT pls_integer := 64; MIMET_COL_LEN The MIME_TYPE column in your document table must be the same as the value of mimet_col_len . mimet_col_len CONSTANT pls_integer := 48; MAX_DOCTABLE_NAME_LEN The name length of your document table must be less than max_doctable_name_len . max_doctable_name_len CONSTANT pls_integer := 256;