---
id: 19c__HTF.LISTINGOPEN
name: HTF.LISTINGOPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.LISTINGOPEN

This function generates the <LISTING> tag which marks the beginning of a section of fixed-width text in the body of an HTML page.

## Syntax

```sql
HTF.LISTINGOPEN
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

To mark the end of a section of fixed-width text in the body of an HTML page, use the LISTINGCLOSE Function . Syntax HTF.LISTINGOPEN RETURN VARCHAR2; Examples This function generates <LISTING>