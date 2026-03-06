---
id: 19c__OWA_UTIL
name: OWA_UTIL
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL

OWA_UTIL uses Types to specify creating information.

## Syntax

```sql
TYPE dateType IS TABLE OF VARCHAR2(10) INDEX BY BINARY_INTEGER;
```

## Usage Notes

DATETYPE Datatype IDENT_ARR Datatype IP_ADDRESS Datatype TYPE dateType IS TABLE OF VARCHAR2(10) INDEX BY BINARY_INTEGER; TYPE ident_arr IS TABLE OF VARCHAR2(30) INDEX BY BINARY_INTEGER; TYPE ip_address IS TABLE OF INTEGER INDEX BY BINARY_INTEGER;