---
id: 19c__OWA_CACHE.GET_LEVEL
name: OWA_CACHE.GET_LEVEL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.GET_LEVEL

This returns the caching level. It is used in the Validation technique model only.

## Syntax

```sql
OWA_CACHE.GET_LEVEL
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax OWA_CACHE.GET_LEVEL RETURN VARCHAR2; Return Values The caching level string (' USER ' or ' SYSTEM ') for cache hit, otherwise NULL .