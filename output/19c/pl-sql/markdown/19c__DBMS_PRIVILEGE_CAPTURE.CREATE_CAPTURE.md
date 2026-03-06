---
id: 19c__DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE
name: DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE

This procedure creates a privilege analysis policy that specifies the conditions for analyzing privilege use. It also optionally specifies the roles for which privilege use is to be analyzed, and the conditions under which privilege use is to be analyzed.

## Syntax

```sql
DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE (
   name            IN  VARCHAR2,
   description     IN  VARCHAR2 DEFAULT NULL, 
   type            IN  NUMBER DEFAULT G_DATABASE,
   roles           IN  ROLE_NAME_LIST DEFAULT ROLE_NAME_LIST(),
   condition       IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the privilege analysis policy. A string of size up to 30 characters. |
| description | VARCHAR2 | IN | Description of the policy (up to 1024 characters) |
| type | NUMBER | IN | Type of the privilege analysis policy. Possible values are: G_DATABASE : Captures all privilege use in the database, except privileges used by the SYS user. G_ROLE : Captures the use of a privilege if the privilege is part of a specified role or list of roles. G_CONTEXT : Captures the use of a privilege if the context specified by the condition parameter evaluates to true. G_ROLE_AND_CONTEXT : Captures the use of a privilege if the privilege is part of the specified list of roles and when the condition specified by the condition parameter is true. |
| roles | ROLE_NAME_LIST | IN | The roles whose privileges are to be analyzed. Required if the type is G_ROLE or G_ROLE_AND_CONTEXT . |
| condition | VARCHAR2 | IN | PL/SQL boolean expression containing up to 4000 characters. Required if type is G_CONTEXT or G_ROLE_AND_CONTEXT . Note that the boolean expression can only contain SYS_CONTEXT , but not other functions. |

## Usage Notes

Syntax DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE ( name IN VARCHAR2, description IN VARCHAR2 DEFAULT NULL, type IN NUMBER DEFAULT G_DATABASE, roles IN ROLE_NAME_LIST DEFAULT ROLE_NAME_LIST(), condition IN VARCHAR2 DEFAULT NULL); Parameters Table 131-3 CREATE_CAPTURE Procedure Parameters Parameter Description name Name of the privilege analysis policy. A string of size up to 30 characters. description Description of the policy (up to 1024 characters) type Type of the privilege analysis policy. Possible values are: G_DATABASE : Captures all privilege use in the database, except privileges used by the SYS user. G_ROLE : Captures the use of a privilege if the privilege is part of a specified role or list of roles. G_CONTEXT : Captures the use of a privilege if the context specified by the condition parameter evaluates to true. G_ROLE_AND_CONTEXT : Captures the use of a privilege if the privilege is part of the specified list of roles and when the condition specified by the condition parameter is true. roles The roles whose privileges are to be analyzed. Required if the type is G_ROLE or G_ROLE_AND_CONTEXT . condition PL/SQL boolean expression containing up to 4000 characters. Required if type is G_CONTEXT or G_ROLE_AND_CONTEXT . Note that the boolean expression can only contain SYS_CONTEXT , but not other functions. Usage Notes When using role-based analysis for the CREATE_CAPTURE procedure, privilege use is analyzed even if the privilege is indirectly granted to the specified role. For example, say role R2 contains role R1, and R1 contains privilege P1. If the privilege policy includes only role R2, any use of the P1 privilege is still analyzed, as privilege P1 is an indirect part of role R2. When using the condition parameter, use the following syntax for the PL/SQL expression: condition::= predicate | ( predicate1 ) AND ( predicate2 ) | ( predicate1 ) OR ( predicate2 ) Where, predicate::= sys_context( namespace , attribute ) relop constant_value | sys_context( namespace , attribute ) between constant_value and constant_value | sys_context(namespace, attribute) in {constant_value (, constant_value )* } Where, relop::= = | < | <= | > | >= | <> A privilege analysis policy cannot analyze the use of SYS user privileges.