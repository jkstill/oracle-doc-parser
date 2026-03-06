---
id: 19c__DBMS_AQADM.DEL_ALIAS_FROM_LDAP
name: DBMS_AQADM.DEL_ALIAS_FROM_LDAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DEL_ALIAS_FROM_LDAP

This procedure drops an alias for a queue, agent, or JMS ConnectionFactory in LDAP.

## Syntax

```sql
DBMS_AQADM.DEL_ALIAS_FROM_LDAP(
   alias IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| alias | VARCHAR2) | IN | The alias to be removed. |

## Usage Notes

Syntax DBMS_AQADM.DEL_ALIAS_FROM_LDAP( alias IN VARCHAR2); Parameters Table 23-25 DEL_ALIAS_FROM_LDAP Procedure Parameters Parameter Description alias The alias to be removed.