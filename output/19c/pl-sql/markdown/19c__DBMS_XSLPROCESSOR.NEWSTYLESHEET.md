---
id: 19c__DBMS_XSLPROCESSOR.NEWSTYLESHEET
name: DBMS_XSLPROCESSOR.NEWSTYLESHEET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.NEWSTYLESHEET

This function creates and returns a new Stylesheet instance.

## Syntax

```sql
DBMS_XSLPROCESSOR.NEWSTYLESHEET(
   xmldoc  IN   DOMDOCUMENT,
   ref     IN   VARCHAR2) 
 RETURN Stylesheet;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmldoc | DOMDOCUMENT | IN | DOMDocument to use for construction |
| inp |  |  | Input URL to use for construction |
| ref | VARCHAR2) | IN | Reference URL |

**Returns:** `Stylesheet`

## Usage Notes

The options are described in the following table. Syntax Creates and returns a new stylesheet instance using the given DOMDOCUMENT and reference URLs: DBMS_XSLPROCESSOR.NEWSTYLESHEET( xmldoc IN DOMDOCUMENT, ref IN VARCHAR2) RETURN Stylesheet; Creates and returns a new Stylesheet instance using the given input and reference URLs: DBMS_XSLPROCESSOR.NEWSTYLESHEET( inp IN VARCHAR2, ref IN VARCHAR2) RETURN Stylesheet; Parameters Table 216-5 NEWSTYLESHEET Function Parameters Parameter Description xmldoc DOMDocument to use for construction inp Input URL to use for construction ref Reference URL