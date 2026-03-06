---
id: 19c__DBMS_XMLPARSER.GETVALIDATIONMODE
name: DBMS_XMLPARSER.GETVALIDATIONMODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.GETVALIDATIONMODE

The GETVALIDATIONMODE function retrieves the validation mode: TRUE for validating, FALSE otherwise.

## Syntax

```sql
FUNCTION GETVALIDATIONMODE(
  p Parser)
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser) | IN | (IN) |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax FUNCTION GETVALIDATIONMODE( p Parser) RETURN BOOLEAN; Parameters Table 207-5 GETVALIDATIONMODE Function Parameters Parameter IN / OUT Description p (IN) Parser instance.