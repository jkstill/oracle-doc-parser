---
id: 19c__DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE
name: DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE

This procedure grants the specified object privilege on the specified object to the specified user or role. If a user owns the object, then the user automatically is granted all privileges on the object, with grant option.

## Syntax

```sql
DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE(
   privilege     IN  BINARY_INTEGER,
   object_name   IN  VARCHAR2,
   grantee       IN  VARCHAR2,
   grant_option  IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The name of the object privilege to grant to the grantee on the object. See " Usage Notes " for the available object privileges. |
| object_name | VARCHAR2 | IN | The name of the object for which you are granting the privilege to the grantee, specified as [ schema_name .] object_name . For example, to grant the privilege on a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. |
| grantee | VARCHAR2 | IN | The name of the user or role for which the privilege is granted. The specified user cannot be the owner of the object. |
| grant_option | BOOLEAN | IN | If TRUE , then the specified user or users granted the specified privilege can grant this privilege to others. If FALSE , then the specified user or users granted the specified privilege cannot grant this privilege to others. |

## Usage Notes

Syntax DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE( privilege IN BINARY_INTEGER, object_name IN VARCHAR2, grantee IN VARCHAR2, grant_option IN BOOLEAN DEFAULT FALSE); Parameters Table 150-11 GRANT_OBJECT_PRIVILEGE Procedure Parameters Parameter Description privilege The name of the object privilege to grant to the grantee on the object. See " Usage Notes " for the available object privileges. object_name The name of the object for which you are granting the privilege to the grantee, specified as [ schema_name .] object_name . For example, to grant the privilege on a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. grantee The name of the user or role for which the privilege is granted. The specified user cannot be the owner of the object. grant_option If TRUE , then the specified user or users granted the specified privilege can grant this privilege to others. If FALSE , then the specified user or users granted the specified privilege cannot grant this privilege to others. Usage Notes To run this procedure, a user must meet at least one of the following requirements: Be the owner of the object on which the privilege is granted Have the same privilege as the privilege being granted with the grant option In addition, if the object is a rule set, then the user must have EXECUTE privilege on all the rules in the rule set with grant option or must own the rules in the rule set. Table 150-12 lists the object privileges. Table 150-12 Object Privileges for Evaluation Contexts, Rules, and Rule Sets Privilege Description SYS.DBMS_RULE_ADM.ALL_ON_EVALUATION_CONTEXT Alter and execute a particular evaluation context in another user's schema SYS.DBMS_RULE_ADM.ALL_ON_RULE Alter and execute a particular rule in another user's schema SYS.DBMS_RULE_ADM.ALL_ON_RULE_SET Alter and execute a particular rule set in another user's schema SYS.DBMS_RULE_ADM.ALTER_ON_EVALUATION_CONTEXT Alter a particular evaluation context in another user's schema SYS.DBMS_RULE_ADM.ALTER_ON_RULE Alter a particular rule in another user's schema SYS.DBMS_RULE_ADM.ALTER_ON_RULE_SET Alter a particular rule set in another user's schema SYS.DBMS_RULE_ADM.EXECUTE_ON_EVALUATION_CONTEXT Execute a particular evaluation context in another user's schema SYS.DBMS_RULE_ADM.EXECUTE_ON_RULE Execute a particular rule in another user's schema SYS.DBMS_RULE_ADM.EXECUTE_ON_RULE_SET Execute a particular rule set in another user's schema Examples For example, to grant the HR user the privilege to alter a rule named hr_dml in the strmadmin schema, enter the following: BEGIN DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE( privilege => SYS.DBMS_RULE_ADM.ALTER_ON_RULE, object_name => 'strmadmin.hr_dml', grantee => 'hr', grant_option => FALSE); END; /