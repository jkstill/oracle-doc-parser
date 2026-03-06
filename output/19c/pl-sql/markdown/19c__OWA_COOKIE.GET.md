---
id: 19c__OWA_COOKIE.GET
name: OWA_COOKIE.GET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_COOKIE
tags: [owa_cookie]
source_file: OWA_COOKIE.html
---

# OWA_COOKIE.GET

This function returns the values associated with the specified cookie. The values are returned in a OWA_COOKIE.COOKIE DATA TYPE .

## Syntax

```sql
OWA_COOKIE.GET(
    name           IN       VARCHAR2) 
  RETURN COOKIE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | The name of the cookie. |

**Returns:** `COOKIE`

## Usage Notes

Syntax OWA_COOKIE.GET( name IN VARCHAR2) RETURN COOKIE; Parameters Table 223-2 GET Function Parameters Parameter Description name The name of the cookie. Return Values OWA_COOKIE.COOKIE DATA TYPE .