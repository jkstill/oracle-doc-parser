---
id: 19c__OWA_UTIL.MIME_HEADER
name: OWA_UTIL.MIME_HEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.MIME_HEADER

This procedure changes the default MIME header that the script returns. This procedure must come before any HTP.PRIN T or HTP.PRN calls to direct the script not to use the default MIME header.

## Syntax

```sql
OWA_UTIL.MIME_HEADER(
   ccontent_type    IN       VARCHAR2   DEFAULT 'text/html',
   bclose_header    IN       BOOLEAN    DEFAULT TRUE,
   ccharset         IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ccontent_type | VARCHAR2 | IN | The MIME type to generate |
| bclose_header | BOOLEAN | IN | Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. |
| ccharset | VARCHAR2 | IN | The character set to use.The character set only makes sense if the MIME type is of type 'text'. Therefore, the character set is only tagged on to the Content-Type header only if the MIME type passed in is of type 'text'. Any other MIME type, such as 'image', will not have any character set tagged on. |

## Usage Notes

Syntax OWA_UTIL.MIME_HEADER( ccontent_type IN VARCHAR2 DEFAULT 'text/html', bclose_header IN BOOLEAN DEFAULT TRUE, ccharset IN VARCHAR2 DEFAULT NULL); Parameters Table 230-8 MIME_HEADER Procedure Parameters Parameter Description ccontent_type The MIME type to generate bclose_header Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. ccharset The character set to use.The character set only makes sense if the MIME type is of type 'text'. Therefore, the character set is only tagged on to the Content-Type header only if the MIME type passed in is of type 'text'. Any other MIME type, such as 'image', will not have any character set tagged on. Examples Content-type: <ccontent_type>; charset=<ccharset> so that owa_util.mime_header('text/plain', false, 'ISO-8859-4') generates Content-type: text/plain; charset=ISO-8859-4\n