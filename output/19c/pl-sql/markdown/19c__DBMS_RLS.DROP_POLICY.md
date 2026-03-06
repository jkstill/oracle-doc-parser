---
id: 19c__DBMS_RLS.DROP_POLICY
name: DBMS_RLS.DROP_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.DROP_POLICY

This procedure drops a fine-grained access control policy from a table, view, or synonym.

## Syntax

```sql
DBMS_RLS.DROP_POLICY (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2,
   policy_name     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view or synonym. If no object_schema is specified, or NULL is provided, then the current user's schema is assumed. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym for which the policy is dropped |
| policy_name | VARCHAR2) | IN | Name of policy to be dropped from table, view, or synonym |

## Usage Notes

The procedure causes the current transaction, if any, to commit before the operation is carried out. However, this does not cause a commit first if it is inside a DDL event trigger. See Also: Operational Notes A COMMIT is also performed at the end of the operation. See Also: Operational Notes Syntax DBMS_RLS.DROP_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, policy_name IN VARCHAR2); Parameters Table 146-13 DROP_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view or synonym. If no object_schema is specified, or NULL is provided, then the current user's schema is assumed. object_name Name of the table, view, or synonym for which the policy is dropped policy_name Name of policy to be dropped from table, view, or synonym Usage Notes When you drop a VPD policy from a synonym, it causes all the dependent objects of the synonym, including policy functions that reference the synonym, to be marked INVALID .