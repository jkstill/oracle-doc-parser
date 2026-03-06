---
id: 19c__DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE
name: DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE_ADM
tags: [dbms_rule_adm]
source_file: DBMS_RULE_ADM.html
---

# DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE

This procedure revokes the specified system privilege from the specified user or role.

## Syntax

```sql
DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE(
   privilege  IN  BINARY_INTEGER,
   revokee    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| privilege | BINARY_INTEGER | IN | The name of the system privilege to revoke from the revokee. See GRANT_SYSTEM_PRIVILEGE Procedure for a list of the system privileges. |
| revokee | VARCHAR2) | IN | The name of the user or role from which the privilege is revoked |

## Usage Notes

Syntax DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE( privilege IN BINARY_INTEGER, revokee IN VARCHAR2); Parameters Table 150-17 REVOKE_SYSTEM_PRIVILEGE Procedure Parameters Parameter Description privilege The name of the system privilege to revoke from the revokee. See GRANT_SYSTEM_PRIVILEGE Procedure for a list of the system privileges. revokee The name of the user or role from which the privilege is revoked