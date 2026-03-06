---
id: 19c__DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE
name: DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE

This procedure grant the specified system privilege to the specified user or role.

## Syntax

```sql
DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE(
   privilege     IN  BINARY_INTEGER,
   grantee       IN  VARCHAR2,
   grant_option  IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The name of the system privilege to grant to the grantee. |
| grantee | VARCHAR2 | IN | The name of the user or role for which the privilege is granted |
| grant_option | BOOLEAN | IN | If TRUE , then the specified user or users granted the specified privilege can grant the system privilege to others. If FALSE , then the specified user or users granted the specified privilege cannot grant the system privilege to others. |

## Usage Notes

Syntax DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE( privilege IN BINARY_INTEGER, grantee IN VARCHAR2, grant_option IN BOOLEAN DEFAULT FALSE); Parameters Table 150-13 GRANT_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The name of the system privilege to grant to the grantee. grantee The name of the user or role for which the privilege is granted grant_option If TRUE , then the specified user or users granted the specified privilege can grant the system privilege to others. If FALSE , then the specified user or users granted the specified privilege cannot grant the system privilege to others. Usage Notes Table 150-14 lists the system privileges. Table 150-14 System Privileges for Evaluation Contexts, Rules, and Rule Sets Privilege Description SYS.DBMS_RULE_ADM.ALTER_ANY_EVALUATION_CONTEXT Alter any evaluation context owned by any user SYS.DBMS_RULE_ADM.ALTER_ANY_RULE Alter any rule owned by any user SYS.DBMS_RULE_ADM.ALTER_ANY_RULE_SET Alter any rule set owned by any user SYS.DBMS_RULE_ADM.CREATE_ANY_EVALUATION_CONTEXT Create a new evaluation context in any schema SYS.DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT_OBJ Create a new evaluation context in the grantee's schema SYS.DBMS_RULE_ADM.CREATE_ANY_RULE Create a new rule in any schema SYS.DBMS_RULE_ADM.CREATE_RULE_OBJ Create a new rule in the grantee's schema SYS.DBMS_RULE_ADM.CREATE_ANY_RULE_SET Create a new rule set in any schema SYS.DBMS_RULE_ADM.CREATE_RULE_SET_OBJ Create a new rule set in the grantee's schema SYS.DBMS_RULE_ADM.DROP_ANY_EVALUATION_CONTEXT Drop any evaluation context in any schema SYS.DBMS_RULE_ADM.DROP_ANY_RULE Drop any rule in any schema SYS.DBMS_RULE_ADM.DROP_ANY_RULE_SET Drop any rule set in any schema SYS.DBMS_RULE_ADM.EXECUTE_ANY_EVALUATION_CONTEXT Execute any evaluation context owned by any user SYS.DBMS_RULE_ADM.EXECUTE_ANY_RULE Execute any rule owned by any user SYS.DBMS_RULE_ADM.EXECUTE_ANY_RULE_SET Execute any rule set owned by any user For example, to grant the strmadmin user the privilege to create a rule set in any schema, enter the following: BEGIN DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE( privilege => SYS.DBMS_RULE_ADM.CREATE_ANY_RULE_SET, grantee => 'strmadmin', grant_option => FALSE); END; /