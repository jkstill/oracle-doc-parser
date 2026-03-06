---
id: 19c__OWA_UTIL.SHOWSOURCE
name: OWA_UTIL.SHOWSOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.SHOWSOURCE

This procedure prints the source of the specified procedure, function, or package. If a procedure or function which belongs to a package is specified, then the entire package is displayed.

## Syntax

```sql
OWA_UTIL.SHOWSOURCE (
   cname      IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cname | VARCHAR2) | IN | The function or procedure whose source you want to show. |

## Usage Notes

Syntax OWA_UTIL.SHOWSOURCE ( cname IN VARCHAR2); Parameters Table 230-10 SHOWSOURCE Procedure Parameters Parameter Description cname The function or procedure whose source you want to show.