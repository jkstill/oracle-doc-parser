---
id: 19c__DBMS_RLS.ADD_POLICY_CONTEXT
name: DBMS_RLS.ADD_POLICY_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.ADD_POLICY_CONTEXT

This procedure adds the context for the active application.

## Syntax

```sql
DBMS_RLS.ADD_POLICY_CONTEXT (
   object_schema   IN VARCHAR2 NULL,
   object_name     IN VARCHAR2,
   namespace       IN VARCHAR2,
   attribute       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is added. |
| namespace | VARCHAR2 | IN | Name which determines the application context namespace |
| attribute | VARCHAR2) | IN | Attribute which determines the application context attribute name |

## Usage Notes

Syntax DBMS_RLS.ADD_POLICY_CONTEXT ( object_schema IN VARCHAR2 NULL, object_name IN VARCHAR2, namespace IN VARCHAR2, attribute IN VARCHAR2); Parameters Table 146-6 ADD_POLICY_CONTEXT Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is added. namespace Name which determines the application context namespace attribute Attribute which determines the application context attribute name Usage Notes Note the following: This procedure indicates the application context that drives the enforcement of policies; this is the context that determines which application is running. The driving context can be session or global. At execution time, the server retrieves the name of the active policy group from the value of this context. There must be at least one driving context defined for each object that has fine-grained access control policies; otherwise, all policies for the object will be executed. Adding multiple context to the same object will cause policies from multiple policy groups to be enforced. If the driving context is NULL, policies from all policy groups are used. If the driving context is a policy group with policies, all enabled policies from that policy group will be applied, along with all policies from the SYS_DEFAULT policy group. To add a policy to table HR.EMPLOYEES in group access_control_group, the following command is issued: DBMS_RLS.ADD_GROUPED_POLICY('hr','employees','access_control_group','policy1','SYS', 'HR.ACCESS');