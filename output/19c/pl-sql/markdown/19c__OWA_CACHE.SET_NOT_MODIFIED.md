---
id: 19c__OWA_CACHE.SET_NOT_MODIFIED
name: OWA_CACHE.SET_NOT_MODIFIED
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.SET_NOT_MODIFIED

This procedure sets up the headers for a not-modified cache hit. It is used in the Validation technique only.

## Syntax

```sql
OWA_CACHE.SET_NOT_MODIFIED;
```

## Usage Notes

Syntax OWA_CACHE.SET_NOT_MODIFIED; Exceptions VALUE_ERROR is thrown if If the etag was not passed in