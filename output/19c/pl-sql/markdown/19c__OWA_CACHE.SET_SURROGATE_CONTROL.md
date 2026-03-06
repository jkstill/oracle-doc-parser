---
id: 19c__OWA_CACHE.SET_SURROGATE_CONTROL
name: OWA_CACHE.SET_SURROGATE_CONTROL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_CACHE
tags: [owa_cache]
source_file: OWA_CACHE.html
---

# OWA_CACHE.SET_SURROGATE_CONTROL

This procedure sets the headers for a surrogate-control header for Web cache

## Syntax

```sql
OWA_CACHE.SET_SURROGATE_CONTROL(
   p_value        IN       VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_value | VARCHAR2) | IN | The value to be passed as the Surrogate-Control header. |

## Usage Notes

Syntax OWA_CACHE.SET_SURROGATE_CONTROL( p_value IN VARCHAR2); Parameters Table 222-4 SET_SURROGATE_CONTROL Procedure Parameters Parameter Description p_value The value to be passed as the Surrogate-Control header. Exceptions VALUE_ERROR is thrown if If p_value is greater than 55 in length.