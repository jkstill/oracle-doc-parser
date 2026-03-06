---
id: 19c__HTP.PRN
name: HTP.PRN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PRN

These procedures generate the specified parameter as a string.

## Syntax

```sql
HTP.PRN (
   cbuf      IN       VARCHAR2);

HTP.PRN (
   dbuf      IN       DATE);

HTP.PRN (
   nbuf      IN       NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbuf | VARCHAR2) | IN | The string to generate (not terminated by a newline). |
| dbuf | DATE) | IN | The string to generate (not terminated by a newline). |
| nbuf | NUMBER) | IN | The string to generate (not terminated by a newline). |

## Usage Notes

Unlike the PRINT Procedures the string is not terminated with the \n newline character. Syntax HTP.PRN ( cbuf IN VARCHAR2); HTP.PRN ( dbuf IN DATE); HTP.PRN ( nbuf IN NUMBER); Parameters Table 221-71 PRN Procedure Parameters Parameter Description cbuf The string to generate (not terminated by a newline). dbuf The string to generate (not terminated by a newline). nbuf The string to generate (not terminated by a newline). Usage Notes These procedures do not have function equivalents.