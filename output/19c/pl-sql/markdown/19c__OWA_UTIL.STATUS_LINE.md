---
id: 19c__OWA_UTIL.STATUS_LINE
name: OWA_UTIL.STATUS_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.STATUS_LINE

This procedure sends a standard HTTP status code to the client.

## Syntax

```sql
OWA_UTIL.STATUS_LINE(
   nstatus        IN       INTEGER,
   creason        IN       VARCHAR2   DEFAULT NULL,
   bclose_header  IN       BOOLEAN    DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nstatus | INTEGER | IN | The status code. |
| creason | VARCHAR2 | IN | The string for the status code. |
| bclose_header | BOOLEAN | IN | Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. |

## Usage Notes

This procedure must come before any htp.print or htp.prn calls so that the status code is returned as part of the header, rather than as "content data". Syntax OWA_UTIL.STATUS_LINE( nstatus IN INTEGER, creason IN VARCHAR2 DEFAULT NULL, bclose_header IN BOOLEAN DEFAULT TRUE); Parameters Table 230-12 STATUS_LINE Procedure Parameters Parameter Description nstatus The status code. creason The string for the status code. bclose_header Whether or not to close the HTTP header. If TRUE , two newlines are sent, which closes the HTTP header. Otherwise, one newline is sent, and the HTTP header remains open. Examples This procedure generates Status: < nstatus > < creason >\n\n