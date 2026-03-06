---
id: 19c__OWA_UTIL.TODATE
name: OWA_UTIL.TODATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.TODATE

This function converts the DATETYPE Datatype to the standard Oracle DATE type.

## Syntax

```sql
OWA_UTIL.TODATE(
   p_dateArray      IN     dateType) 
 RETURN DATE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_dateArray | dateType) | IN | The value to convert. |

**Returns:** `DATE`

## Usage Notes

Syntax OWA_UTIL.TODATE( p_dateArray IN dateType) RETURN DATE; Parameters Table 230-14 TODATE Function Parameters Parameter Description p_dateArray The value to convert.