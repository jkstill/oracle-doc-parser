---
id: 19c__DBMS_UTILITY.ACTIVE_INSTANCES
name: DBMS_UTILITY.ACTIVE_INSTANCES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.ACTIVE_INSTANCES

This procedure returns the active instance.

## Syntax

```sql
DBMS_UTILITY.ACTIVE_INSTANCES (
   instance_table   OUT INSTANCE_TABLE,
   instance_count   OUT NUMBER);
```

## Usage Notes

Syntax DBMS_UTILITY.ACTIVE_INSTANCES ( instance_table OUT INSTANCE_TABLE, instance_count OUT NUMBER); Parameters Table 187-5 ACTIVE_INSTANCES Procedure Parameters Procedure Description instance_table Contains a list of the active instance numbers and names. When no instance is up, the list is empty. instance_count Number of active instances