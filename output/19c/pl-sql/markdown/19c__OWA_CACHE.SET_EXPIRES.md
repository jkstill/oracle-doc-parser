---
id: 19c__OWA_CACHE.SET_EXPIRES
name: OWA_CACHE.SET_EXPIRES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.SET_EXPIRES

This procedure sets up the cache headers for expires model cache type.

## Syntax

```sql
OWA_CACHE.SET_EXPIRES(
   p_expires      IN       NUMBER,
   p_level        IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_expires | NUMBER | IN | The number of minutes this content is valid. |
| p_level | VARCHAR2) | IN | The caching level (' USER' or ' SYSTEM' ). |

## Usage Notes

Syntax OWA_CACHE.SET_EXPIRES( p_expires IN NUMBER, p_level IN VARCHAR2); Parameters Table 222-3 SET_EXPIRES Procedure Parameters Parameter Description p_expires The number of minutes this content is valid. p_level The caching level (' USER' or ' SYSTEM' ). Exceptions VALUE_ERROR is thrown if p_expires is negative or zero p_level is not ' USER ' or ' SYSTEM ' p_expires is > 525600 (1 year)