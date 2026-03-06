---
id: 19c__DBMS_RLS.DELETE_POLICY_GROUP
name: DBMS_RLS.DELETE_POLICY_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.DELETE_POLICY_GROUP

This procedure deletes a policy group.

## Syntax

```sql
DBMS_RLS.DELETE_POLICY_GROUP (
  object_schema   IN VARCHAR2 NULL,
  object_name     IN VARCHAR2,
  policy_group    IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is added |
| policy_group | VARCHAR2) | IN | Name of the policy group that the policy belongs to |

## Usage Notes

Syntax DBMS_RLS.DELETE_POLICY_GROUP ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, policy_group IN VARCHAR2); Parameters Table 146-10 DELETE_POLICY_GROUP Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is added policy_group Name of the policy group that the policy belongs to Usage Notes Note the following: This procedure deletes a policy group for the specified table, view, or synonym. No policy can be in the policy group.