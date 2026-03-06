---
id: 19c__UTL_URL.ESCAPE
name: UTL_URL.ESCAPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_URL
tags: [utl_url]
source_file: UTL_URL.html
---

# UTL_URL.ESCAPE

This function returns a URL with illegal characters (and optionally reserved characters) escaped using the %2-digit-hex-code format.

## Syntax

```sql
UTL_URL.ESCAPE (
   url                   IN VARCHAR2 CHARACTER SET ANY_CS,
   escape_reserved_chars IN BOOLEAN  DEFAULT  FALSE,
   url_charset           IN VARCHAR2 DEFAULT  utl_http.body_charset)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url | VARCHAR2 | IN | The original URL |
| escape_reserved_chars | BOOLEAN | IN | Indicates whether the URL reserved characters should be escaped. If set to TRUE , both the reserved and illegal URL characters are escaped. Otherwise, only the illegal URL characters are escaped. The default value is FALSE . |
| url_charset | VARCHAR2 | IN | When escaping a character (single-byte or multibyte), determine the target character set that character should be converted to before the character is escaped in %hex-code format. If url_charset is NULL , the database charset is assumed and no character set conversion will occur. The default value is the current default body character set of the UTL_HTTP package, whose default value is ISO-8859-1 . The character set can be named in Internet Assigned Numbers Authority (IANA) or in the Oracle naming convention. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_URL.ESCAPE ( url IN VARCHAR2 CHARACTER SET ANY_CS, escape_reserved_chars IN BOOLEAN DEFAULT FALSE, url_charset IN VARCHAR2 DEFAULT utl_http.body_charset) RETURN VARCHAR2; Parameters Table 278-3 ESCAPE Function Parameters Parameter Description url The original URL escape_reserved_chars Indicates whether the URL reserved characters should be escaped. If set to TRUE , both the reserved and illegal URL characters are escaped. Otherwise, only the illegal URL characters are escaped. The default value is FALSE . url_charset When escaping a character (single-byte or multibyte), determine the target character set that character should be converted to before the character is escaped in %hex-code format. If url_charset is NULL , the database charset is assumed and no character set conversion will occur. The default value is the current default body character set of the UTL_HTTP package, whose default value is ISO-8859-1 . The character set can be named in Internet Assigned Numbers Authority (IANA) or in the Oracle naming convention. Usage Notes Use this function to escape URLs that contain illegal characters as defined in the URL specification RFC 2396. The legal characters in URLs are: A through Z, a through z, and 0 through 9 Hyphen ( - ), underscore ( _ ), period ( . ), exclamation point ( ! ), tilde ( ~ ), asterisk ( * ), accent ( ' ), left parenthesis ( ( ), right parenthesis ( ) ) The reserved characters consist of: Semi-colon ( ; ) slash ( / ), question mark ( ? ), colon ( : ), at sign ( @ ), ampersand ( & ), equals sign ( = ), plus sign ( + ), dollar sign ( $ ), and comma ( , ) Many of the reserved characters are used as delimiters in the URL. You should escape characters beyond those listed here by using escape_url. Also, to use the reserved characters in the name-value pairs of the query string of a URL, those characters must be escaped separately. An escape_url cannot recognize the need to escape those characters because once inside a URL, those characters become indistinguishable from the actual delimiters. For example, to pass a name-value pair $logon=HR/ <password> into the query string of a URL, escape the $ and / separately as %24logon=HR%2F <password> and use it in the URL. Normally, you will escape the entire URL, which contains the reserved characters (delimiters) that should not be escaped. For example: utl_url.escape('http://www.acme.com/a url with space.html') Returns: http://www.acme.com/a%20url%20with%20space.html In other situations, you may want to send a query string with a value that contains reserved characters. In that case, escape only the value fully (with escape_reserved_chars set to TRUE ) and then concatenate it with the rest of the URL. For example: url := 'http://www.acme.com/search?check=' || utl_url.escape ('Is the use of the "$" sign okay?', TRUE); This expression escapes the question mark ( ? ), dollar sign ( $ ), and space characters in ' Is the use of the "$" sign okay?' but not the ? after search in the URL that denotes the use of a query string. The Web server that you intend to fetch Web pages from may use a character set that is different from that of your database. In that case, specify the url_charset as the Web server character set so that the characters that need to be escaped are escaped in the target character set. For example, a user of an EBCDIC database who wants to access an ASCII Web server should escape the URL using US7ASCII so that a space is escaped as %20 (hex code of a space in ASCII) instead of %40 (hex code of a space in EBCDIC). This function does not validate a URL for the proper URL format.