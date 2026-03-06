---
id: 19c__HTF.ESCAPE_URL
name: HTF.ESCAPE_URL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF.ESCAPE_URL

This deprecated function replaces characters that have special meaning in HTML and HTTP with their escape sequences.

## Syntax

```sql
HTF.ESCAPE_URL(
     p_url          IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_url | VARCHAR2) | IN | The string to convert. |

**Returns:** `UNKNOWN`

## Usage Notes

Note: This procedure, deprecated in Release 10 g , and provided here only for reasons of backward compatibility, does not comply with the Internet Engineering Task Force (IETF) Request for Comments (RFC) standards of URL encoding. If you need to encode URLs, it is recommended you use the ESCAPE Function in the UTL_URL package. The following characters are converted: & to &amp; " to &quot: < to &lt; > to &gt; % to &25 Note: This procedure, deprecated in Release 10 g , and provided here only for reasons of backward compatibility, does not comply with the Internet Engineering Task Force (IETF) Request for Comments (RFC) standards of URL encoding. If you need to encode URLs, it is recommended you use the ESCAPE Function in the UTL_URL package. Syntax HTF.ESCAPE_URL( p_url IN VARCHAR2); Parameters Table 220-27 ESCAPE_URL Function Parameters Parameter Description p_url The string to convert.