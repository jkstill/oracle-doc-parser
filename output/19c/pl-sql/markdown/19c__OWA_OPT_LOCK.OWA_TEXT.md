---
id: 19c__OWA_OPT_LOCK.OWA_TEXT
name: OWA_OPT_LOCK.OWA_TEXT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_OPT_LOCK
tags: [owa_opt_lock]
source_file: OWA_OPT_LOCK.html
---

# OWA_OPT_LOCK.OWA_TEXT

This datatype is a PL/SQL table intended to hold ROWIDs.

## Syntax

```sql
TYPE VCARRAY IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER
```

## Usage Notes

TYPE VCARRAY IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER Note that this is different from the OWA_TEXT . VC_ARR DATA TYPE .