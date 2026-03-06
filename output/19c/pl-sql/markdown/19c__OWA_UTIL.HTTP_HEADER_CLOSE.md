---
id: 19c__OWA_UTIL.HTTP_HEADER_CLOSE
name: OWA_UTIL.HTTP_HEADER_CLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.HTTP_HEADER_CLOSE

This procedure generates a newline character to close the HTTP header.

## Syntax

```sql
OWA_UTIL.HTTP_HEADER_CLOSE;
```

## Usage Notes

Syntax OWA_UTIL.HTTP_HEADER_CLOSE; Return Values A newline character, which closes the HTTP header. Usage Notes Use this procedure if you have not closed the header by using the bclose_header parameter in calls such as MIME_HEADER Procedure , REDIRECT_URL Procedure , or STATUS_LINE Procedure The HTTP header must be closed before any HTP.PRINT or HTP.PRN calls.