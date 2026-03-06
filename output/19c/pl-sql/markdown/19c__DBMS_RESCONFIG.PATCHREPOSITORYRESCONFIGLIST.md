---
id: 19c__DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST
name: DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST

This procedure removes invalid references from the repository resource configuration list, and makes the repository available.

## Syntax

```sql
DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST;
```

## Usage Notes

Under normal circumstances, deletion of a resource configuration resource cannot be performed if it is part of the repository resource configuration list. If, for some reason, the deletion of a resource configuration resource that is part of the repository resource configuration list succeeds, then any repository operation results in a 'dangling reference' error. This procedure removes those invalid references. This procedure must be run as SYS . Syntax DBMS_RESCONFIG.PATCHREPOSITORYRESCONFIGLIST;