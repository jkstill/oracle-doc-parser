---
id: 19c__DBMS_UTILITY.CURRENT_INSTANCE
name: DBMS_UTILITY.CURRENT_INSTANCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.CURRENT_INSTANCE

This function returns the current connected instance number. It returns NULL when connected instance is down.

## Syntax

```sql
DBMS_UTILITY.CURRENT_INSTANCE
   RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.CURRENT_INSTANCE RETURN NUMBER;