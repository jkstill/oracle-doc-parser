---
id: 19c__UTL_URL.UNESCAPE
name: UTL_URL.UNESCAPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_URL
tags: [utl_url]
source_file: UTL_URL.html
---

# UTL_URL.UNESCAPE

This function unescapes the escape character sequences to its original form in a URL, to convert the %XX escape character sequences to the original characters.

## Syntax

```sql
UTL_URL.UNESCAPE (
   url            IN VARCHAR2 CHARACTER SET ANY_CS,
   url_charset    IN VARCHAR2 DEFAULT utl_http.body_charset)
                  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url | VARCHAR2 | IN | The URL to unescape |
| url_charset | VARCHAR2 | IN | After a character is unescaped, the character is assumed to be in the source_charset character set and it will be converted from the source_charset to the database character set before the URL is returned. If source_charset is NULL , the database charset is assumed and no character set conversion occurred. The default value is the current default body character set of the UTL_HTTP package, whose default value is "ISO-8859-1". The character set can be named in Internet Assigned Numbers Authority (IANA) or Oracle naming convention. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_URL.UNESCAPE ( url IN VARCHAR2 CHARACTER SET ANY_CS, url_charset IN VARCHAR2 DEFAULT utl_http.body_charset) RETURN VARCHAR2; Parameters Table 278-4 UNESCAPE Function Parameters Parameter Description url The URL to unescape url_charset After a character is unescaped, the character is assumed to be in the source_charset character set and it will be converted from the source_charset to the database character set before the URL is returned. If source_charset is NULL , the database charset is assumed and no character set conversion occurred. The default value is the current default body character set of the UTL_HTTP package, whose default value is "ISO-8859-1". The character set can be named in Internet Assigned Numbers Authority (IANA) or Oracle naming convention. Usage Notes The Web server that you receive the URL from may use a character set that is different from that of your database. In that case, specify the url_charset as the Web server character set so that the characters that need to be unescaped are unescaped in the source character set. For example, a user of an EBCDIC database who receives a URL from an ASCII Web server should unescape the URL using US7ASCII so that %20 is unescaped as a space (0x20 is the hex code of a space in ASCII) instead of a ? (because 0x20 is not a valid character in EBCDIC). This function does not validate a URL for the proper URL format.