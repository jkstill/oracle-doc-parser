---
id: 19c__DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA
name: DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA

This procedure submits pending changes for the resource manager. It clears the pending area after validating and committing the changes (if valid).

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA;
```

## Usage Notes

Note: A call to SUBMIT_PENDING_AREA may fail even if VALIDATE_PENDING_AREA succeeds. This may happen if a plan being deleted is loaded by an instance after a call to VALIDATE_PENDING_AREA , but before a call to SUBMIT_PENDING_AREA . Note: A call to SUBMIT_PENDING_AREA may fail even if VALIDATE_PENDING_AREA succeeds. This may happen if a plan being deleted is loaded by an instance after a call to VALIDATE_PENDING_AREA , but before a call to SUBMIT_PENDING_AREA . Syntax DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA;