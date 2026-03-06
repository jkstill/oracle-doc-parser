---
id: 19c__DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE
name: DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE

This procedure revokes the specified object privilege on the specified object from the specified user or role.

## Syntax

```sql
DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE(
   privilege    IN  BINARY_INTEGER,
   object_name  IN  VARCHAR2,
   revokee      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The name of the object privilege on the object to revoke from the revokee. See GRANT_OBJECT_PRIVILEGE Procedure for a list of the object privileges. |
| object_name | VARCHAR2 | IN | The name of the object for which you are revoking the privilege from the revokee, specified as [ schema_name .] object_name . For example, to revoke an object privilege on a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. |
| revokee | VARCHAR2) | IN | The name of the user or role from which the privilege is revoked. The user who owns the object cannot be specified. |

## Usage Notes

Syntax DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE( privilege IN BINARY_INTEGER, object_name IN VARCHAR2, revokee IN VARCHAR2); Parameters Table 150-16 REVOKE_OBJECT_PRIVILEGE Procedure Parameters Parameter Description privilege The name of the object privilege on the object to revoke from the revokee. See GRANT_OBJECT_PRIVILEGE Procedure for a list of the object privileges. object_name The name of the object for which you are revoking the privilege from the revokee, specified as [ schema_name .] object_name . For example, to revoke an object privilege on a rule set named apply_rules in the hr schema, enter hr.apply_rules for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. revokee The name of the user or role from which the privilege is revoked. The user who owns the object cannot be specified.