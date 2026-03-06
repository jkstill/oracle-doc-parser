---
id: 19c__DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS
name: DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS

This procedure captures the privileges that are used by definer’s rights and invoker’s rights PL/SQL program units for compilation.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS ();
```

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS (); Parameters This procedure has no parameters. Usage Notes Every rerun of the DBMS_PRIVILEGE_CAPTURE.CAPTURE_DEPENDENCY_PRIVS procedure deletes any existing records from the privilege analysis data dictionary views. It then recaptures records based on the existing PL/SQL program units.