---
id: 19c__DBMS_RLS.REFRESH_GROUPED_POLICY
name: DBMS_RLS.REFRESH_GROUPED_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.REFRESH_GROUPED_POLICY

This procedure reparses the SQL statements associated with a refreshed policy.

## Syntax

```sql
DBMS_RLS.REFRESH_GROUPED_POLICY (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2 NULL,
   group_name      IN VARCHAR2 NULL,
   policy_name     IN VARCHAR2 NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym with which the policy is associated |
| group_name | VARCHAR2 | IN | Name of the group of the policy |
| policy_name | VARCHAR2 | IN | Name of the policy |

## Usage Notes

Syntax DBMS_RLS.REFRESH_GROUPED_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2 NULL, group_name IN VARCHAR2 NULL, policy_name IN VARCHAR2 NULL); Parameters Table 146-17 REFRESH_GROUPED_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym with which the policy is associated group_name Name of the group of the policy policy_name Name of the policy Usage Notes This procedure causes all the cached statements associated with the policy to be reparsed. This guarantees that the latest change to the policy has immediate effect after the procedure is executed. The procedure causes the current transaction, if any, to commit before the operation is carried out. A commit is performed at the end of the operation. The procedure returns an error if it tries to refresh a disabled policy. The procedure removes the cached results of context and shared sensitive VPD policies.