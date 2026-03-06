---
id: 19c__OWA_UTIL.REDIRECT_URL
name: OWA_UTIL.REDIRECT_URL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.REDIRECT_URL

This procedure specifies that the application server is to visit the specified URL. The URL may specify either a Web page to return or a program to execute.

## Syntax

```sql
OWA_UTIL.REDIRECT_URL(
   curl           IN       VARCHAR2
   bclose_header  IN       BOOLEAN    DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| curl | VARCHAR2 | IN | The URL to visit. |
| bclose_header | BOOLEAN | IN | Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. |

## Usage Notes

Syntax OWA_UTIL.REDIRECT_URL( curl IN VARCHAR2 bclose_header IN BOOLEAN DEFAULT TRUE); Parameters Table 230-9 REDIRECT_URL Procedure Parameters Parameter Description curl The URL to visit. bclose_header Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. Usage Notes This procedure must come before any HTP procedure or HTF function call. Examples This procedure generates Location: < curl >\n\n