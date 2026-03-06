---
id: 19c__DBMS_METADATA_DIFF.CLOSE
name: DBMS_METADATA_DIFF.CLOSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_METADATA_DIFF
tags: [dbms_metadata_diff]
source_file: DBMS_METADATA_DIFF.html
---

# DBMS_METADATA_DIFF.CLOSE

This procedure invalidates the handle returned by OPENC and cleans up associated state.

## Syntax

```sql
DBMS_METADATA_DIFF.CLOSE(
handle IN NUMBER);
```

## Usage Notes

Syntax DBMS_METADATA_DIFF.CLOSE( handle IN NUMBER); Parameters Table 108-6 CLOSE Function Parameters Parameters Description handle The handle returned from OPENC Exceptions INVALID_ARGVAL A NULL or invalid value was supplied for an input parameter. The error message text identifies the parameter.