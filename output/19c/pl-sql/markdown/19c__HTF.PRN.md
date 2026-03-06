---
id: 19c__HTF.PRN
name: HTF.PRN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PRN

These functions generate the specified parameter as a string.

## Syntax

```sql
HTF.PRN (
   cbuf      IN       VARCHAR2)
  RETURN VARCHAR2;

HTF.PRN (
   dbuf      IN       DATE)
  RETURN VARCHAR2;

HTF.PRN (
   nbuf      IN       NUMBER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbuf | VARCHAR2) | IN | The string to generate (not terminated by a newline). |
| dbuf | DATE) | IN | The string to generate (not terminated by a newline). |
| nbuf | NUMBER) | IN | The string to generate (not terminated by a newline). |

**Returns:** `VARCHAR2`

## Usage Notes

Unlike the PRINT Functions the string is not terminated with the \n newline character. Syntax HTF.PRN ( cbuf IN VARCHAR2) RETURN VARCHAR2; HTF.PRN ( dbuf IN DATE) RETURN VARCHAR2; HTF.PRN ( nbuf IN NUMBER) RETURN VARCHAR2; Parameters Table 220-72 PRN Function Parameters Parameter Description cbuf The string to generate (not terminated by a newline). dbuf The string to generate (not terminated by a newline). nbuf The string to generate (not terminated by a newline). Usage Notes These functions do not have function equivalents.