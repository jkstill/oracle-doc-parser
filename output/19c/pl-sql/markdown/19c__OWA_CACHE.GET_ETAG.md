---
id: 19c__OWA_CACHE.GET_ETAG
name: OWA_CACHE.GET_ETAG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.GET_ETAG

This function returns the tag associated with the cached content. It is used in the Validation technique only.

## Syntax

```sql
OWA_CACHE.GET_ETAG
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax OWA_CACHE.GET_ETAG RETURN VARCHAR2; Return Values The tag for cache hit, otherwise NULL .