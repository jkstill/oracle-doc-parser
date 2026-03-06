---
id: 19c__OWA_OPT_LOCK.GET_ROWID
name: OWA_OPT_LOCK.GET_ROWID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_OPT_LOCK
tags: [owa_opt_lock]
source_file: OWA_OPT_LOCK.html
---

# OWA_OPT_LOCK.GET_ROWID

This function returns the ROWID datatype from the specified OWA_OPT_LOCK.VCARRAY DATA TYPE.

## Syntax

```sql
OWA_OPT_LOCK.GET_ROWID(
   p_old_values      IN      vcarray) 
 RETURN ROWID;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_old_values | vcarray) | IN | This parameter is usually passed in from an HTML form. |

**Returns:** `ROWID`

## Usage Notes

Syntax OWA_OPT_LOCK.GET_ROWID( p_old_values IN vcarray) RETURN ROWID; Parameters Table 226-3 GET_ROWID Function Parameters Parameter Description p_old_values This parameter is usually passed in from an HTML form.