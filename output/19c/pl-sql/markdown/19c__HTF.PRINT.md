---
id: 19c__HTF.PRINT
name: HTF.PRINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.PRINT

These functions generate the specified parameter as a string terminated with the \n newline character.

## Syntax

```sql
HTF.PRINT (
   cbuf      IN       VARCHAR2)
  RETURN VARCHAR2;

HTF.PRINT (
   dbuf      IN       DATE)
  RETURN VARCHAR2;

HTF.PRINT (
   nbuf      IN       NUMBER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cbuf | VARCHAR2) | IN | The string to generate terminated by a newline. |
| dbuf | DATE) | IN | The string to generate terminated by a newline. |
| nbuf | NUMBER) | IN | The string to generate terminated by a newline. |

**Returns:** `VARCHAR2`

## Usage Notes

The PRN Functions performs the same operation but does not terminate with a newline character. Syntax HTF.PRINT ( cbuf IN VARCHAR2) RETURN VARCHAR2; HTF.PRINT ( dbuf IN DATE) RETURN VARCHAR2; HTF.PRINT ( nbuf IN NUMBER) RETURN VARCHAR2; Parameters Table 220-71 PRINT Function Parameters Parameter Description cbuf The string to generate terminated by a newline. dbuf The string to generate terminated by a newline. nbuf The string to generate terminated by a newline. Usage Notes The \n character is not the same as <BR> . The \n character formats the HTML source but it does not affect how the browser renders the HTML source. Use <BR> to control how the browser renders the HTML source. These functions do not have function equivalents.