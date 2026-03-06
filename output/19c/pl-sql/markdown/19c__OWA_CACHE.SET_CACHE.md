---
id: 19c__OWA_CACHE.SET_CACHE
name: OWA_CACHE.SET_CACHE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.SET_CACHE

This procedure sets up the cache headers for validation model cache type.

## Syntax

```sql
OWA_CACHE.SET_CACHE(
   p_etag        IN       VARCHAR2,
   p_level       IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_etag | VARCHAR2 | IN | The etag associated with this content |
| p_level | VARCHAR2) | IN | The caching level (' USER' or ' SYSTEM' ). |

## Usage Notes

Syntax OWA_CACHE.SET_CACHE( p_etag IN VARCHAR2, p_level IN VARCHAR2); Parameters Table 222-2 SET_CACHE Procedure Parameters Parameter Description p_etag The etag associated with this content p_level The caching level (' USER' or ' SYSTEM' ). Exceptions VALUE_ERROR is thrown if p_etag is greater than 55 p_level is not ' USER ' or ' SYSTEM '