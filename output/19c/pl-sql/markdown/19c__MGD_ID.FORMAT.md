---
id: 19c__MGD_ID.FORMAT
name: MGD_ID.FORMAT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: MGD_ID
tags: [mgd_id]
source_file: MGD_ID-Package-Types.html
---

# MGD_ID.FORMAT

This function returns the string representation of the MGD_ID object in the specified format.

## Syntax

```sql
FORMAT (parameter_list  IN VARCHAR2,
        output_format   IN VARCHAR2)
 RETURN VARCHAR2 DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter_list | VARCHAR2 | IN | List of additional parameters required to create the object in the representation. The list is expressed as a parameter string containing key-value pairs, separated by the semicolon (;) as a delimiter between key-value pairs. For example, for a GTIN code, the parameter string would look as follows: filter=3;companyprefixlength=7;taglength=96 |
| output_format | VARCHAR2) | IN | One of the supported output formats into which an MGD_ID component is formatted: BINARY LEGACY TAG_ENCODING PURE_IDENTITY ONS_HOSTNAME |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax FORMAT (parameter_list IN VARCHAR2, output_format IN VARCHAR2) RETURN VARCHAR2 DETERMINISTIC; Parameters Table 289-7 FORMAT Function Parameters Parameter Description parameter_list List of additional parameters required to create the object in the representation. The list is expressed as a parameter string containing key-value pairs, separated by the semicolon (;) as a delimiter between key-value pairs. For example, for a GTIN code, the parameter string would look as follows: filter=3;companyprefixlength=7;taglength=96 output_format One of the supported output formats into which an MGD_ID component is formatted: BINARY LEGACY TAG_ENCODING PURE_IDENTITY ONS_HOSTNAME Examples See the example for the GET_COMPONENT Function .