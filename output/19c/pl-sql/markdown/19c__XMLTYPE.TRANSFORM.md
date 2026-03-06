---
id: 19c__XMLTYPE.TRANSFORM
name: XMLTYPE.TRANSFORM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: XMLTYPE
tags: [xmltype]
source_file: XMLTYPE.html
---

# XMLTYPE.TRANSFORM

This member function transforms the XML data using the XSL stylesheet argument and the top-level parameters passed as a string of name=value pairs

## Syntax

```sql
MEMBER FUNCTION transform(
xsl IN XMLType,
parammap in varchar2 := NULL)
RETURN XMLType deterministic;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xsl | XMLType | IN | (IN) |
| parammap | varchar2 | in | (IN) |

**Returns:** `XMLType`

## Usage Notes

If any of the arguments other than the parammap is NULL , then a NULL is returned. MEMBER FUNCTION transform( xsl IN XMLType, parammap in varchar2 := NULL) RETURN XMLType deterministic;