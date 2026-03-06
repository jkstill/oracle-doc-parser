---
id: 19c__DBMS_RLS.DROP_GROUPED_POLICY
name: DBMS_RLS.DROP_GROUPED_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.DROP_GROUPED_POLICY

This procedure drops a policy associated with a policy group.

## Syntax

```sql
DBMS_RLS.DROP_GROUPED_POLICY (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2,
   policy_group    IN VARCHAR2 'SYS_DEFAULT',
   policy_name     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is dropped |
| policy_group | VARCHAR2 | IN | Name of the policy group to which the policy belongs |
| policy_name | VARCHAR2) | IN | Name of the policy |

## Usage Notes

Syntax DBMS_RLS.DROP_GROUPED_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, policy_group IN VARCHAR2 'SYS_DEFAULT', policy_name IN VARCHAR2); Parameters Table 146-12 DROP_GROUPED_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is dropped policy_group Name of the policy group to which the policy belongs policy_name Name of the policy