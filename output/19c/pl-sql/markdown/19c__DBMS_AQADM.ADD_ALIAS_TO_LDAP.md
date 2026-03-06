---
id: 19c__DBMS_AQADM.ADD_ALIAS_TO_LDAP
name: DBMS_AQADM.ADD_ALIAS_TO_LDAP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ADD_ALIAS_TO_LDAP

This procedure creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP. The alias will be placed directly under the database server's distinguished name in LDAP hierarchy.

## Syntax

```sql
DBMS_AQADM.ADD_ALIAS_TO_LDAP(
   alias          IN VARCHAR2,
   obj_location   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| alias | VARCHAR2 | IN | Name of the alias. Example: west_shipping. |
| obj_location | VARCHAR2) | IN | The distinguished name of the object (queue, agent or connection factory) to which alias refers. |

## Usage Notes

Syntax DBMS_AQADM.ADD_ALIAS_TO_LDAP( alias IN VARCHAR2, obj_location IN VARCHAR2); Parameters Table 23-11 ADD_ALIAS_TO_LDAP Procedure Parameters Parameter Description alias Name of the alias. Example: west_shipping. obj_location The distinguished name of the object (queue, agent or connection factory) to which alias refers. Usage Notes This method can be used to create aliases for queues, agents, and JMS ConnectionFactory objects. These object must exist before the alias is created. These aliases can be used for JNDI lookup in JMS and Oracle Database Advanced Queuing Internet access.