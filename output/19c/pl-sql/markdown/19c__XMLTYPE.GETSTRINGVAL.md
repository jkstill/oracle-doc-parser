---
id: 19c__XMLTYPE.GETSTRINGVAL
name: XMLTYPE.GETSTRINGVAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.GETSTRINGVAL

This member function returns the document as a string. It returns a string containing the seralized XML representation, or in the case of text nodes, the text itself.

## Syntax

```sql
MEMBER FUNCTION getStringVal()
RETURN varchar2 deterministic;
```

**Returns:** `varchar2`

## Usage Notes

If the XML document exceeds the VARCHAR2 maximum size (4000), then an error is raised at run time. MEMBER FUNCTION getStringVal() RETURN varchar2 deterministic;