---
id: 19c__DBMS_RLS.REFRESH_POLICY
name: DBMS_RLS.REFRESH_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.REFRESH_POLICY

This procedure causes all the cached statements associated with the policy to be reparsed. This guarantees that the latest change to this policy will have immediate effect after the procedure is executed.

## Syntax

```sql
DBMS_RLS.REFRESH_POLICY (
   object_schema IN VARCHAR2 NULL,
   object_name   IN VARCHAR2 NULL,
   policy_name   IN VARCHAR2 NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of table, view, or synonym with which the policy is associated |
| policy_name | VARCHAR2 | IN | Name of policy to be refreshed |

## Usage Notes

The procedure causes the current transaction, if any, to commit before the operation is carried out. However, this does not cause a commit first if it is inside a DDL event trigger. See Also: Operational Notes A COMMIT is also performed at the end of the operation. See Also: Operational Notes Syntax DBMS_RLS.REFRESH_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2 NULL, policy_name IN VARCHAR2 NULL); Parameters Table 146-18 REFRESH_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of table, view, or synonym with which the policy is associated policy_name Name of policy to be refreshed Usage Notes The procedure returns an error if it tries to refresh a disabled policy. The procedure removes the cached results of context and shared sensitive VPD policies.