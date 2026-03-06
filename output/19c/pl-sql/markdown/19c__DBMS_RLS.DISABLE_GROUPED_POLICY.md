---
id: 19c__DBMS_RLS.DISABLE_GROUPED_POLICY
name: DBMS_RLS.DISABLE_GROUPED_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.DISABLE_GROUPED_POLICY

This procedure disables a row-level group security policy.

## Syntax

```sql
DBMS_RLS.DISABLE_GROUPED_POLICY (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2,
   group_name      IN VARCHAR2,
   policy_name     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym with which the policy is associated |
| group_name | VARCHAR2 | IN | Name of the group of the policy |
| policy_name | VARCHAR2) | IN | Name of the policy to be enabled or disabled |

## Usage Notes

Syntax DBMS_RLS.DISABLE_GROUPED_POLICY ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, group_name IN VARCHAR2, policy_name IN VARCHAR2); Parameters Table 146-11 DISABLE_GROUPED_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym object_name Name of the table, view, or synonym with which the policy is associated group_name Name of the group of the policy policy_name Name of the policy to be enabled or disabled Usage Notes The procedure causes the current transaction, if any, to commit before the operation is carried out. A commit is performed at the end of the operation. A policy is disabled when this procedure is executed or when the ENABLE_GROUPED_POLICY procedure is executed with "enable" set to FALSE .