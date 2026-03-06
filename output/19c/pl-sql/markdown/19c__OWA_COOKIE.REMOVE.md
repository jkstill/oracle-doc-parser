---
id: 19c__OWA_COOKIE.REMOVE
name: OWA_COOKIE.REMOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_COOKIE
tags: [owa_cookie]
source_file: OWA_COOKIE.html
---

# OWA_COOKIE.REMOVE

This procedure forces a cookie to expire immediately by setting the "expires" field of a Set-Cookie line in the HTTP header to "01-Jan-1990".

## Syntax

```sql
OWA_COOKIE.REMOVE(
   name           IN       VARCHAR2,
   val            IN       VARCHAR2,
   path           IN       VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | The name of the cookie to expire. |
| val | VARCHAR2 | IN | The value of the cookie. |
| path | VARCHAR2 | IN | [Currently unused] |

## Usage Notes

This procedure must be called within the context of an HTTP header. Syntax OWA_COOKIE.REMOVE( name IN VARCHAR2, val IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 223-4 REMOVE Procedure Parameters Parameter Description name The name of the cookie to expire. val The value of the cookie. path [Currently unused]