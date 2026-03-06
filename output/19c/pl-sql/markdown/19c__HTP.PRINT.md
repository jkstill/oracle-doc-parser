---
id: 19c__HTP.PRINT
name: HTP.PRINT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP.PRINT

These procedures generate the specified parameter as a string terminated with the \n newline character.

## Syntax

```sql
HTP.PRINT (
   cbuf      IN       VARCHAR2);

HTP.PRINT (
   dbuf      IN       DATE);

HTP.PRINT (
   nbuf      IN       NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbuf | VARCHAR2) | IN | The string to generate terminated by a newline. |
| dbuf | DATE) | IN | The string to generate terminated by a newline. |
| nbuf | NUMBER) | IN | The string to generate terminated by a newline. |

## Usage Notes

The PRN Procedures performs the same operation but does not terminate with a newline character. Syntax HTP.PRINT ( cbuf IN VARCHAR2); HTP.PRINT ( dbuf IN DATE); HTP.PRINT ( nbuf IN NUMBER); Parameters Table 221-69 PRINT Procedure Parameters Parameter Description cbuf The string to generate terminated by a newline. dbuf The string to generate terminated by a newline. nbuf The string to generate terminated by a newline. Usage Notes The \n character is not the same as <BR> . The \n character formats the HTML source but it does not affect how the browser renders the HTML source. Use <BR> to control how the browser renders the HTML source. These procedures do not have function equivalents.