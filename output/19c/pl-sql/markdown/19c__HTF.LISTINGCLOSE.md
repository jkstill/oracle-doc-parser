---
id: 19c__HTF.LISTINGCLOSE
name: HTF.LISTINGCLOSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LISTINGCLOSE

This function generates the </LISTING> tags which marks the end of a section of fixed-width text in the body of an HTML page.

## Syntax

```sql
HTF.LISTINGCLOSE
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the beginning of a section of fixed-width text in the body of an HTML page, use the LISTINGOPEN Function . Syntax HTF.LISTINGCLOSE RETURN VARCHAR2; Examples This function generates </LISTING>