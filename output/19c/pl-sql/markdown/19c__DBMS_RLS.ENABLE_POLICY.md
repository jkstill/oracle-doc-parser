---
id: 19c__DBMS_RLS.ENABLE_POLICY
name: DBMS_RLS.ENABLE_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.ENABLE_POLICY

This procedure enables or disables a fine-grained access control policy. A policy is enabled when it is created.

## Syntax

```sql
DBMS_RLS.ENABLE_POLICY (
   object_schema IN VARCHAR2 NULL,
   object_name   IN VARCHAR2,
   policy_name   IN VARCHAR2,
   enable        IN BOOLEAN TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of table, view, or synonym with which the policy is associated |
| policy_name | VARCHAR2 | IN | Name of policy to be enabled or disabled |
| enable | BOOLEAN | IN | TRUE to enable the policy, FALSE to disable the policy |

## Usage Notes

The procedure causes the current transaction, if any, to commit before the operation is carried out. However, this does not cause a commit first if it is inside a DDL event trigger. See Also: Operational Notes A COMMIT is also performed at the end of the operation. See Also: Operational Notes Syntax DBMS_RLS.ENABLE_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, policy_name IN VARCHAR2, enable IN BOOLEAN TRUE); Parameters Table 146-16 ENABLE_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of table, view, or synonym with which the policy is associated policy_name Name of policy to be enabled or disabled enable TRUE to enable the policy, FALSE to disable the policy