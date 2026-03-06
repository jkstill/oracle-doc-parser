---
id: 19c__DBMS_RLS.ALTER_POLICY
name: DBMS_RLS.ALTER_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RLS
tags: [dbms_rls]
source_file: DBMS_RLS.html
---

# DBMS_RLS.ALTER_POLICY

This procedure associates an application context attribute with VPD policies.

## Syntax

```sql
DBMS_RLS.ALTER_POLICY (
   object_schema    IN VARCHAR2 DEFAULT NULL,
   object_name      IN VARCHAR2,
   policy_name      IN VARCHAR2,
   alter_option     IN NUMBER,
   namespace        IN VARCHAR2 DEFAULT NULL,
   attribute        IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. |
| object_name | VARCHAR2 | IN | Name of the table, view, or synonym to which the policy is added |
| policy_name | VARCHAR2 | IN | Name of the policy, unique for the same table or view |
| alter_option | NUMBER | IN | Used to determine whether the application context is being added or removed from an Oracle Virtual Private Database policy |
| namespace | VARCHAR2 | IN | Name which determines the application context namespace |
| attribute | VARCHAR2 | IN | Attribute which determines the application context attribute name |

## Usage Notes

Syntax DBMS_RLS.ALTER_POLICY ( object_schema IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2, policy_name IN VARCHAR2, alter_option IN NUMBER, namespace IN VARCHAR2 DEFAULT NULL, attribute IN VARCHAR2 DEFAULT NULL); Parameters Table 146-7 ALTER_POLICY Procedure Parameters Parameter Description object_schema Schema containing the table, view, or synonym. If no object_schema is specified or is NULL , then the current schema is used. object_name Name of the table, view, or synonym to which the policy is added policy_name Name of the policy, unique for the same table or view alter_option Used to determine whether the application context is being added or removed from an Oracle Virtual Private Database policy namespace Name which determines the application context namespace attribute Attribute which determines the application context attribute name Usage Notes Note the following: This procedure associates an application context namespace and application context attribute to context sensitive and shared context sensitive policies only. Specifying application context namespace and application context attribute for DYNAMIC , STATIC or SHARED_STATIC policies will result in an error. If namespace is specified, attribute should also be specified for the procedure call. You cannot associate a global application context with a context sensitive policy or a context shared sensitive policy. Invocations of ALTER_POLICY which modify a shared context sensitive VPD policy have an effect on all shared context sensitive VPD policies that have the same VPD policy function. The driving context can be session or global. At execution time, the server retrieves the name of the active policy group from the value of this context. There must be at least one driving context defined for each object that has fine-grained access control policies; otherwise, all policies for the object will be executed. Adding multiple context to the same object will cause policies from multiple policy groups to be enforced. If the driving context is NULL, policies from all policy groups are used. If the driving context is a policy group with policies, all enabled policies from that policy group will be applied, along with all policies from the SYS_DEFAULT policy group. To add a policy to table hr.employees in group access_control_group, the following command is issued: DBMS_RLS.ADD_GROUPED_POLICY( 'hr','employees','access_control_group','policy1','SYS', 'HR.ACCESS');